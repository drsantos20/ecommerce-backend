from rest_framework import serializers


def generic_serializer(cls):
    class BaseSerializer(serializers.ModelSerializer):
        class Meta:
            model = cls
            fields = '__all__'

    return BaseSerializer
