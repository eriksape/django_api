from django.db import models


class Scraper(models.Model):
    """
    Structure for Scrapper model
    """
    currency = models.CharField(max_length=50, unique=True)
    frequency = models.IntegerField()
    value = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    value_updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.currency
