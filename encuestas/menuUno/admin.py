from django.contrib import admin

# Here you set the model in admin panel.

from .models import Encuesta

admin.site.register(Encuesta)
