#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django
import csv


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JobSatellite.settings')
    django.setup()
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

from recommend.models import jobdict
CSV_PATH=r'C:\Users\네리\Desktop\sba_re\4조\job_dict_final.csv'
with open(CSV_PATH,newline='',encoding="utf-8")as csvfile:
    data_reader=csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        jobdict.objects.create(job=row['job'],skill=row['skill'])
