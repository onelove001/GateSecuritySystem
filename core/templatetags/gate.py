from django import template
from core.models import *



register = template.Library()

@register.filter
def gate_tag(value):
    return value[:15]
