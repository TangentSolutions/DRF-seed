from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

{% if with_api %}
from api.views import router
{% endif %}

urlpatterns = [
    url(r'^admin/', admin.site.urls),

{% if with_api | bool %}
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
{% endif %}
{% if with_swagger | bool %}
    url(r'^explorer/', 
    	include('rest_framework_swagger.urls', namespace='swagger')),
{% endif %}
]

# Setting up static files for development:
if settings.DEBUG is True:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
