from django.db import models

from api.models import OrgModel, OrgGroup
from api.storage import CustomFileSystemStorage


class Attachment(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='business_attachments')
    name = models.CharField(max_length=256)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='business', blank=False, null=False)


class Tag(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='business_tags')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class ResourceType(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='resource_types')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class ResourceSet(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='resource_sets')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='resource_set_attachments', blank=True)


class ResourceSetComponent(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='resource_set_components')
    resource_set = models.ForeignKey(ResourceSet, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='components')
    type = models.ForeignKey(ResourceType, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='resource_set_components')
    purpose = models.TextField(null=True, blank=True)
    count = models.IntegerField(default=1)


class Resource(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='resources')
    type = models.ForeignKey(ResourceType, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='resources')
    identifier = models.CharField(max_length=256, unique=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='resource_attachments', blank=True)
