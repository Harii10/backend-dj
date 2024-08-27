from django.db import models

class Materials(models.Model):
    Name = models.CharField(max_length=30)
    Cost_per_Unit = models.DecimalField(max_digits=10, decimal_places=2)
    Durability = models.DecimalField(max_digits=10, decimal_places=2)
    Strength = models.DecimalField(max_digits=10, decimal_places=2)
    Resistance = models.DecimalField(max_digits=10, decimal_places=2)
    Performance = models.DecimalField(max_digits=10, decimal_places=2)
    Pressure = models.DecimalField(max_digits=10, decimal_places=2)
    Construction_Cost_Over_Time_Years = models.DecimalField(max_digits=10, decimal_places=2)
    Area_Measurements = models.DecimalField(max_digits=10, decimal_places=2)
    Risk_Score = models.DecimalField(max_digits=10, decimal_places=2)
    Material_Score = models.DecimalField(max_digits=10, decimal_places=2)

class Bmaterials(models.Model):
    Name = models.CharField(max_length=30)
    Cost_per_Unit = models.DecimalField(max_digits=10, decimal_places=2)
    Durability = models.DecimalField(max_digits=10, decimal_places=2)
    Strength = models.DecimalField(max_digits=10, decimal_places=2)
    Resistance = models.DecimalField(max_digits=10, decimal_places=2)
    Performance = models.DecimalField(max_digits=10, decimal_places=2)
    Pressure = models.DecimalField(max_digits=10, decimal_places=2)
    Construction_Cost_Over_Time_Years = models.DecimalField(max_digits=10, decimal_places=2)
    Area_Measurements = models.DecimalField(max_digits=10, decimal_places=2)
    Risk_Score = models.DecimalField(max_digits=10, decimal_places=2)
    Material_Score = models.DecimalField(max_digits=10, decimal_places=2)

class nested(models.Model):
    Name = models.CharField(max_length=30)
    Cost_per_Unit = models.DecimalField(max_digits=10, decimal_places=2)
    Durability = models.DecimalField(max_digits=10, decimal_places=2)
    Strength = models.DecimalField(max_digits=10, decimal_places=2)
    Resistance = models.DecimalField(max_digits=10, decimal_places=2)
    Performance = models.DecimalField(max_digits=10, decimal_places=2)
    Pressure = models.DecimalField(max_digits=10, decimal_places=2)
    Construction_Cost_Over_Time_Years = models.DecimalField(max_digits=10, decimal_places=2)
    Area_Measurements = models.DecimalField(max_digits=10, decimal_places=2)
    Risk_Score = models.DecimalField(max_digits=10, decimal_places=2)
    Material_Score = models.DecimalField(max_digits=10, decimal_places=2)
    
