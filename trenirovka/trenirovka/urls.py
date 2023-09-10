from django.contrib import admin
from django.urls import path, include
from products.views import IndexView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users'))
]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)