from django import template

register = template.Library()

@register.filter(name="iconize")
def iconize(user):
    if user.first_name and user.last_name:
        icon = user.first_name[0] + user.last_name[0]
    else:
        icon = 'ad'
    return icon.upper()