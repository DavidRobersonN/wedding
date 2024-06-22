from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # Certifique-se de que 'admin/' termine com '/'
    path('', include('core.urls')),
    path('', include('conta.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
