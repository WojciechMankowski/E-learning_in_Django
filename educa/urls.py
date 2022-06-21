from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from courses.views import ManageCourseListView
urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', ManageCourseListView.as_view()),
    path("course/", include("courses.urls")),
    path('admin/', admin.site.urls),
]
