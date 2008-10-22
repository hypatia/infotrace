from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from forms import PingForm

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def ping(request):
    if request.method == 'POST':
        form = PingForm(request.POST)
    else:
        form = PingForm()
    return render_to_response('contact.html', {'form': form})

