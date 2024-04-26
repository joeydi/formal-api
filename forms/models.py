from django.db import models
from django.conf import settings


class Form(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='created_by',
        blank=True,
        null=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='updated_by',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField()
    description = models.TextField(blank=True)
    schema = models.JSONField(blank=True, default=dict)
    uischema = models.JSONField(blank=True, default=dict)

    def __str__(self) -> str:
        return self.name
