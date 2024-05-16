from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('mainApp.urls')),
    path('user/', include('userApp.urls')),
    path('order/', include('orderApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
