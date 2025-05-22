from django.shortcuts import render, redirect
from .models import Risk
from .forms import RiskForm

def index(request):
    return render(request, 'index.html')

def risk_list(request):
    risks = Risk.objects.all()
    return render(request, 'risk_list.html', {'risks': risks})

def risk_create(request):
    if request.method == 'POST':
        form = RiskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('risk_list')
    else:
        form = RiskForm()
    return render(request, 'risk_form.html', {'form': form})
