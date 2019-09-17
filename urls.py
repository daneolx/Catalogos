from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from principal.views import BooksPage

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','principal.views.inicio'),
    url(r'^segmentos/(?P<codigo>\d+)$','principal.views.segmentos'),
    url(r'^familias/(?P<codigo>\d+)$','principal.views.familias'),
    url(r'^productos/(?P<codigo>\d+)$','principal.views.productos'),
    url(r'^clases/(?P<codigo>\d+)$','principal.views.clases'),
    url(r'^buscar/$', 'principal.views.buscar'),
    url(r'^books/$', BooksPage.as_view(), name='books'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)