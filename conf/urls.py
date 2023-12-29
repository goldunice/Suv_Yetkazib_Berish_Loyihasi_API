from django.contrib import admin
from django.urls import path
from mainApp.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Suv yetkazib berish loyihasi uchun Doc fayl',
        default_version='v1.0',
        description='Front-end, Android, Desktop dasturchilar uchun Blog-API DOCS',
        contact=openapi.Contact(email='AkmaljonGold@gmail.com'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('suvlar/', SuvlarAPIView.as_view()),
    path('suv/<int:pk>/', SuvAPIView.as_view()),
    path('mijozlar/', MijozlarAPIView.as_view()),
    path('mijoz/<int:pk>/', MijozAPIView.as_view()),
    path('buyurtmalar/', BuyurtmalarAPIView.as_view()),
    path('haydovchilar/', HaydovchilarAPIView.as_view()),
    path('haydovchi/<int:pk>/', HaydovchiAPIView.as_view()),
    path('adminlar/', AdminlarAPIView.as_view()),
    path('admin/<int:pk>/', AdminAPIView.as_view()),
]
