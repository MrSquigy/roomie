# Copyright (c) 2021 Jonathan Vice

from django.contrib.admin import AdminSite

from .models import Event, Room


class RoomieAdmin(AdminSite):
    site_header = "Roomie Administration"


admin_site = RoomieAdmin(name="admin")
admin_site.register(Event)
admin_site.register(Room)
