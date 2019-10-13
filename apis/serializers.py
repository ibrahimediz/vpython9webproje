from rest_framework import serializers
from todolist import models

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'konu',
            'tanim',
        )
        model = models.todolist