from django.db import models

# Create your models here.
class tranfusion(models.Model):
    employee_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    patient_id = models.IntegerField()
    patient_name = models.TextField(max_length=50)
    blood_product_type = models.TextField(max_length=20)
    blood_product_id = models.IntegerField()
    