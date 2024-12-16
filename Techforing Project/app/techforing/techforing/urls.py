from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from pmtool.urls import router as pmtool_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(pmtool_router.urls)),
]
