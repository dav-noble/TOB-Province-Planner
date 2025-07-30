from .models import Plan, Primary, Secondary
from django import forms


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = (
            'title',
        )


class PrimaryForm(forms.ModelForm):
    class Meta:
        model = Primary
        fields = (
            'primary_building',
        )


class SecondaryForm1(forms.ModelForm):
    class Meta:
        model = Secondary
        fields = (
            'secondary_building',
        )


class SecondaryForm2(forms.ModelForm):
    class Meta:
        model = Secondary
        fields = (
            'secondary_building',
        )


class SecondaryForm3(forms.ModelForm):
    class Meta:
        model = Secondary
        fields = (
            'secondary_building',
        )