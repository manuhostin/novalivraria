from django.contrib import admin
from django.urls import include, path
from core.views.autor import AutorViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, UserViewSet

router = DefaultRouter()

router.register(r"categorias", CategoriaViewSet) # nova linha
router.register(r"editoras", EditoraViewSet)
router.register(r"autores", AutorViewSet)
router.register(r'usuarios', UserViewSet, basename='usuarios')


urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
