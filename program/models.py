from django.db import models

from django.urls import reverse


class Abies(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    instagram = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Abi'
        verbose_name_plural = 'Abies'


class Event(models.Model):
    title = models.CharField("Name of Program", max_length=200)
    description = models.CharField("Abi and Group", max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title}</a>'

