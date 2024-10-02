from rest_framework import serializers
from .models import Announcement, WorkRequest
from datetime import timedelta
from users.models import *

class AnnouncementSerializer(serializers.ModelSerializer):
    formatted_datetime = serializers.SerializerMethodField()
    assigned_to_team = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = [
            'id',
            'url',
            'tashkilot_nomi',
            'phone',
            'name_of_employer',
            'project_name',
            'deadline',
            'cost',
            'description',
            'assigned_to_team',
            'assigned_to',
            'file1',
            'file2',
            'file3',
            'formatted_datetime',
            'updated_at',
            'deleted_at',
            'remove_file1',
            'remove_file2',
            'remove_file3',
        ]
        extra_kwargs = {
            'file1': {'required': False},
            'file2': {'required': False},
            'file3': {'required': False},
        }
        read_only_fields = [
            "id",
            'assigned_to',
            'formatted_datetime',
            'updated_at',
            'deleted_at',
        ]

    def get_formatted_datetime(self, obj):
        adjusted_datetime = obj.created_at + timedelta(hours=5)
        return adjusted_datetime.strftime('%d-%m-%Y %H:%M')

    def get_assigned_to_team(self, obj):
        user = obj.assigned_to
        if user:
            team = Team.objects.filter(user=user).first()
            if team:
                return team.title
        return None
    




class WorkRequestSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()    
    announcement = AnnouncementSerializer()
    
    class Meta:
        model = WorkRequest
        fields = [
            'id',
            'url',
            'announcement',
            'requester',
            'deadline',
            'cost',
            'description',
            'status',
            'created_at',
            'updated_at',
            'deleted_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
            'deleted_at',
        ]
    def get_created_at(self, obj):
        adjusted_datetime = obj.created_at + timedelta(hours=5)
        return adjusted_datetime.strftime('%d-%m-%Y %H:%M')


class WorkRequestSerializerWithOutAnn(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()    
    
    class Meta:
        model = WorkRequest
        fields = [
            'id',
            'url',
            'announcement',
            'requester',
            'deadline',
            'cost',
            'description',
            'status',
            'created_at',
            'updated_at',
            'deleted_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
            'deleted_at',
        ]
    def get_created_at(self, obj):
        adjusted_datetime = obj.created_at + timedelta(hours=5)
        return adjusted_datetime.strftime('%d-%m-%Y %H:%M')
