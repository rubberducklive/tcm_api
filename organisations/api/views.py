from rest_framework import viewsets

from organisations.models import Organisation, Project
from organisations.api.serializers import OrganisationSerializer, ProjectSerializer


class OrganisationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(root_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(root_user=self.request.user)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self, *args, **kwargs):
        # TODO: Add appropriate select_related and prefetch_related
        return self.queryset.filter(organisation__root_user=self.request.user)

