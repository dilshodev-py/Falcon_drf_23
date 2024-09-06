from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from root import settings

urlpatterns = [
path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('product', include('apps.product.urls')),
    path('user', include('apps.users.urls')),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
