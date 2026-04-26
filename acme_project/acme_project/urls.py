# Импортируем настройки проекта.
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
