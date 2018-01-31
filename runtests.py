#!/usr/bin/env python

import os
import sys


def run():
    import django
    from django.conf import settings
    from django.core.management import execute_from_command_line

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enumchoicefield.tests.settings')
    execute_from_command_line([sys.argv[0], 'test'] + sys.argv[1:])


if __name__ == '__main__':
    run()
