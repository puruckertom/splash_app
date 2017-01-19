#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf.urls import include, url
import views


urlpatterns = [
    #url(r'^api/', include('api.urls')),
    #url(r'^rest/', include('REST.urls')),
    url(r'^$', views.qed_splash_page_public),
    #url(r'^$', views.qed_splash_page_intranet),
    # url(r'^admin/', include(admin.site.urls)),
]

# 404 Error view (file not found)
handler404 = views.file_not_found
# 500 Error view (server error)
handler500 = views.file_not_found
# 403 Error view (forbidden)
handler403 = views.file_not_found
