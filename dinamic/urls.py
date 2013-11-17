from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dinamic.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', 'core.views.index'),
                       url(r'^get-data$', 'core.views.get_data'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
