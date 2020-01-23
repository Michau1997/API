import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Pytanie(models.Model):
    tekst_pytania = models.CharField(max_length=200)
    data_publikacji = models.DateField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.tekst_pytania

    def ostatnio_opublikowane(self):
        return self.data_publikacji >= \
            timezone.now() - datetime.timedelta(days=-1)

    class Meta:
        verbose_name = "Pytanie"
        verbose_name_plural = "Pytania"


class Odpowiedz(models.Model):
    pytanie = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    tekst_odpowiedzi = models.CharField(max_length=200)
    glosy = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.tekst_odpowiedzi

    class Meta:
        verbose_name = "Odpowiedź"
        verbose_name_plural = "Odpowiedzi"
