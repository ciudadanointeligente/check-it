from django.template.loaders.app_directories import Loader
from django.conf import settings
import os
from constance import config
from django.utils import six
import sys
from django.utils.importlib import import_module



#this changes in the newer versions of django
#so I need to fix this
if six.PY2:
    fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()


def return_dir(mod, extra_dir=""):
    template_dir = os.path.join(os.path.dirname(mod.__file__), extra_dir, 'templates')
    if os.path.isdir(template_dir):
        if six.PY2:
            template_dir = template_dir.decode(fs_encoding)
    else:
        template_dir = None

    return template_dir


app_template_dirs = []
themes_dirs = {}
for app in settings.INSTALLED_APPS:
    try:
        mod = import_module(app)
    except ImportError as e:
        raise ImproperlyConfigured('ImportError %s: %s' % (app, e.args[0]))

    # At this exact moment it is asked if the current module
    # has an attribute called PROMISES_THEMES
    # which is intended to detect if has themes or not
    # I think it's pretty hacky but it is working
    extra_dir = []
    if hasattr(mod, 'PROMISES_THEMES'):
        extra_dirs = mod.PROMISES_THEMES
        for extra_dir in extra_dirs:
            template_dir = return_dir(mod, extra_dir)
            if template_dir:
               themes_dirs[extra_dir] = template_dir


    template_dir = return_dir(mod)
    if template_dir:
        app_template_dirs.append(template_dir)

# It won't change, so convert it to a tuple to save memory.
app_template_dirs = tuple(app_template_dirs)


class ThemeLoader(Loader):
    def load_template_source(self, template_name, template_dirs=None):
        if not template_dirs:
            template_dirs = app_template_dirs
        if config.CURRENT_THEME and config.CURRENT_THEME in themes_dirs:
            template_dirs = (themes_dirs[config.CURRENT_THEME], ) + template_dirs
        return super(ThemeLoader, self).load_template_source(template_name, template_dirs)

