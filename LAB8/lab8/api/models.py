from django.db import models

class Product(models.Model):
    name = models.CharField(verbose_name='Name', max_length=300)
    price = models.FloatField(verbose_name='Price', default=0)
    description = models.TextField(verbose_name='Description')
    count = models.IntegerField(verbose_name='Count')
    is_active = models.BooleanField(verbose_name='Status', default=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active
        }

class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

