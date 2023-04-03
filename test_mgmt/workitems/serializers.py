from rest_framework import serializers

from .models import Attachment, Tag, Release, Story, Sprint, Feature, Epic, Feedback


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'published', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'published', ]


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'published', ]


class EpicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epic
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'release', 'org_group',
                  'published', ]


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'epic', 'org_group', 'published', ]


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['id', 'number', 'release', 'start_date', 'end_date', 'org_group', 'published', ]


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'rank', 'sprint', 'feature',
                  'org_group', 'published', ]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'summary', 'description', 'time', 'release', 'org_group', 'published', ]
