from django import template

register = template.Library()

@register.filter
def format_phone(phone_number):
    # Telefon numarasını belirli bir formata dönüştürmek için gerekli kodu buraya yazın
    # Örneğin:
    # +905443574293 --> +90 544 357 42 93
    
    # PhoneNumber nesnesini dizeye dönüştür
    phone_str = str(phone_number)
    
    # Dizeyi istenen formata dönüştür
    formatted_phone = "+90 {} {} {} {}".format(phone_str[3:6], phone_str[6:9], phone_str[9:11], phone_str[11:])
    return formatted_phone


@register.filter
def format_date(date):
    
    months = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
    
    formatted_date = "{} {} {}, {}".format(date.day, months[date.month-1], date.year, date.strftime("%H:%M"))
    return formatted_date
