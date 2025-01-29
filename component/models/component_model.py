from django.db import models
import uuid
from datetime import datetime
from post.models import Post


class Component(models.Model):
    class ComponentTypes(models.TextChoices):
        TEXT = ("TEXT",)
        IMAGE = ("IMAGE",)
        TITLE = ("TITLE",)
        SUBTITLE = ("SUBTITLE",)
        SNIPPET = ("SNIPPET",)
        VIDEO = ("VIDEO",)

    shared_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    component_type = models.CharField(
        max_length=20, choices=ComponentTypes.choices, null=False
    )
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(null=False, default=datetime.now)
    updated_at = models.DateTimeField(null=False, default=datetime.now)

    def __str__(self):
        return f"id={self.shared_id} component_type={self.component_type} post={self.post_id.post_name}"

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.shared_id:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super(Component, self).save(*args, **kwargs)
