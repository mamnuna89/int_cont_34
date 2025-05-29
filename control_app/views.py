from django.shortcuts import render, redirect
from .models import Risk
from .forms import RiskForm

def risk_list(request):
    risks = Risk.objects.all()

    # фильтры
    risk_type = request.GET.get('risk_type')
    department = request.GET.get('department')
    level = request.GET.get('level')

    if risk_type:
        risks = risks.filter(risk_type=risk_type)
    if department:
        risks = risks.filter(department=department)
    if level:
        risks = risks.filter(level=level)

    return render(request, 'control_risk_list.html', {'risks': risks})

def risk_create(request):
    if request.method == 'POST':
        form = RiskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('control_risk_list')
    else:
        form = RiskForm()
    return render(request, 'control_risk_form.html', {'form': form})
