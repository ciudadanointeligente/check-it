#!/usr/bin/env python
from django.core.management import call_command
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deldichoalhecho_site.settings")
call_command('test', 'deldichoalhecho', verbosity=1)

