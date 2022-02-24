from django.db import models

# Create your models here.
class Employe(models.Model):
    eid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    mobile=models.CharField(max_length=15,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    city=models.CharField(max_length=50)
    salary=models.FloatField()
   
class Meta:
    dbtable="empdata"
   
   
   
   
   
