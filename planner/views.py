from django.shortcuts import render
from django.views import generic
from .models import Plan
# Create your views here.


class PlanList(generic.ListView):
    queryset = Plan.objects.all()
    template_name = "planner/index.html"
    paginate_by = 6