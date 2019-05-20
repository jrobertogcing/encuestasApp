from django.contrib import admin

# Here you set the model in admin panel.

from .models import Persona, Nota

class NotaInLine(admin.TabularInline):
    model = Nota

class PersonaAdmin(admin.ModelAdmin):
    inlines = [NotaInLine, ]

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Nota)

 