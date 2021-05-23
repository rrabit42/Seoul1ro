from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main import views
from main.views import SendtoAIView, ShowResult

router = routers.DefaultRouter()

# router.register('', views.SendtoAIView, 'main')
# input = SendtoAIView.as_view({
#     'post': 'create',
# })
#
# list = SendtoAIView.as_view({
#     'get': 'list',
# })

urlpatterns = [
    path('', ShowResult),
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)