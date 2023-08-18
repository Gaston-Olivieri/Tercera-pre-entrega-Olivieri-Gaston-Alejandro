from django.db import models

class Carta_Menú(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Carta Menú"
        verbose_name_plural = "Carta Menú"
        

    
    def __str__(self):
        return f"{self.nombre}"
    
class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Bebida"
        verbose_name_plural = "Bebidas"

    def __str__(self):
        return f"{self.nombre}"
    


class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    comensales = models.IntegerField()
    observacion = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"


    def __str__(self):
        return f"{self.apellido},{self.nombre}"

class Contacto(models.Model):
    sucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    telefono = models.IntegerField()
    gerente = models.CharField(max_length=50)
    delivery = models.IntegerField()

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"


    def __str__(self):
        return f"{self.sucursal}"

    

