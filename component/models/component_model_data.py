from django.db import models
import uuid
from datetime import datetime

from component.models.component_model import Component


class ComponentData(models.Model):
    """
    value represents the text from text components
    or keys from videos/images, used to access the
    in third_party storage providers
    """

    shared_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    value = models.CharField(null=False)
    component_id = models.ForeignKey(Component, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False, default=datetime.now)
    updated_at = models.DateTimeField(null=False, default=datetime.now)

    def __str__(self):
        return (
            f"id={self.shared_id} component_fk_type={self.component_id.component_type}"
        )

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.shared_id:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super(Component, self).save(*args, **kwargs)
