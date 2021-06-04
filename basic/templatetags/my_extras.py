from django import templates

register = templates.Library()


@register.filter(name='cut')
def cut(value, arg):
    """"
    This cuts out all values of "arg" form the string
    """
    return value.repalce(arg, '')

# register.filter('cut', cut)
