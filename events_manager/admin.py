from django.contrib import admin
from .models import Sessions, Events


# Register your models here.

class sessions(admin.ModelAdmin):
    class Meta:
        model = Sessions, Events

admin.site.register(Sessions)
