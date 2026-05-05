"""Заглушка."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Заглушка."""

    class Meta:
        """Заглушка."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
