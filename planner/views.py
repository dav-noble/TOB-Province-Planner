from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Plan
from .forms import PlanForm
from django.contrib import messages


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

    plan_form = PlanForm()

    if request.method == "POST":
        plan_form = PlanForm(data=request.POST)
        if plan_form.is_valid():
            plan = plan_form.save(commit=False)
            plan.author = request.user
            
            title = plan.title
            title_words = title.split()
            slug = "-".join(title_words)
            plan.slug = slug

            plan.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
        else:
            messages.add_message(
                request, messages.SUCCESS,
                'Invalid'
            )

    plan_form = PlanForm()

    return render(
        request,
        "planner/plan_form.html",
        {
            "plan_form": plan_form,
        }
    )