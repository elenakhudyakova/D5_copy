from django import template

register = template.Library()
censorwords = ["сука", "блять", "пиздец", "хуй", "ебать"]

@register.filter(name='censor')
def censor(value):
    for a in censorwords:
        b = str(a + ",")
        с = str(b.title())
        value = value.replace(a, "&#129324;")
        value = value.replace(b, "&#129324;")
        value = value.replace(с, "&#129324;")
    return value
