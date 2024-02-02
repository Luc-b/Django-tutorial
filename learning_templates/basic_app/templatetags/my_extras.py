from django import template

register=template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
this cuts all values of 'arg' from the string
    Args:
        value (_type_): _description_
        arg (_type_): _description_
    """
    return value.replace(arg,'')

# register.filter('cut',cut)