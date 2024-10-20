from django.db import models


class PhotoTypeChoices(models.TextChoices):
    TEAMS = "team", "Team"
    CLIENTS = "clients", "Clients"
