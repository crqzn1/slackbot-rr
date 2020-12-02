#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import configparser

def main():
    # Allow invoking manage.py from any directory
    repo_dir = os.path.dirname(os.path.realpath(__file__))

    # Load env variables from .env config file
    cp = configparser.ConfigParser(interpolation=None)
    cp.read(os.path.join(repo_dir, ".env"))

    # Load the files variables into the environment
    for i in cp.items('django'):
        os.environ[i[0]] = i[1]

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dimebot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
