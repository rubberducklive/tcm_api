import uuid

from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True


class PrimaryUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta(object):
        abstract = True


class PrimaryUUIDTimeStampedModel(TimeStampedModel, PrimaryUUIDModel):
    class Meta(object):
        abstract = True
