from django import template

register = template.Library()

@register.filter(name="iconize")
def iconize(user):
    icon = user.first_name[0] + user.last_name[0]
    return icon.upper()