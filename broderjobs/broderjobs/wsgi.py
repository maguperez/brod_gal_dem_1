"""
WSGI config for broderjobs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys, traceback, signal, time

sys.path.append('/opt/python/current/app/broderjobs/broderjobs')

sys.path.append('/opt/python/current/app/Lib/site-packages')

sys.path.append('/usr/local/lib/python2.7/site-packages')

sys.path.append('/usr/local/lib64/python2.7/site-packages')

sys.path.append('/usr/lib/python2.7/dist-packages')

"""
sys.path.append('/usr/local/lib/python2.7/site-packages/psycopg2-2.6.1-py2.7-linux-x86_64.egg')
"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "broderjobs.settings")

from django.core.wsgi import get_wsgi_application

try:
   application = get_wsgi_application()
   print 'Sin excepcion'
except Exception:
   print 'manejar excepcion'
   #Error loading applications
   if 'mod_wsgi' in sys.modules:
      traceback.print_exc()
      os.kill(os.getpid(), signal.SIGINT)
      time.sleep(2.5)
