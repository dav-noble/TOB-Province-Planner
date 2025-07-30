from .models import Plan
from django import forms


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = (
            'title',
            'primary_building',
            'secondary_building_1',
            'secondary_building_2',
            'secondary_building_3',
        )