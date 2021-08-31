from django.shortcuts import render
from .models import model
from .forms import DateTime


def index(request):
    form = DateTime()
    if request.method == 'POST':
        day = int(request.POST.get('date')[0:2])
        hour = int(request.POST.get('time')[0:2])
        message = model({'day': day, 'hour': hour})
        return render(request, 'mainApp/index.html', {'form': form, 'message': message})
    elif request.method == 'GET':
        return render(request, 'mainApp/index.html', {'form': form})