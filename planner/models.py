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
        return f"{self.get_primary_building_display()}"


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
        return f"{self.get_secondary_building_display()}"


class Tertiary(models.Model):
    EMPTY = "EM"
    ALEHOUSE = "AH"
    ARENA = "AR"
    ARTISANS = "AT"
    BULLAUN = "BL"
    CHURCH_CRAFTS = "CC"
    CHURCH = "CH"
    CRAFT_MERCHANT = "CM"
    ESTATE = "ES"
    FORGE = "FG"
    GARRISON = "GA"
    GRANARY = "GR"
    HERRING_PORT = "HP"
    LIBRARY = "LB"
    MARKET_FAIR = "MF"
    MERCHANT = "MR"
    MILL = "MI"
    MINT = "MT"
    MOOT_HILL = "MH"
    PORT = "PT"
    ROUND_TOWER = "RT"
    SCRIBES = "SC"
    TANNER = "TA"
    TITHE_HALL = "TH"
    TOOLS = "TL"
    TRADE_PORT = "TP"
    VIKING_PORT = "VP"
    WAREHOUSE = "WH"
    WORKSHOP = "WK"
    TERTIARY = [
        (EMPTY, "Empty"),
        (ALEHOUSE, "Alehouse"),
        (ARENA, "Arena"),
        (ARTISANS, "Artisans"),
        (BULLAUN, "Bullaun"),
        (CHURCH_CRAFTS, "Church Crafts"),
        (CHURCH, "Church"),
        (CRAFT_MERCHANT, "Craft Merchant"),
        (ESTATE, "Estate"),
        (FORGE, "Forge"),
        (GARRISON, "Garrison"),
        (GRANARY, "Granary"),
        (HERRING_PORT, "Herring Port"),
        (LIBRARY, "Library"),
        (MARKET_FAIR, "Market Fair"),
        (MERCHANT, "Merchant"),
        (MILL, "Mill"),
        (MINT, "Mint"),
        (MOOT_HILL, "Moot Hill"),
        (PORT, "Port"),
        (ROUND_TOWER, "Round Tower"),
        (SCRIBES, "Scribes"),
        (TANNER, "Tanner"),
        (TITHE_HALL, "Tithe Hall"),
        (TOOLS, "Tools"),
        (TRADE_PORT, "Trade Port"),
        (VIKING_PORT, "Viking Port"),
        (WAREHOUSE, "Warehouse"),
        (WORKSHOP, "Workshop"),
    ]

    tertiary_building = models.CharField(max_length=2, choices=TERTIARY, default=EMPTY)

    def __str__(self):
        return f"{self.get_tertiary_building_display()}"

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
    tertiary_building_1 = models.ForeignKey(
        Tertiary,
        on_delete=models.CASCADE,
        related_name="tertiary_building_1_of"
    )
    tertiary_building_2 = models.ForeignKey(
        Tertiary,
        on_delete=models.CASCADE,
        related_name="tertiary_building_2_of"
    )
    tertiary_building_3 = models.ForeignKey(
        Tertiary,
        on_delete=models.CASCADE,
        related_name="tertiary_building_3_of"
    )
    tertiary_building_4 = models.ForeignKey(
        Tertiary,
        on_delete=models.CASCADE,
        related_name="tertiary_building_4_of"
    )
    tertiary_building_5 = models.ForeignKey(
        Tertiary,
        on_delete=models.CASCADE,
        related_name="tertiary_building_5_of"
    )
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | created by {self.author}"