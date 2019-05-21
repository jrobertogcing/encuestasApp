from django.contrib import admin

# Here you set the model in admin panel.

from .models import Persona, Nota, Item

class NotaInLine(admin.TabularInline):
    model = Nota

class ItemInLine(admin.TabularInline):
    model = Item

class PersonaAdmin(admin.ModelAdmin):
    inlines = [NotaInLine, ]

class NotaAdmin(admin.ModelAdmin):
    inlines = [ItemInLine, ]

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Nota, NotaAdmin )

 