from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from .models import Plan
from .forms import (
    PlanForm,
    PrimaryForm,
    SecondaryForm1,
    SecondaryForm2,
    SecondaryForm3,
    TertiaryForm1,
    TertiaryForm2,
    TertiaryForm3,
    TertiaryForm4,
    TertiaryForm5,
)
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.


class PlanList(generic.ListView):
    template_name = "planner/index.html"
    paginate_by = 6

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Plan.objects.filter(author=self.request.user)
        else:
            return Plan.objects.none()


def plan_detail(request, slug):
    """
    Display an individual :model:`planner.Plan`.

    **Context**

    ``plan``
        An instance of :model:`planner.Plan`.

    **Template:**

    :template:`planner/plan_detail.html`
    """

    queryset = Plan.objects.all()
    plan = get_object_or_404(queryset, slug=slug)

    is_author = request.user == plan.author

    return render(
        request,
        "planner/plan_detail.html",
        {"plan": plan, "is_author": is_author},
    )


def plan_form(request, slug=None):
    if slug:
        plan = get_object_or_404(Plan, slug=slug)
        # Check if the user is the author
        if request.user != plan.author:
            messages.error(request, "You do not have permission to edit this plan.")
            return redirect("plan_detail", slug=plan.slug)
        primary_instance = plan.primary_building
        secondary_instance_1 = plan.secondary_building_1
        secondary_instance_2 = plan.secondary_building_2
        secondary_instance_3 = plan.secondary_building_3
        tertiary_instance_1 = plan.tertiary_building_1
        tertiary_instance_2 = plan.tertiary_building_2
        tertiary_instance_3 = plan.tertiary_building_3
        tertiary_instance_4 = plan.tertiary_building_4
        tertiary_instance_5 = plan.tertiary_building_5
    else:
        plan = None
        primary_instance = None
        secondary_instance_1 = None
        secondary_instance_2 = None
        secondary_instance_3 = None
        tertiary_instance_1 = None
        tertiary_instance_2 = None
        tertiary_instance_3 = None
        tertiary_instance_4 = None
        tertiary_instance_5 = None

    if request.method == "POST":
        plan_form = PlanForm(data=request.POST, instance=plan)
        primary_form = PrimaryForm(data=request.POST, instance=primary_instance)
        secondary_form_1 = SecondaryForm1(data=request.POST, prefix="sec1", instance=secondary_instance_1)
        secondary_form_2 = SecondaryForm2(data=request.POST, prefix="sec2", instance=secondary_instance_2)
        secondary_form_3 = SecondaryForm3(data=request.POST, prefix="sec3", instance=secondary_instance_3)
        tertiary_form_1 = TertiaryForm1(data=request.POST, prefix="ter1", instance=tertiary_instance_1)
        tertiary_form_2 = TertiaryForm2(data=request.POST, prefix="ter2", instance=tertiary_instance_2)
        tertiary_form_3 = TertiaryForm3(data=request.POST, prefix="ter3", instance=tertiary_instance_3)
        tertiary_form_4 = TertiaryForm4(data=request.POST, prefix="ter4", instance=tertiary_instance_4)
        tertiary_form_5 = TertiaryForm5(data=request.POST, prefix="ter5", instance=tertiary_instance_5)

        if plan_form.is_valid():
            plan = plan_form.save(commit=False)
            plan.author = request.user
            title = plan.title
            title_words = title.split()
            slug = "-".join(title_words)
            plan.slug = slug

            if primary_form.is_valid():
                plan.primary_building = primary_form.save()
            
            if secondary_form_1.is_valid():
                plan.secondary_building_1 = secondary_form_1.save()
            
            if secondary_form_2.is_valid():
                plan.secondary_building_2 = secondary_form_2.save()
            
            if secondary_form_3.is_valid():
                plan.secondary_building_3 = secondary_form_3.save()

            if tertiary_form_1.is_valid():
                plan.tertiary_building_1 = tertiary_form_1.save()

            if tertiary_form_2.is_valid():
                plan.tertiary_building_2 = tertiary_form_2.save()

            if tertiary_form_3.is_valid():
                plan.tertiary_building_3 = tertiary_form_3.save()

            if tertiary_form_4.is_valid():
                plan.tertiary_building_4 = tertiary_form_4.save()

            if tertiary_form_5.is_valid():
                plan.tertiary_building_5 = tertiary_form_5.save()
            
            is_edit = plan.pk is not None  # True if editing, False if creating

            plan.save()

            if is_edit:
                messages.add_message(
                    request, messages.SUCCESS,
                    'Plan updated successfully'
                )
            else:
                messages.add_message(
                    request, messages.SUCCESS,
                    'Plan submitted successfully'
                )

            return HttpResponseRedirect(reverse('plan_detail', args=[slug]))
        else:
            messages.add_message(
                request, messages.SUCCESS,
                'Invalid Plan'
            )
    else:
        plan_form = PlanForm(instance=plan)
        primary_form = PrimaryForm(instance=primary_instance)
        secondary_form_1 = SecondaryForm1(prefix="sec1", instance=secondary_instance_1)
        secondary_form_2 = SecondaryForm2(prefix="sec2", instance=secondary_instance_2)
        secondary_form_3 = SecondaryForm3(prefix="sec3", instance=secondary_instance_3)
        tertiary_form_1 = TertiaryForm1(prefix="ter1", instance=tertiary_instance_1)
        tertiary_form_2 = TertiaryForm2(prefix="ter2", instance=tertiary_instance_2)
        tertiary_form_3 = TertiaryForm3(prefix="ter3", instance=tertiary_instance_3)
        tertiary_form_4 = TertiaryForm4(prefix="ter4", instance=tertiary_instance_4)
        tertiary_form_5 = TertiaryForm5(prefix="ter5", instance=tertiary_instance_5)

    return render(
        request,
        "planner/plan_form.html",
        {
            "plan_form": plan_form,
            "primary_form": primary_form,
            "secondary_form_1": secondary_form_1,
            "secondary_form_2": secondary_form_2,
            "secondary_form_3": secondary_form_3,
            "tertiary_form_1": tertiary_form_1,
            "tertiary_form_2": tertiary_form_2,
            "tertiary_form_3": tertiary_form_3,
            "tertiary_form_4": tertiary_form_4,
            "tertiary_form_5": tertiary_form_5,
        }
    )


def plan_delete(request, slug):
    plan = get_object_or_404(Plan, slug=slug)
    if request.method == "POST":
        plan.delete()
        messages.success(request, "Plan deleted successfully.")
        return redirect("home")