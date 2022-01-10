from django.db import models
from django.urls import reverse

"""
Categories:
- Produce
- Tobacco
- Vehicle
"""


CATEGORY = [
    ('Other', 'Other'),
    ('Produce', 'Produce'),
    ('Tobacco', 'Tobacco'),
    ('Vehicle', 'Vehicle'),
]


# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    upc = models.IntegerField()
    name = models.CharField(max_length=30)
    count = models.IntegerField()
    category = models.CharField(max_length=60, choices=CATEGORY)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # Vendor foreign key here
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.upc} | {self.name}'

    def get_absolute_url(self):
        return reverse('cim_item', args=(str(self.id)))


"""

"""


class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    category = models.CharField(max_length=60, choices=CATEGORY, default=0)
    contact = models.IntegerField()

    def __str__(self):
        return f'{self.number} | {self.name}'

    def get_absolute_url(self):
        return reverse('cim_viewVendor', args=(str(self.id)))

