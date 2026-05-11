from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/resources/', include('resources.urls')),
    path('api/interactions/', include('interactions.urls')),
] + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
