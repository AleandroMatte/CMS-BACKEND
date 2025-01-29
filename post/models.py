import uuid
from django.db import models
from datetime import datetime

from post.post_exceptions.post_exceptions import DuplicatedPostNameException


class Post(models.Model):
    shared_id = models.UUIDField(
        unique=True, primary_key=True, null=False, default=uuid.uuid4
    )
    post_name = models.CharField(max_length=255, null=False, unique=True)
    created_at = models.DateTimeField(null=False, default=datetime.now)
    updated_at = models.DateTimeField(null=False, default=datetime.now)

    def __str__(self):
        return f"id={self.shared_id}  post_name={self.post_name} created_at={self.created_at}"

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.shared_id:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super(Post, self).save(*args, **kwargs)
