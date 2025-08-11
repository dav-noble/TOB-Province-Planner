from django.apps import AppConfig


class PlannerConfig(AppConfig):
    """
    Provides primary key type for planner app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'planner'
