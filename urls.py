#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf import settings
from django.conf.urls import url
# Django 2.0 url import
from django.urls import include, path, re_path
from .views import landing
from .views import server_access

if settings.IS_PUBLIC:
    urlpatterns = [
        #url(r'^api/', include('api.urls')),
        #url(r'^rest/', include('REST.urls')),
        # url(r'^$', landing.qed_splash_page_old),
        # re_path(r'^$', landing.splash_landing_page),
        re_path(r'^$', landing.splash_landing_page),
        re_path(r'^api/$', landing.api_landing_page),
        re_path(r'^api/pram/$', server_access.qed_api_pram),
        re_path(r'^source/$', landing.source_landing_page),
        re_path(r'^wiki/$', landing.wiki_landing_page),
        #url(r'^$', views.qed_splash_page_intranet),
        # url(r'^admin/', include(admin.site.urls)),
    ]
else:
    urlpatterns = [
        # url(r'^api/', include('api.urls')),
        # url(r'^rest/', include('REST.urls')),
        re_path(r'^$', landing.splash_landing_page),
        re_path(r'^api/$', landing.api_landing_page),
        re_path(r'^api/pram/$', server_access.qed_api_pram),
        re_path(r'^rest/(?P<model>.*?)/?$', server_access.pram_rest_model),
        re_path(r'^rest_landing/$', landing.rest_landing_page),
        re_path(r'^qed_external_redirect/$', landing.qed_external_redirect),
        re_path(r'^source/$', landing.source_landing_page),
        re_path(r'^wiki/$', landing.wiki_landing_page),
        # url(r'^$', landing.splash_landing_page),
        # url(r'^api$', landing.api_landing_page),
        # url(r'^api/pram$', server_access.qed_api_pram),
        # url(r'^rest/(?P<model>.*?)/?$', server_access.pram_rest_model),
        # url(r'^rest$', landing.rest_landing_page),
        # url(r'^qed_external_redirect$', landing.qed_external_redirect),
        # url(r'^source$', landing.source_landing_page),
        # url(r'^wiki$', landing.wiki_landing_page),

        #url(r'^$', views.qed_splash_page_intranet),
        # url(r'^admin/', include(admin.site.urls)),
    ]

# 404 Error view (file not found)
handler404 = landing.file_not_found
# 500 Error view (server error)
handler500 = landing.file_not_found
# 403 Error view (forbidden)
handler403 = landing.file_not_found
