
from django.contrib import admin
from django.conf.urls import url, include
from django.views.static import serve
from ttsx.settings import MEDIA_ROOT


urlpatterns = [
    url('admin/', admin.site.urls),
    url('account/', include('account.urls', namespace='account')),
    url('^', include('goods.urls', namespace='goods')),
    url('media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
]
