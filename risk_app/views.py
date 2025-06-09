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

def risk_matrix_view(request):
    risks = Risk.objects.all()

    # Создаём матрицу 5x5: impact (1–5) — строки, probability (1–5) — столбцы
    matrix = {impact: {prob: [] for prob in range(1, 6)} for impact in range(1, 6)}

    for risk in risks:
        i = risk.impact
        p = risk.probability
        matrix[i][p].append(risk)

    context = {
        'matrix': matrix,
    }
    return render(request, 'risk_app/risk_matrix.html', context)

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
