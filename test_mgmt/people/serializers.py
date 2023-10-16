from rest_framework import serializers

from .models import Engineer, SiteHoliday, Leave, EngineerOrgGroupParticipation, Topic, \
    TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Site, Attachment, Credit, Scale, Reason


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', ]


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', 'attachments', ]


class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = ['id', 'employee_id', 'name', 'auth_user', 'role', 'org_group', 'created_at', 'updated_at',
                  'published', 'site', 'attachments', ]


class EngineerOrgGroupParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineerOrgGroupParticipation
        fields = ['id', 'engineer', 'org_group', 'created_at', 'updated_at', 'published', 'role', 'capacity', ]


class SiteHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteHoliday
        fields = ['id', 'name', 'date', 'summary', 'attachments', 'site', 'created_at', 'updated_at', 'published', ]


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['id', 'engineer', 'start_date', 'end_date', 'summary', 'attachments', 'status', 'created_at',
                  'updated_at', 'published', ]


class EngineerOrgGroupParticipationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineerOrgGroupParticipationHistory
        fields = ['id', 'date', 'engineer', 'org_group', 'created_at', 'updated_at', 'published', 'expected_capacity',
                  'capacity', ]


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'summary', 'description', 'parent_topic', 'org_group', 'created_at', 'updated_at',
                  'published', ]


class TopicEngineerAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicEngineerAssignment
        fields = ['id', 'topic', 'engineer', 'status', 'rating', 'start_date', 'end_date', 'org_group', 'created_at',
                  'updated_at', 'published', ]


class ScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scale
        fields = ['id', 'name', 'summary', 'description', ]


class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = ['id', 'name', 'summary', 'description', 'weight', ]


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = ['id', 'time', 'credited_user', 'credits', 'scale', 'reason', 'description', 'creditor', 'org_group',
                  'created_at', 'updated_at', 'published', ]
