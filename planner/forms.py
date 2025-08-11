from django import forms
from .models import Plan, Primary, Secondary, Tertiary


class PlanForm(forms.ModelForm):
    """
    Form class for users to create a new plan 
    """
    class Meta:
        model = Plan
        fields = (
            'title',
        )


class PrimaryForm(forms.ModelForm):
    """
    Form class for users to create a new primary building for new plan 
    """
    class Meta:
        model = Primary
        fields = (
            'primary_building',
        )


class SecondaryForm1(forms.ModelForm):
    """
    Form class for users to create a new secondary building for new plan 
    """
    class Meta:
        model = Secondary
        fields = (
            'secondary_building',
        )


class SecondaryForm2(forms.ModelForm):
    """
    Form class for users to create a new secondary building for new plan 
    """
    class Meta:
        model = Secondary
        fields = (
            'secondary_building',
        )


class SecondaryForm3(forms.ModelForm):
    """
    Form class for users to create a new secondary building for new plan 
    """
    class Meta:
        model = Secondary
        fields = (
            'secondary_building',
        )


class TertiaryForm1(forms.ModelForm):
    """
    Form class for users to create a new tertiary building for new plan 
    """
    class Meta:
        model = Tertiary
        fields = (
            'tertiary_building',
        )


class TertiaryForm2(forms.ModelForm):
    """
    Form class for users to create a new tertiary building for new plan 
    """
    class Meta:
        model = Tertiary
        fields = (
            'tertiary_building',
        )


class TertiaryForm3(forms.ModelForm):
    """
    Form class for users to create a new tertiary building for new plan 
    """
    class Meta:
        model = Tertiary
        fields = (
            'tertiary_building',
        )


class TertiaryForm4(forms.ModelForm):
    """
    Form class for users to create a new tertiary building for new plan 
    """
    class Meta:
        model = Tertiary
        fields = (
            'tertiary_building',
        )


class TertiaryForm5(forms.ModelForm):
    """
    Form class for users to create a new tertiary building for new plan 
    """
    class Meta:
        model = Tertiary
        fields = (
            'tertiary_building',
        )
