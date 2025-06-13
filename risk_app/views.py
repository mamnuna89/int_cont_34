from django.shortcuts import render, redirect, get_object_or_404
from .models import Risk
from .forms import RiskForm
from control_app.models import Department  # ForeignKey к департаменту
from django.db.models import Q
from django.http import HttpResponse
import openpyxl


def index(request):
    return render(request, 'index.html')


def risk_list(request):
    department_id = request.GET.get('department')
    process_filter = request.GET.get('process')

    risks = Risk.objects.all()
    if department_id:
        risks = risks.filter(department__id=department_id)
    if process_filter:
        risks = risks.filter(process__icontains=process_filter)

    departments = Department.objects.all()
    context = {
        'risks': risks,
        'departments': departments,
        'selected_department': department_id,
        'selected_process': process_filter,
    }
    return render(request, 'risk_list.html', context)


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
    department_id = request.GET.get('department')
    process_filter = request.GET.get('process')

    risks = Risk.objects.all()
    if department_id:
        risks = risks.filter(department__id=department_id)
    if process_filter:
        risks = risks.filter(process__icontains=process_filter)

    matrix = {impact: {prob: [] for prob in range(1, 6)} for impact in range(1, 6)}

    for risk in risks:
        matrix[risk.impact][risk.probability].append(risk)

    context = {
        'matrix': matrix,
        'departments': Department.objects.all(),
        'processes': Risk.objects.values_list('process', flat=True).distinct(),
        'selected_department': department_id,
        'selected_process': process_filter,
    }
    return render(request, 'risk_app/risk_matrix.html', context)


def export_risks_to_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Risks"

    headers = [
        "№", "Risk Code", "Name", "Type", "Source", "Registration Date",
        "Department", "Owner", "Process", "Probability", "Impact", "Risk Level"
    ]
    ws.append(headers)

    for idx, risk in enumerate(Risk.objects.all(), start=1):
        ws.append([
            idx,
            risk.risk_code,
            risk.name,
            risk.risk_type,
            risk.source,
            risk.registered_at.strftime('%Y-%m-%d'),
            str(risk.department),
            risk.owner,
            risk.process,
            risk.probability,
            risk.impact,
            risk.level,
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=risks.xlsx'
    wb.save(response)
    return response
