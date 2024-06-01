from django import template

register = template.Library()

@register.filter
def format_phone(value):
    # Telefon numarasını belirli bir formata dönüştürmek için gerekli kodu buraya yazın
    # Örneğin:
    # +905443574293 --> +90 544 357 42 93
    formatted_phone = "+90 {} {} {} {}".format(value[3:6], value[6:9], value[9:11], value[11:])
    return formatted_phone