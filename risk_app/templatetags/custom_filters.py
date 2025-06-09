# risk_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def to(value, end, step=1):
    """Генератор диапазона: {% for i in 1|to:6 %} → 1,2,3,4,5"""
    return range(value, end)

@register.filter
def mul(value, arg):
    """Умножение: {{ impact|mul:probability }}"""
    try:
        return int(value) * int(arg)
    except:
        return 0

@register.filter
def dict_get(d, key):
    """Безопасное извлечение значения по ключу: {{ matrix|dict_get:i }}"""
    return d.get(key, {})
