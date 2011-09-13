#!/usr/bin/python
import os, site, sys


# Tell wsgi to add the Python site-packages to it's path.
site.addsitedir('/home/progressnow/.virtualenvs/production/lib/python2.7/site-packages')

# Fix markdown.py (and potentially others) using stdout
sys.stdout = sys.stderr

root = os.path.dirname(__file__)
project = os.path.join(root, 'gfcactivatingland')
workspace = os.path.dirname(project)
sys.path.append(workspace)

os.environ['DJANGO_SETTINGS_MODULE'] = 'gfcactivatingland.settings'
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()