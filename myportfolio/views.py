from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import mimetypes

class index(ListView):
    form_class = ContactForm
    template_name = 'index.html'

    def get(self, request, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print("sreek")
            data = form.cleaned_data
            name=data.get('name')
            email=data.get('email')
            message = data.get('message')
            details ="Name : " +name + " Email : " +email + " Message : " +message
            send_mail('Contact Form',details,settings.EMAIL_HOST_USER,["modupallisreekanth99@gmail.com"],fail_silently=False,)
        return render(request, self.template_name, {'form': form})


class readmore(ListView):
    template_name = 'post.html'
    def get(self, request, **kwargs):
        return render(request, self.template_name)

def download_file(request):
    fl_path = 'templatesSreekanth.Modupalli@Resume.pdf'
    filename = 'myresume.pdf'
    fl=open(fl_path,'r')
    mime_type, _ =mimetypes.guess_type(fl_path)
    response = HttpResponse(fl ,content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response