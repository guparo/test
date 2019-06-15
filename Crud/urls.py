from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('video', TemplateView.as_view(template_name='crud/video.html'), name='video'),

    path('chart/',          views.chart,                name='chart'),




    path('passenger_pdf',             views.passengerPdf.as_view(),    name='passenger_pdf'),

    path('passenger_pdf2',            views.passengerPdf2.as_view(),    name='passenger_pdf2'),


    path('passenger_list',            views.PassengerList.as_view(),   name='passenger_list'),
    path('passenger_view/<int:pk>',   views.PassengerView.as_view(),   name='passenger_view'),
    path('passenger_new',             views.PassengerCreate.as_view(), name='passenger_new'),
    path('passenger_edit/<int:pk>',   views.PassengerUpdate.as_view(), name='passenger_edit'),
    path('passenger_delete/<int:pk>', views.PassengerDelete.as_view(), name='passenger_delete'),

  #  path('json-example/',             views.json_example,              name='json_example'),
  #  path('json-example/data/',        views.chart_data,                name='chart_data'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)