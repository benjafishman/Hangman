from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from minyan_mailer.models import Davening, Minyan
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the minyan mailer index.")

def davening_sign_up(request, minyan_id):
    minyan = get_object_or_404(Minyan, pk=minyan_id)

    davenings = minyan.davening_set.all()

    print(davenings)

    return render(request, 'minyan_mailer/sign_up.html', {'minyan': minyan})
