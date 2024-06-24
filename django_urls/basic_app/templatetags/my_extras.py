from django import template


register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    
    this cuts any value of arg
    """

    return value.replace(arg, '')

# register.filter('cut', cut)