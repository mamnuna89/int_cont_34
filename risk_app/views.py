from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('risk_app:risk_list')
    else:
        form = RiskForm()
    return render(request, 'risk_form.html', {'form': form, 'risk': None})

def risk_detail(request, risk_id):
    risk = get_object_or_404(Risk, id=risk_id)

    if request.method == 'POST':
        form = RiskForm(request.POST, instance=risk)
        if form.is_valid():
            form.save()
            return redirect('risk_app:risk_list')
    else:
        form = RiskForm(instance=risk)

    return render(request, 'risk_app/risk_detail.html', {'form': form, 'risk': risk})

def risk_delete(request, risk_id):
    risk = get_object_or_404(Risk, id=risk_id)
    if request.method == 'POST':
        risk.delete()
        return redirect('risk_app:risk_list')
    return redirect('risk_app:risk_detail', risk_id=risk.id)

def risk_update(request, pk):
    risk = get_object_or_404(Risk, pk=pk)
    if request.method == 'POST':
        form = RiskForm(request.POST, instance=risk)
        if form.is_valid():
            form.save()
            return redirect('risk_app:risk_list')
    else:
        form = RiskForm(instance=risk)
    return render(request, 'risk_app/risk_update.html', {'form': form, 'risk': risk})

def risk_matrix_view(request):
    department_filter = request.GET.get('department', '')
    process_filter = request.GET.get('process', '')

    risks = Risk.objects.all()

    if department_filter:
        risks = risks.filter(department=department_filter)
    if process_filter:
        risks = risks.filter(process=process_filter)

    matrix = {}
    for impact in range(1, 6):
        matrix[impact] = {}
        for prob in range(1, 6):
            matrix[impact][prob] = []

    for risk in risks:
        matrix[risk.impact][risk.probability].append(risk)

    context = {
        'matrix': matrix,
        'departments': Risk.objects.values_list('department', flat=True).distinct(),
        'processes': Risk.objects.values_list('process', flat=True).distinct(),
        'selected_department': department_filter,
        'selected_process': process_filter,
    }
    return render(request, 'risk_app/risk_matrix.html', context)
