from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    readonly_fields = [
        "created_by",
        "created_at",
        "updated_by",
        "updated_at",
        "schema",
        "uischema",
    ]

    fields = [
        "created_by",
        "created_at",
        "updated_by",
        "updated_at",
        "name",
        "description",
        "schema",
        "uischema",
    ]

    def save_model(self, request, obj, form, change,):
        if not obj.created_by:
            obj.created_by = request.user

        obj.updated_by = request.user

        super().save_model(request, obj, form, change)


admin.site.register(Form, FormAdmin)
