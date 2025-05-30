from django.shortcuts import render, redirect
from .models import Risk, ControlPoint
from .forms import RiskForm, ControlPointForm

# 👉 Главная страница модуля внутреннего контроля
def control_index(request):
    return render(request, 'control_app/control_index.html')

# 👉 Отображение списка рисков
def risk_list(request):
    risks = Risk.objects.all()

    # Фильтрация
    department_filter = request.GET.get('department')
    risk_type_filter = request.GET.get('risk_type')
    level_filter = request.GET.get('level')

    if department_filter:
        risks = risks.filter(department__icontains=department_filter)
    if risk_type_filter:
        risks = risks.filter(risk_type__icontains=risk_type_filter)
    if level_filter:
        try:
            level_value = int(level_filter)
            risks = risks.filter(level=level_value)
        except ValueError:
            pass

    # Цветовая индикация
    for risk in risks:
        if risk.level is not None:
            if risk.level <= 6:
                risk.color = 'green'
            elif 7 <= risk.level <= 14:
                risk.color = 'yellow'
            else:
                risk.color = 'red'
        else:
            risk.color = 'gray'

    return render(request, 'control_app/control_risk_list.html', {'risks': risks})

# 👉 Создание нового риска
def risk_create(request):
    if request.method == 'POST':
        form = RiskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('control_risk_list')  # исправлено на правильный redirect
    else:
        form = RiskForm()
    return render(request, 'control_app/control_risk_form.html', {'form': form})

# 👉 Создание контрольной точки
def control_point_create(request):
    if request.method == 'POST':
        form = ControlPointForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('control_index')  # временно возвращаемся на главную
    else:
        form = ControlPointForm()
    return render(request, 'control_app/control_point_form.html', {'form': form})

