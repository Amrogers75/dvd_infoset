from django.db import models

import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# Create your models here.


class DvdCas(Model):
    uu_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    title = columns.Text(required=False)
    sql_id = columns.Integer(required=False)


class DvdList(models.Model):
    dvd_title = models.CharField(max_length=255, null=True, blank=True)   
    released = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    rating = models.CharField(max_length=255, null=True, blank=True)
    genre = models.ForeignKey('main.Genre', null=True, blank=True)
    studio = models.ForeignKey('main.Studio', null=True, blank=True)

    # Year
    # Sound = models.FloatField(null=True, blank=True)
    # Versions
    # Aspect
    # UPC
    # DVD_ReleaseDate
    # Timestamp
    # ID

    def __unicode__(self):
        return self.dvd_title


class Genre(models.Model):
    genre = models.CharField(max_length=255, null=True, blank=True)


class Studio(models.Model):
    studio = models.CharField(max_length=255, null=True, blank=True)
