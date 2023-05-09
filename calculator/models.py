from django.db import models


class Altitude(models.Model):
    value = models.DecimalField(max_digits=8, decimal_places=2)


class AtmosphericVariables(models.Model):
    altitude = models.ForeignKey(Altitude, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=8, decimal_places=2)
    pressure = models.DecimalField(max_digits=8, decimal_places=2)
    density = models.DecimalField(max_digits=8, decimal_places=2)
