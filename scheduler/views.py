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
        }

        return context

    def get_current_events(self):
        e = Event.objects.filter(start_time__lte=timezone.now()).filter(
            end_time__gte=timezone.now()
        )

        return e
