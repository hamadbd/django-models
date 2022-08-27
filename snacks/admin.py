from django.contrib import admin

from .models import Snack


class SnackAdmin(admin.ModelAdmin):
    list_display = ['name', 'purchaser']


# Register the models in the admin panel
admin.site.register(Snack, SnackAdmin)
