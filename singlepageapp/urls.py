from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_control
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve

# from . import views
from . import settings


urlpatterns = [
    path('', include('spa.urls')),
    path('admin/', admin.site.urls),
    # path('spa/', include('spa.urls')),
] + static(settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve)) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
