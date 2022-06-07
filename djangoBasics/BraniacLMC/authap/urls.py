from authap.apps import AuthapConfig
from django.urls import path
from authap.views import CustomLoginView, RegisterView, CustomLogoutView, EditView

app_name = AuthapConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('edit/', EditView.as_view(), name='edit'),
]