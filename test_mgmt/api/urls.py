from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from .apiviews import get_score, get_use_case_category_score, get_use_case_score, get_org_capacity_for_time_range, \
    get_engineer_capacity_for_time_range
from .views import UserViewSet, GroupViewSet, UseCaseViewSet, RequirementViewSet, FeatureViewSet, \
    RunViewSet, ExecutionRecordViewSet, AttachmentViewSet, DefectViewSet, ReleaseViewSet, EpicViewSet, SprintViewSet, \
    StoryViewSet, UseCaseCategoryViewSet, ReliabilityRunViewSet, OrgGroupViewSet, EngineerViewSet, SiteHolidayViewSet, \
    LeaveViewSet, EngineerOrgGroupParticipationViewSet, EnvironmentViewSet, TopicViewSet, \
    TopicEngineerAssignmentViewSet, EngineerOrgGroupParticipationHistoryViewSet, SiteViewSet, TagViewSet, \
    FeedbackViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'attachments', AttachmentViewSet)

router.register(r'org_groups', OrgGroupViewSet)
router.register(r'sites', SiteViewSet)
router.register(r'engineers', EngineerViewSet)
router.register(r'engineer_org_group_participation', EngineerOrgGroupParticipationViewSet)
router.register(r'site_holidays', SiteHolidayViewSet)
router.register(r'leaves', LeaveViewSet)
router.register(r'engineer_org_group_participation_history', EngineerOrgGroupParticipationHistoryViewSet)

router.register(r'releases', ReleaseViewSet)
router.register(r'epics', EpicViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'sprints', SprintViewSet)
router.register(r'stories', StoryViewSet)

router.register(r'use_case_categories', UseCaseCategoryViewSet)
router.register(r'use_cases', UseCaseViewSet)
# router.register(r'steps', StepViewSet)
router.register(r'requirements', RequirementViewSet)
router.register(r'tags', TagViewSet)
# router.register(r'steps', StepViewSet)

router.register(r'defects', DefectViewSet)
router.register(r'runs', RunViewSet)
router.register(r'execution_records', ExecutionRecordViewSet)
router.register(r'reliability_runs', ReliabilityRunViewSet)

router.register(r'environments', EnvironmentViewSet)

router.register(r'topics', TopicViewSet)
router.register(r'topic_engineer_assignments', TopicEngineerAssignmentViewSet)

router.register(r'feedbacks', FeedbackViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('usecases_count', use_case_count),
    # path('requirement_count', requirement_count),
    # path('testcases_count', test_case_count),

    path('auth/restframework', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/jwt/login', jwt_views.TokenObtainPairView.as_view()),
    path('auth/jwt/refresh', jwt_views.TokenRefreshView.as_view()),

    path('score/', get_score),
    path('use_case_category_score/<int:pk>', get_use_case_category_score),
    path('use_case_score/<int:pk>', get_use_case_score),
    # path('use_case_completion/<int:pk>', get_use_case_completion),
    # path('use_case_category_completion/<int:pk>', get_use_case_category_completion),
    # path('completion', get_overall_completion),

    path('capacity_view', get_org_capacity_for_time_range),
    path('engineer_capacity_view', get_engineer_capacity_for_time_range),
]
