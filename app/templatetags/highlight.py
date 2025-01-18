from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def highlight(value, query):
    """
    Highlights occurrences of the query string in the given value.
    """
    if not value or not query:
        return value
    highlighted = value.replace(
        query, f'<span style="background:yellow;">{query}</span>'
    )
    return mark_safe(highlighted)
