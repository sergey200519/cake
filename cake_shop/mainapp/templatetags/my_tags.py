from django import template

register = template.Library()

@register.filter
def get_product_by_weight(model, weight):
    return model.filter(weight=weight)