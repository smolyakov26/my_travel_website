# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/d/doradogd/doradogd.beget.tech/public_html/website')
sys.path.insert(1, '/home/d/doradogd/doradogd.beget.tech/public_html/venv/lib/python3.9/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()