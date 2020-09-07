from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.timezone import utc


class CustomDateTimeField(models.DateTimeField):

    def value_to_string(self, obj):
        datetime = getattr(obj, self.name, True).utcnow().replace(tzinfo=utc)
        return str(datetime)

    def value_from_object(self, obj):
        return obj

class Scraper(models.Model):
    """
    Structure for Scrapper model
    """
    currency = models.CharField(max_length=50, unique=True)
    frequency = models.IntegerField()
    value = models.FloatField(default=0)
    created_at = CustomDateTimeField(auto_now_add=True)
    value_updated_at = CustomDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.currency


@receiver(pre_save, sender=Scraper)
def post_update_scraper(**kwargs):
    instance = kwargs['instance']
    if instance.id:
        old_instance = Scraper.objects.get(id=kwargs['instance'].id)
        if old_instance.value != instance.value:
            instance.value_updated_at = timezone.now()
