from django.shortcuts import render
from .models import Department

def department_list(request):
    departments = Department.objects.prefetch_related('divisions').all()
    return render(request, 'process_map/department_list.html', {'departments': departments})
def diagram_list(request):
    # Пока просто заглушка, позже добавим список схем
    return render(request, 'process_map/diagram_list.html')