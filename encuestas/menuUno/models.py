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
        return self.nombre + ' ' + self.apellido + ' (' + self.info + ')'

class Nota(models.Model):
    auto_id_nota = models.AutoField(primary_key=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=255)
    receptor = models.CharField(max_length=255)
    cliente = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.auto_id_nota)

class Item(models.Model):
    auto_id_item = models.AutoField(primary_key=True)     
    descripción = models.CharField(max_length=255)
    serie = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    cargador = models.CharField(max_length=255)
    funda = models.CharField(max_length=255)
    cables = models.CharField(max_length=255)
    cartuchos = models.CharField(max_length=255)
    falla = models.CharField(max_length=255)
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.auto_id_item)


# Create your models here.
# class Notas(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     auto_id_nota = models.AutoField(primary_key=True)  

#     def __str__(self):
#         return self.nombre