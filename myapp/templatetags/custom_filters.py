from django import template

register = template.Library()

@register.filter(name='truncate_with_ellipsis')
def truncate_with_ellipsis(text, max_length):
    if len(text) <= max_length:
        return text
    else:
        truncated_text = text[:max_length] + '  ........'
        return truncated_text




