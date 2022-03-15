import uuid
from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    uid = serializers.UUIDField(default=uuid.uuid4)
    description = serializers.CharField()
    created_at = serializers.DateField(format=)
