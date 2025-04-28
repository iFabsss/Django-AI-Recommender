from django_mongoengine import Document, fields

from django.conf import settings

class Products(Document):
    name = fields.StringField(max_length=100, blank=False)
    description = fields.StringField(blank=False)
    price = fields.FloatField(blank=False)
    category = fields.StringField(max_length=50, blank=False)

    def __str__(self):
        return self.name
