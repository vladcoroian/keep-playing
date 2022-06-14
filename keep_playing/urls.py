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
    path('login/', obtain_auth_token, name='login'),
]
