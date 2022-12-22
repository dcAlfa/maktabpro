from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from maktabapp.views import *
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns




urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('news/', New.as_view(), name="news"),
    path('media/', Media.as_view(), name="media"),
    path('jurnal/', Jurnal.as_view(), name="jurnal"),
    path('room/', Room.as_view(), name="room"),
    path('plis/', Puplis.as_view(), name="publis"),
    path('juritem/<int:pk>/', Jurnalitem.as_view(), name="juritem"),
    path('contact/', Contact.as_view(), name="contact"),
    path('logout/', Logout.as_view(), name="out"),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
admin.site.site_header = "Kirish"