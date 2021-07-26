# Copyright (c) 2021 Jonathan Vice

from django.utils import timezone
from django.views import generic

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