from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Plan
from .forms import PlanForm, PrimaryForm, SecondaryForm1, SecondaryForm2, SecondaryForm3
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

    return render(
        request,
        "planner/plan_detail.html",
        {"plan": plan},
    )


def plan_form(request):
    if request.method == "POST":
        plan_form = PlanForm(data=request.POST)
        primary_form = PrimaryForm(data=request.POST)
        secondary_form_1 = SecondaryForm1(data=request.POST, prefix="sec1")
        secondary_form_2 = SecondaryForm2(data=request.POST, prefix="sec2")
        secondary_form_3 = SecondaryForm3(data=request.POST, prefix="sec3")

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
            
            plan.save()
            
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
        plan_form = PlanForm()
        primary_form = PrimaryForm()
        secondary_form_1 = SecondaryForm1(prefix="sec1")
        secondary_form_2 = SecondaryForm2(prefix="sec2")
        secondary_form_3 = SecondaryForm3(prefix="sec3")

    return render(
        request,
        "planner/plan_form.html",
        {
            "plan_form": plan_form,
            "primary_form": primary_form,
            "secondary_form_1": secondary_form_1,
            "secondary_form_2": secondary_form_2,
            "secondary_form_3": secondary_form_3,
        }
    )