from django.shortcuts import render

from django.db.models import Count, Q

from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from contact.models import  Contact
from .models import Passenger
from contact.forms import ContactForm


from django.views.generic import View, ListView, DetailView
from django.utils import timezone
from .render import Render



from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

class passengerPdf(View):

    def get(self, request):
        passenger = Passenger.objects.all()

        today = timezone.now()
        params = {
            'today': today,
            'passenger': passenger,
            'request': request
        }
        return Render.render('crud/passenger_pdf.html', params) 

class passengerPdf2(View):

    def cabecera(self,pdf):
     #   archivo_imagen = settings.MEDIA_ROOT + '/imagenes/varco.png'
        archivo_imagen = settings.STATIC_ROOT + '/img/logo.png'
        print("media_root " + settings.MEDIA_ROOT )





        pdf.drawImage(archivo_imagen, 40, 750, 120, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)         
        pdf.drawString(230, 790, u'TITANIC')
        pdf.setFont('Helvetica', 14)
        pdf.drawString(224, 770, u'REPORT PASSENGERS')

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 680
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        nombre_archivo = 'ReportPassengers.pdf'
        contenido = 'attachment; filename={0}'.format(nombre_archivo)
        response['Content-Disposition'] = contenido

        return response    

    def tabla(self,pdf,y):
        encabezados = ('Id', 'Name', 'Survived', 'age', 'sexo', 'class')
        detalles = [(passenger.id, passenger.name, passenger.survived, passenger.age, passenger.sexo, passenger.ticket_class) for passenger in Passenger.objects.all()]
        detalle_orden = Table([encabezados] + detalles, colWidths = [2 * cm, 6 * cm, 2 * cm, 2 * cm, 2* cm, 2 * cm])
        detalle_orden.setStyle(TableStyle(
            [
                ('ALIGN',(0,0),(3,0),'CENTER'),
                ('GRID',(0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1,-1), 10),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60,y)

def chart(request):
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')
    return render(request, 'crud/chart.html', {'dataset': dataset})




def chart_data(request):
    dataset = Passenger.objects \
        .values('embarked') \
        .exclude(embarked='') \
        .annotate(total=Count('embarked')) \
        .order_by('embarked')

    port_display_name = dict()
    for port_tuple in Passenger.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'series': [{
            'name': 'Embarkation Port',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)



class PassengerList(ListView):
    model = Passenger
    template_name="crud/passenger_list.html"


class PassengerView(DetailView):
    model = Passenger
    template_name="crud/passenger_detail.html"

class PassengerCreate(CreateView):
    model = Passenger
    template_name="crud/passenger_form.html"
    fields = ['name', 'image','survived','ticket_class','age','sexo','text']
    success_url = reverse_lazy('chart')

class PassengerUpdate(UpdateView):
    model = Passenger
    template_name="crud/passenger_form.html"

    fields = ['name','image','survived','ticket_class','age','sexo','text']
    success_url = reverse_lazy('passenger_list')

class PassengerDelete(DeleteView):
    model = Passenger
    template_name="crud/passenger_confirm_delete.html"

    #messages.add_message(request, messages.INFO, 'Data Delete Successfully')
    success_url = reverse_lazy('passenger_list')

