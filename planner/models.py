from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Primary(models.Model):
    EMPTY = "EM"
    GREAT_HALL = "GH"
    MARKET = "MK"
    MONASTERY = "MN"
    LONGPHORT = "LP"
    PRIMARY = [
        (EMPTY, 'Empty'),
        (GREAT_HALL, 'Great Hall'),
        (MARKET, 'Market'),
        (MONASTERY, 'Monastery'),
        (LONGPHORT, 'Longphort'),
    ]

    primary_building = models.CharField(max_length=2, choices=PRIMARY, default=EMPTY)

    def __str__(self):
        return f"{self.primary_building}"


class Secondary(models.Model):
    EMPTY = "EM"
    BENEDICTINE_ABBEY = "BA"
    FARM = "FM"
    ORCHARD = "OR"
    PASTURE = "PA"
    HUNTING = "HN"
    FISHING = "FI"
    WOOD = "WD"
    GOLD = "GD"
    TIN = "TN"
    IRON = "IN"
    SILVER = "SL"
    COPPER = "CP"
    LEAD = "LD"
    CLOTH = "CL"
    SALT = "SA"
    BEACH_PORT = "BP"
    POTTERY = "PT"
    SECONDARY = [
        (EMPTY, "Empty"),
        (BENEDICTINE_ABBEY, "Benedictine Abbey"),
        (FARM, "Farm"),
        (ORCHARD, "Orchard"),
        (PASTURE, "Pasture"),
        (HUNTING, "Hunting"),
        (FISHING, "Fishing"),
        (WOOD, "Wood"),
        (GOLD, "Gold"),
        (TIN, "Tin"),
        (IRON, "Iron"),
        (SILVER, "Silver"),
        (COPPER, "Copper"),
        (LEAD, "Lead"),
        (CLOTH, "Cloth"),
        (SALT, "Salt"),
        (BEACH_PORT, "Beach Port"),
        (POTTERY, "Pottery"),
    ]

    secondary_building = models.CharField(max_length=2, choices=SECONDARY, default=EMPTY)

    def __str__(self):
        return f"{self.secondary_building}"


class Plan(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="province_plans"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    primary_building = models.OneToOneField(
        Primary,
        on_delete=models.CASCADE,
        related_name="primary_building_of"
    )
    secondary_building_1 = models.ForeignKey(
        Secondary,
        on_delete=models.CASCADE,
        related_name="secondary_building_1_of"
    )
    secondary_building_2 = models.ForeignKey(
        Secondary,
        on_delete=models.CASCADE,
        related_name="secondary_building_2_of"
    )
    secondary_building_3 = models.ForeignKey(
        Secondary,
        on_delete=models.CASCADE,
        related_name="secondary_building_3_of"
    )
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | created by {self.author}"