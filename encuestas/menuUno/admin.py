from django.contrib import admin

# Here you set the model in admin panel.

from .models import Encuesta, Persona

class PersonInLine(admin.TabularInline):
    model = Persona

class PersonaAdmin(admin.ModelAdmin):
    inlines = [PersonInLine, ]

admin.site.register(Encuesta, PersonaAdmin)
 