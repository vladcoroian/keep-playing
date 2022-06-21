from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('events/', views.EventView.as_view(), name='events'),
    path('users/', views.UsersRecordView.as_view(), name='users'),
    path('user/', views.UserRecordView.as_view(), name='user'),
    path('events/<int:pk>/', views.EventView.as_view(), name='events'),
    path('events/<int:pk>/apply/', views.CoachEventView.as_view(), name='apply'),
    path('events/<int:pk>/cancel/', views.CoachCancelEventView.as_view(), name='cancel'),
    path('events/<int:pk>/accept/<int:coach_pk>/', views.AcceptOfferView.as_view(), name='apply'),
    path('coach/<int:pk>/', views.CoachEventView.as_view(), name='coach'),
    path('organiser/', views.OrganiserView.as_view(), name='organiser'),
    path('organiser/block/<int:coach_pk>/', views.OrganiserBlockCoachView.as_view(), name='organiser_block'),
    path('organiser/unblock/<int:coach_pk>/', views.OrganiserUnblockCoachView.as_view(), name='organiser_unblock'),
    path('organiser/add-favourite/<int:coach_pk>/', views.OrganiserAddFavouriteCoachView.as_view(), name='organiser_add_favourite'),
    path('organiser/remove-favourite/<int:coach_pk>/', views.OrganiserRemoveFavouriteCoachView.as_view(), name='organiser_remove_favorite'),
    path('organiser/events/', views.OrganiserEventsView.as_view(), name='organiser_events'),
    path('coach/feed/', views.CoachFeedView.as_view(), name='coach_feed'),
    path('coach/upcoming-jobs/', views.CoachUpcomingJobsView.as_view(), name='coach_upcoming_jobs'),
    path('login/', obtain_auth_token, name='login'),
]


