from django.db import models
    
class Carinventory(models.Model):
    cars_count= models.IntegerField()
    cars_value= models.FloatField()
    created_data= models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-created_data']

    def __str__(self):
        return f'Qtd carros = {self.cars_count} / Valores = {self.cars_value}'
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)  
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,related_name='cars_brand')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    plate = models.CharField(max_length=7)
    photo = models.ImageField(upload_to='cars/',blank=True,null=True)
    value = models.FloatField()
    biography = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.model


    