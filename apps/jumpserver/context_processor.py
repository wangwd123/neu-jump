# -*- coding: utf-8 -*-
#
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def jumpserver_processor(request):
    # Setting default pk
    context = {
        'DEFAULT_PK': '00000000-0000-0000-0000-000000000000',
        'LOGO_URL': static('img/logo.png'),
        'LOGO_TEXT_URL': static('img/logo_text.png'),
        'LOGIN_IMAGE_URL': static('img/login_image.png'),
        'FAVICON_URL': static('img/facio.ico'),
        'JMS_TITLE': 'Jumpserver',
        'VERSION': settings.VERSION,
        'COPYRIGHT': 'NEU安全堡垒机(基于 JumpServer 开发)',
        'SECURITY_COMMAND_EXECUTION': settings.SECURITY_COMMAND_EXECUTION,
        'SECURITY_MFA_VERIFY_TTL': settings.SECURITY_MFA_VERIFY_TTL,
    }
    return context



