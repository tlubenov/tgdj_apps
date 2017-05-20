"""tglserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from rest_framework import routers

from django.contrib import admin

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'myriad_image_request', views.MyriadImageRequestViewSet)

from django.http import HttpResponse
from django.template import loader

from . import settings

def index(request):
    template = loader.get_template('index.html')
    try:
        settings.STATIC_ROOT
        djstr = settings.STATIC_ROOT
    except Exception as ex:
        djstr = ex
    response = {
        'static_root': djstr,
        'static_url': settings.STATIC_URL,
        'platform': settings.platf,
        'STATICFILES_DIRS': settings.STATICFILES_DIRS,
    }
    return HttpResponse(template.render(response, request))


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#    url(r'^apidocs$', schema_view),
    url(r'^rest/', include(router.urls)),
    #url(r'^', include('tlsites.urls')),
    url(r'^$', index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns