from django.shortcuts import render
from django.views import generic
from .models import Plan
# Create your views here.


class PlanList(generic.ListView):
    queryset = Plan.objects.all()
    template_name = "plan_list.html"