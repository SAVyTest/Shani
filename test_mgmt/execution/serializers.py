from rest_framework import serializers

from .models import Attachment, Tag, Release, Environment, ReliabilityRun, ExecutionRecord, Run, Defect, Build


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published', ]


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published', ]


class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ['id', 'release', 'name', 'build_time', 'summary', 'description', 'properties', 'attachments',
                  'org_group', 'created_at', 'updated_at', 'published', ]


class DefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defect
        fields = ['id', 'summary', 'description', 'external_id', 'release', 'build', 'details_file', 'attachments',
                  'org_group', 'created_at', 'updated_at', 'published', ]


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ['id', 'build', 'name', 'start_time', 'end_time', 'release', 'org_group', 'created_at', 'updated_at',
                  'published', ]


class ExecutionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutionRecord
        fields = ['id', 'name', 'summary', 'description', 'status', 'defects', 'run', 'start_time', 'end_time',
                  'org_group', 'created_at', 'updated_at', 'published', ]


class ReliabilityRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliabilityRun
        fields = ['id', 'build', 'name', 'start_time', 'modified_time', 'testName', 'testEnvironmentType',
                  'testEnvironmentName', 'status', 'totalIterationCount', 'passedIterationCount', 'incidentCount',
                  'targetIPTE', 'ipte', 'incidents', 'release', 'org_group', 'created_at', 'updated_at', 'published', ]


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ['id', 'name', 'summary', 'type', 'description', 'purpose', 'details_file', 'attachments',
                  'current_release', 'current_build', 'properties', 'org_group', 'created_at', 'updated_at',
                  'published', ]
