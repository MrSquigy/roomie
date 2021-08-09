# Copyright (c) 2021 Jonathan Vice

from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=30)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # auto_now_add uses date at time of record creation. Cannot be modified.
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
