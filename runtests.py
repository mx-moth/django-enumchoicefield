#!/usr/bin/env python

import os
import sys


def run():
    import django
    from django.conf import settings
    from django.core.management import execute_from_command_line

    settings.configure(
        DATABASES={'default': {
            'NAME': ':memory:',
            'ENGINE': 'django.db.backends.sqlite3'}},
        INSTALLED_APPS=['enumchoicefield', 'enumchoicefield.tests'])
    django.setup()
    execute_from_command_line([sys.argv[0], 'test'] + sys.argv[1:])


if __name__ == '__main__':
    run()
