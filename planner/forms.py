from django import forms
from .models import Plan, Primary, Secondary, Tertiary


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


class TertiaryForm1(forms.ModelForm):
    class Meta:
        model = Tertiary
        fields = (
            'tertiary_building',
        )


class TertiaryForm2(forms.ModelForm):
    class Meta:
        model = Tertiary
        fields = (
            'tertiary_building',
        )


class TertiaryForm3(forms.ModelForm):
    class Meta:
        model = Tertiary
        fields = (
            'tertiary_building',
        )


class TertiaryForm4(forms.ModelForm):
    class Meta:
        model = Tertiary
        fields = (
            'tertiary_building',
        )


class TertiaryForm5(forms.ModelForm):
    class Meta:
        model = Tertiary
        fields = (
            'tertiary_building',
        )