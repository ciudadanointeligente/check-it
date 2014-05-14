from django.template.loaders.app_directories import Loader
from django.conf import settings
import os
from constance import config

class ThemeLoader(Loader):
    def get_template_sources(self, template_name, template_dirs=None):
        template_name = os.path.join(config.CURRENT_THEME, template_name)
        return super(ThemeLoader, self).get_template_sources(template_name, template_dirs)

