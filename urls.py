from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from app.serializers import UserViewSet
from app.views import AppView
from session.views import SessionView

router = DefaultRouter()
router.register(r'users', UserViewSet)


admin.autodiscover()

urlpatterns = patterns('',
   # Examples:
   # url(r'^$', 'webmdee.views.home', name='home'),
   # url(r'^blog/', include('blog.urls')),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^/?$', AppView.as_view()),
   url(r'^session/$', SessionView.as_view()),
   url(r'^api/', include(router.urls)),
)
