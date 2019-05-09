from django.db import models

# Create your models here.
class Encuesta(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Persona(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    lastName = models.CharField(max_length=255, blank=True, null=True)
    ocupacion = models.CharField(max_length=255, blank=True, null=True)
    redSocialUno = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField(default=0)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.name