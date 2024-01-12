from rest_framework import serializers


class UsageDataSerializer(serializers.Serializer):
    flags = serializers.IntegerField()
    identities = serializers.IntegerField()
    traits = serializers.IntegerField()
    environment_document = serializers.IntegerField()
    day = serializers.CharField()


class UsageDataQuerySerializer(serializers.Serializer):
    project_id = serializers.IntegerField(required=False)
    environment_id = serializers.IntegerField(required=False)


class UsageTotalCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class SDKAnalyticsFlagsQuerySerializer(serializers.Serializer):
    identity_identifier = serializers.CharField(
        required=False, default=None, allow_null=True
    )
    enabled_when_evaluated = serializers.BooleanField(
        required=False, default=None, allow_null=True
    )
