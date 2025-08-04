from django.contrib import admin
from .models import Plan, Primary, Secondary, Tertiary
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Plan)
class PlanAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Primary)
admin.site.register(Secondary)
admin.site.register(Tertiary)