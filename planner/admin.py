from django.contrib import admin
from .models import Plan
from .models import Primary
from .models import Secondary

# Register your models here.
admin.site.register(Plan)
admin.site.register(Primary)
admin.site.register(Secondary)