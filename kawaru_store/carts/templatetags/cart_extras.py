from django import template
register = template.Library()

@register.filter
def formato_cant_productos(cantidad=1):
    return '{} {}'.format(cantidad, 'productos' if cantidad > 1 else 'producto')

@register.filter
def formato_productos_agregados(cantidad):
    return '{} {}'.format(
        formato_cant_productos(cantidad),
        'agregados' if cantidad > 1 else 'agregado'
    )