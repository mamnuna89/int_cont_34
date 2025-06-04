from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Risk, ControlPoint, Department, Division, ProcessDiagram
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
            return redirect('control_point_list')
    else:
        form = ControlPointForm()
    return render(request, 'control_app/control_point_form.html', {'form': form})

from .models import Department  # убедись, что импорт есть

def control_point_list(request):
    selected_department = request.GET.get('department')

    if selected_department:
        control_points = ControlPoint.objects.filter(division__department__name=selected_department)
    else:
        control_points = ControlPoint.objects.all()

    departments = Department.objects.all()  # 🔄 для фильтра

    return render(request, 'control_app/control_point_list.html', {
        'control_points': control_points,
        'departments': departments,
        'selected_department': selected_department,
    })


def department_structure(request):
    departments = Department.objects.prefetch_related('divisions').all()
    return render(request, 'control_app/department_structure.html', {'departments': departments})

def process_map_overview(request):
    departments = Department.objects.prefetch_related('divisions').all()
    return render(request, 'control_app/process_map_overview.html', {'departments': departments})

def diagram_list(request):
    departments = Department.objects.prefetch_related('divisions__processdiagram_set')
    return render(request, 'control_app/diagram_list.html', {
        'departments': departments
    })

# 👉 Сохранение схемы из редактора
@require_POST
def save_process_diagram(request):
    name = request.POST.get('name')
    department_id = request.POST.get('department_id')
    division_id = request.POST.get('division_id')
    bpmn_xml = request.POST.get('bpmn_xml')

    department = Department.objects.get(id=department_id)
    division = Division.objects.get(id=division_id)

    diagram = ProcessDiagram.objects.create(
        name=name,
        department=department,
        division=division,
        bpmn_xml=bpmn_xml,
        created_by=request.user
    )
    return JsonResponse({'status': 'success', 'diagram_id': diagram.id})
def editor_view(request):
    departments = Department.objects.prefetch_related('divisions').all()
    return render(request, 'control_app/editor.html', {'departments': departments})
