from django import template

register = template.Library()

@register.filter
def simple_accomplishment(fulfillment):
    if fulfillment.percentage > 0 and \
            fulfillment.percentage < 100:
        return 'half-accomplished'
    if fulfillment.percentage >= 100:
        return 'accomplished'
    return 'not-accomplished'
