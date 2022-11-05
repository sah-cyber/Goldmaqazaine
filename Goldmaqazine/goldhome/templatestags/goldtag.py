from django import template

from goldhome.models import Gold


register = template.Library()


@register.simple_tag()
def get_gold():
    return Gold.objects.all()

def get_categories():
    return Category.objects.all()


