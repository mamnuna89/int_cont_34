from modeltranslation.translator import register, TranslationOptions
from .models import Department, Division

@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Division)
class DivisionTranslationOptions(TranslationOptions):
    fields = ('name',)
