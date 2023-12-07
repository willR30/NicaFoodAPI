from django.urls import path
from rest_framework import routers
from .views import index, FoodViewSet

urlpatterns = [
    path('', index, name='index'),  # Esta línea asigna la función index a la ruta raíz ('/')
]

# Aquí puedes continuar usando el enrutador para tus vistas basadas en clases si así lo deseas
router = routers.DefaultRouter()
router.register('Food', FoodViewSet, 'Food')

# Agrega las URLs del enrutador a urlpatterns
urlpatterns += router.urls

