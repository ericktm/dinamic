from django.db import models


class Contact(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)

    def __unicode__(self):
        return self.name.capitalize()