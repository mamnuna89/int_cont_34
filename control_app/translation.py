# control_app/translation.py

from modeltranslation.translator import translator, TranslationOptions
from .models import Department, Division

class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name',)

class DivisionTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Department, DepartmentTranslationOptions)
translator.register(Division, DivisionTranslationOptions)
