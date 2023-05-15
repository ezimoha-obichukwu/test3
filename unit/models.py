from django.db import models

class PollingUnit(models.Model):
    name = models.CharField(max_length=50)


class PollingUnitResult(models.Model):
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE)
    party = models.CharField(max_length=100)
    result = models.IntegerField()
