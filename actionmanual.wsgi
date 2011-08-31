import os
import sys

sys.path = ['/home/cityparks/webapps/actionmanual_django', '/home/cityparks/webapps/actionmanual_django/lib/python2.6'] + sys.path
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'actionmanual.settings'
application = WSGIHandler()
