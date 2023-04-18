from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, Release, Environment, ReliabilityRun, ExecutionRecord, Run, Defect


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Release)
class ReleaseAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Defect)
class DefectAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('release', RelatedOnlyFieldListFilter),
    )
    search_fields = ['summary', 'description', 'external_id', ]


@admin.register(Run)
class RunAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('release', RelatedOnlyFieldListFilter),
        'build',
        'start_time',
        'end_time',
    )
    search_fields = ['name', 'build', ]


@admin.register(ExecutionRecord)
class ExecutionRecordAdmin(CustomModelAdmin):
    # readonly_fields = ('id', 'start_time', 'end_time',)
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'status',
        'acceptance_test',
        'automated',
        ('run', RelatedOnlyFieldListFilter),
        ('defects', RelatedOnlyFieldListFilter),
        'start_time',
        'end_time',
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(ReliabilityRun)
class ReliabilityRunAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'status',
        ('release', RelatedOnlyFieldListFilter),
        'build',
        'testName',
        'testEnvironmentType',
        'testEnvironmentName',
        'incidents',
        'start_time',
        'modified_time',
    )
    search_fields = ['name', 'build', 'testName', 'testEnvironmentName', 'targetIPTE', 'ipte', ]


@admin.register(Environment)
class EnvironmentAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('current_release', RelatedOnlyFieldListFilter),
        'type',
        'purpose',
    )
    search_fields = ['name', 'summary', 'description', 'purpose', 'type', ]
