from django.shortcuts import render

def bpmn_editor(request):
    return render(request, 'bpmn_app/bpmn_editor.html')
