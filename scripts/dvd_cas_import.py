#!/usr/bin/env python

import csv
import sys
import os
from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import Dvd_List, Dvd_Cas

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "dvd.csv"

dvd_csv = os.path.join(dir_name, file_name)

csv_file = open(dvd_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:

    dvd_name = unidecode(row['DVD_Title'])

    print dvd_name

    dvd_name = unidecode(row['DVD_Title'])
    session = cluster.connect() 
    dvd = DvdCas(title=dvd_name)
    dvd.save()

    cluster.shutdown()