from django import template
register = template.Library()


# filter to get month by list index
@register.filter
def month_index(array, i):
    return array[int(i) - 1]