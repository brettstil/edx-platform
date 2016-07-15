# aws_appsembler.py

from .aws import *
from .appsembler import *

INSTALLED_APPS += ('appsembler',)
DEFAULT_TEMPLATE_ENGINE['OPTIONS']['context_processors'] += ('appsembler.context_processors.intercom',)

SEARCH_SKIP_ENROLLMENT_START_DATE_FILTERING = True

#enable course visibility feature flags
COURSE_CATALOG_VISIBILITY_PERMISSION = 'see_in_catalog'
COURSE_ABOUT_VISIBILITY_PERMISSION = 'see_about_page'

INSTALLED_APPS += ('hr_management',)

# set media values for SCORM upload
MEDIA_ROOT = '/edx/var/edxapp/media'
MEDIA_URL = '/media/'
