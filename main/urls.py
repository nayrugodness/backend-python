from django.urls import path, include
from main import views
from rest_framework import routers

app_name = "hoisu"
router = routers.DefaultRouter()


# localhost:8000/api/producto/


urlpatterns = [
    path('', views.homepage, name='index'),

    path('api/', include(router.urls)),

]
