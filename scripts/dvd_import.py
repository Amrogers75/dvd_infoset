#!/usr/bin/env python

import csv
import sys
import os
from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

#easy to forget, but fixes most things!!
import django
django.setup()

from main.models import DvdList, DvdCas, Genre, Studio

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster


print os.path.abspath(__file__)

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "dvd.csv"

dvd_csv = os.path.join(dir_name, file_name)

csv_file = open(dvd_csv, 'r')

reader = csv.DictReader(csv_file)


cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace('dvdjango7')

for row in reader:

    print row['DVD_Title']

    new_genre, created = Genre.objects.get_or_create(genre=row['Genre'])
    new_studio, created = Studio.objects.get_or_create(studio=row['Studio'])

    new_dvd, created = DvdList.objects.get_or_create(dvd_title=unidecode(row['DVD_Title']))
    new_dvd.price = row['Price']
    new_dvd.status = row['Status']
    new_dvd.rating = row['Rating']   
    new_dvd.releas = row['Released']

    new_dvd.genre = new_genre
    new_dvd.studio = new_studio

    new_dvd.save()

    cas_dvd = DvdCas(title=unidecode(row['DVD_Title']), sql_id=new_dvd.id)
    cas_dvd.save()


cluster.shutdown()
