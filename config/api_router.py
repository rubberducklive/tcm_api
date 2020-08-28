from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from tcm_api.users.api.views import UserViewSet
from organisations.api.views import OrganisationViewSet, ProjectViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("organisations", OrganisationViewSet)
router.register("projects", ProjectViewSet)


app_name = "api"
urlpatterns = router.urls
