from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [


    path('contact_new',     views.ContactCreate.as_view(),   name='contact_new'),
    path('contact_list',    views.ContactList.as_view(),     name='contact_list'),




]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)