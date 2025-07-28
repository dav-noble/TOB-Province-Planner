from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Plan
# Create your views here.


class PlanList(generic.ListView):
    queryset = Plan.objects.all()
    template_name = "planner/index.html"
    paginate_by = 6


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