#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf.urls import include, url
from views import misc, landing


# All view functions here must be in '/views/views.py'
urlpatterns = [
    #url(r'^api/', include('api.urls')),
    #url(r'^rest/', include('REST.urls')),
    url(r'^$', landing.qed_splash_test),
    #url(r'^$', landing.qed_splash_page),
    #url(r'^$', landing.qed_landing_page),
    # url(r'^admin/', include(admin.site.urls)),
]

# 404 Error view (file not found)
handler404 = misc.file_not_found
# 500 Error view (server error)
handler500 = misc.file_not_found
# 403 Error view (forbidden)
handler403 = misc.file_not_found
