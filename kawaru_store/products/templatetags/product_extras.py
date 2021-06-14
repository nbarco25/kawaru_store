from django import template


register = template.Library()
#funciones que realicen tareas sencillas

@register.filter() #Decorador
def formato_precio_cop(value):
    return '${:,.0f}'.format(value)