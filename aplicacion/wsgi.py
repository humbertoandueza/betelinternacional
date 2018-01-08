# +++++++++++ DJANGO +++++++++++
#Para usar tu propia aplicación Django usa un código como este:
import  os
import  sys

# asumiendo que el archivo de configuración de Django está en '/home/myusername/mysite/mysite/settings.py'
path  =  '/ home / humberto / betelinternacional / aplicacion'
#si la  ruta  no está  en el  sistema . camino :
#    sys . trayectoria . Añadir ( ruta )

os . environ [ 'DJANGO_SETTINGS_MODULE' ]  =  'aplicacion.settings'

## Descomente las líneas a continuación dependiendo de su versión de Django
###### luego, para Django> = 1.5:
from  django.core.wsgi  import  get_wsgi_application
application  =  get_wsgi_application ()
###### o, para
#versiones anteriores de Django < = 1.4 #import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler ()