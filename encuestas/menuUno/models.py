from django.db import models

# Create your models here.
# class Nota(models.Model):
#     auto_id_nota = models.AutoField(primary_key=True)  
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.auto_id_nota

class Persona(models.Model):
    auto_id_cliente = models.AutoField(primary_key=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    info = models.CharField(max_length=255)

    class Meta:
        ordering = ['auto_id_cliente', ]

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    auto_id_nota = models.AutoField(primary_key=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=255)
    person = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.auto_id_nota)


# Create your models here.
# class Notas(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     auto_id_nota = models.AutoField(primary_key=True)  

#     def __str__(self):
#         return self.nombre