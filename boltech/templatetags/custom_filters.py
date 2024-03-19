from django import template
from datetime import datetime ,timedelta
from django.utils import timezone
from django.utils.timesince import timesince
register = template.Library()


@register.filter
def strftime(value, format_string):
    if isinstance(value, datetime):
        return value.strftime(format_string)
    return value 

@register.filter
def replace_dash(value=None):
    return value.replace("_" , " ").title() if value != None else ""

@register.filter
def humanize_time(value):
  return timesince(value) + " ago"

@register.filter
def slice_description(description, length):
    return description[:length]