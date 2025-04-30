from django_mongoengine import Document, fields

class Products(Document):
    name = fields.StringField(max_length=100, blank=False)
    description = fields.StringField(blank=False)
    price = fields.FloatField(blank=False)
    category = fields.StringField(max_length=50, blank=False)
    tags = fields.ListField(fields.StringField(), blank=True, default=list, )  # List of tags

    def __str__(self):
        return self.name
