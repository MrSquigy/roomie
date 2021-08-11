# Copyright (c) 2021 Jonathan Vice

from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import dateparse, timezone
from django.views import generic

from .forms import AddRoomForm, AddEventForm
from .models import Event, Room


class IndexView(generic.TemplateView):
    template_name = "scheduler/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add to page context here
        context["data"] = {
            "rooms": Room.objects.all(),
            "current_events": self.get_current_events(),
            "upcoming_events": self.get_upcoming_events(),
            "add_room_form": AddRoomForm(),
            "add_event_form": AddEventForm(),
            # TODO: "edit_event_form": EventForm(instance=?) check docs
        }

        return context

    def get_current_events(self):
        """Return events that are taking place now."""
        events = Event.objects.filter(start_time__lte=timezone.now()).filter(
            end_time__gte=timezone.now()
        )

        return events

    def get_upcoming_events(self):
        """Return events that will take place in the future."""
        # TODO: Add option to select how far to look for upcoming events
        events = Event.objects.filter(start_time__gte=timezone.now())

        return events


def add_room(request):
    Room.objects.create(name=request.POST["room_name"])

    return HttpResponseRedirect(reverse("scheduler:index"))


def add_event(request):
    room = get_object_or_404(Room, pk=request.POST["room"])
    start_date = (
        f"{request.POST['event-start-date']} {request.POST['event-start-time']}"
    )
    end_date = f"{request.POST['event-end-date']} {request.POST['event-end-time']}"

    start_date = dateparse.parse_datetime(start_date)
    end_date = dateparse.parse_datetime(end_date)

    Event.objects.create(
        name=request.POST["event_name"],
        room=room,
        start_time=start_date,
        end_time=end_date,
        request_date=timezone.now(),
    )

    return HttpResponseRedirect(reverse("scheduler:index"))
