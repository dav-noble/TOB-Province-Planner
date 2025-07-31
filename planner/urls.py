from . import views
from django.urls import path


urlpatterns = [
    path('', views.PlanList.as_view(), name='home'),
    path('<slug:slug>/', views.plan_detail, name='plan_detail'),
    path('plan/new/', views.plan_form, name='plan_form'),
    path("plan/edit/<slug:slug>/", views.plan_form, name='plan_edit'),
]