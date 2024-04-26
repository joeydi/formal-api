from django.db import models


class Form(models.Model):
    name = models.CharField()
    description = models.TextField()
    schema = models.JSONField()
    uischema = models.JSONField()
