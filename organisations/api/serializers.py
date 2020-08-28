from rest_framework import serializers

from organisations.models import Organisation, Project


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ("id", "name")


class ProjectSerializer(serializers.ModelSerializer):
    organisation = OrganisationSerializer(read_only=True)
    organisation_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Project
        fields = ("id", "name", "organisation", "organisation_id")
