from django import template
from datetime import date, timedelta
from mensaje.models import Mensaje, Notificacion
from oportunidad.models import Oportunidad

register = template.Library()

@register.filter(name='get_due_date_string')

def get_due_date_string(value):
    try:
        delta = value - date.today()
        if delta.days == 0:
            return "Hoy!"
        elif delta.days < 1:
            return "Hace %s %s !" % (abs(delta.days),
                ("dia" if abs(delta.days) == 1 else "dias"))
        elif delta.days == 1:
            return "Ayer!"
        elif delta.days > 1:
            return "In %s days" % delta.days
    except:
        return ""
