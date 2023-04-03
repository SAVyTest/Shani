from django.urls import include, path
from rest_framework import routers

from siteconfig.views import SiteSettingsViewSet, DisplayItemViewSet, get_all_site_details_api, PageViewSet, \
    get_default_site_details_api

router = routers.DefaultRouter()

router.register(r'display_items', DisplayItemViewSet)
router.register(r'pages', PageViewSet)
router.register(r'categori', PageViewSet)
router.register(r'pages', PageViewSet)
router.register(r'site_settings', SiteSettingsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/site_details', get_all_site_details_api),
    path('api/default_site_details', get_default_site_details_api),
]
