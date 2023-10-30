from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from cars.models import Car, Carinventory
from django.db.models import Sum
from openai_api.client import auto_biography



def car_inventoryupdate():
        cars_count = Car.objects.all().count()
        cars_value = Car.objects.aggregate(total_value = Sum('value'))['total_value']
        Carinventory.objects.create(cars_count = cars_count, cars_value = cars_value)
        
@receiver(post_save, sender = Car)
def carpostsave(sender, instance, **kwargs):
        car_inventoryupdate()
        
@receiver(post_delete, sender = Car)
def carpostdelete(sender, instance, **kwargs):
        car_inventoryupdate()
        
@receiver(pre_save, sender = Car)
def carpresave(sender, instance, **kwargs):
        if not instance.biography:
                
                instance.biography = 'Biografia não descrita.' 
                
                '''chatgpt se estiver com cota em dia'''
                
                '''
                ai_bio = auto_biography(
                        instance.model,instance.brand,instance.model_year )
                instance.biography = ai_bio '''