from rest_framework import serializers

from meetings.models import Meeting


class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meeting
        fields = ('title', 'date', 'duration')
