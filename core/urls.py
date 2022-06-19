from django.urls import URLPattern, path
from .views import categoria, index, registro, api,api2,bandanas,correas,identificadores


urlpatterns=[
    path('', index),
    path('registro/', registro),
    path('api/', api),
    path('api2/', api2),
    path('bandanas/', bandanas),
    path('correas/', correas),
    path('identificadores/', identificadores),
    path('categoria/', categoria),
]