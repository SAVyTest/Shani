from django.db import models

import business.models
from api.models import OrgModel, OrgGroup, ReviewStatus
from api.storage import CustomFileSystemStorage


class Attachment(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='requirement_attachments')
    name = models.CharField(max_length=256)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='requirements', blank=False, null=False)


class Tag(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='requirement_tags')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class FeatureCategory(OrgModel):
    class Meta:
        verbose_name_plural = "feature categories"

    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='feature_categories')
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='sub_categories')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    tags = models.ManyToManyField(Tag, related_name='feature_categories', blank=True)
    details_file = models.FileField(storage=CustomFileSystemStorage, upload_to='requirements', blank=True, null=True,
                                    verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='feature_category_attachments', blank=True)


class Feature(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='requirement_features')
    parent = models.ForeignKey(FeatureCategory, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='features', verbose_name='feature category')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=11, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)

    tags = models.ManyToManyField(Tag, related_name='features', blank=True)
    external_id = models.CharField(max_length=256, blank=True, null=True)

    details_file = models.FileField(storage=CustomFileSystemStorage, upload_to='requirements', blank=True, null=True,
                                    verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='feature_attachments', blank=True)


class UseCase(OrgModel):
    feature = models.ForeignKey(Feature, on_delete=models.SET_NULL, null=True, blank=True, related_name="use_cases")

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=11, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)

    details_file = models.FileField(storage=CustomFileSystemStorage, upload_to='requirements', blank=True, null=True,
                                    verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='use_case_attachments', blank=True)


class RequirementCategory(OrgModel):
    class Meta:
        verbose_name_plural = "requirement categories"

    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='requirement_categories')
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='sub_categories')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    tags = models.ManyToManyField(Tag, related_name='sub_categories', blank=True)
    details_file = models.FileField(storage=CustomFileSystemStorage, upload_to='requirements', blank=True, null=True,
                                    verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='requirement_category_attachments', blank=True)


class Requirement(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='requirements')
    category = models.ForeignKey(RequirementCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='requirements', verbose_name='category')
    name = models.CharField(max_length=256, unique=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='parent_requirement')

    summary = models.CharField(max_length=256, null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=11, choices=ReviewStatus.choices, default=ReviewStatus.DRAFT)

    tags = models.ManyToManyField(Tag, related_name='requirements', blank=True)
    external_id = models.CharField(max_length=256, blank=True, null=True)

    details_file = models.FileField(storage=CustomFileSystemStorage, upload_to='requirements', blank=True, null=True,
                                    verbose_name='File with details')
    attachments = models.ManyToManyField(Attachment, related_name='requirement_attachments', blank=True)

    cost = models.FloatField(default=0)

    business_requirements = models.ManyToManyField(business.models.Requirement, related_name='technical_requirements',
                                                   blank=True)

    additional_data = models.JSONField(null=True, blank=True)

# TODO: Add user segment with use-case variations
