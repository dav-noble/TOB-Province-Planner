from django.urls import path
from . import views


urlpatterns = [
    path('', views.PlanList.as_view(), name='home'),
    path('<slug:slug>/', views.plan_detail, name='plan_detail'),
    path('plan/new/', views.plan_form, name='plan_form'),
    path("plan/edit/<slug:slug>/", views.plan_form, name='plan_edit'),
    path("plan/delete/<slug:slug>/", views.plan_delete, name="plan_delete"),
]
