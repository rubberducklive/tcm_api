from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import PrimaryUUIDTimeStampedModel


PROJECT_ROLES = (
    ("lead", "Lead"),
    ("member", "Member"),
)


class Organisation(PrimaryUUIDTimeStampedModel):

    name = models.CharField(_("Name of the organisation"), blank=False, max_length=255, unique=True)
    root_user = models.ForeignKey(
        "users.User",
        related_name="organisations",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Project(PrimaryUUIDTimeStampedModel):

    name = models.CharField(
        _("Name of the project"), blank=False, null=False, max_length=255
    )
    organisation = models.ForeignKey(
        "Organisation",
        related_name="projects",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    team = models.ManyToManyField(
        "users.User", related_name="projects", through="ProjectMembership"
    )

    def __str__(self):
        return self.name


class ProjectMembership(PrimaryUUIDTimeStampedModel):

    project = models.ForeignKey(
        "Project",
        blank=False,
        null=False,
        related_name="project_members",
        on_delete=models.CASCADE,
    )
    member = models.ForeignKey(
        "users.User",
        blank=False,
        null=False,
        related_name="project_members",
        on_delete=models.CASCADE,
    )
    role = models.CharField(
        _("Role for the project"),
        blank=False,
        null=False,
        choices=PROJECT_ROLES,
        max_length=16,
    )

    def __str__(self):
        return f"{self.project.name} | {self.member.first_name}"
