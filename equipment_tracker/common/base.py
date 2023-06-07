from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    """Adds common fields within this App"""

    class Meta:
        abstract = True

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_created_by",
    )
