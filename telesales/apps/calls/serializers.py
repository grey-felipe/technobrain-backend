from rest_framework import serializers
from datetime import datetime
from django.utils.timezone import get_current_timezone

from .models import Call


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('id', 'caller_name', 'caller_email', 'caller_phone',
                  'disposition', 'callback_date', 'updated_at', 'created_at')
    id = serializers.CharField(read_only=True)
    callback_date = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)


class UpdateDispositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('disposition',)

    def update(self, instance, validated_data):
        instance.disposition = validated_data['disposition']
        instance.updated_at = datetime.now(
            tz=get_current_timezone()).isoformat()
        instance.save()
        return instance
