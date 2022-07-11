from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

now = timezone.now()


# Create your models here.
class ConcertDate(models.Model):
    date = models.DateField(default=now.date())

    def __str__(self):
        return str(self.date)


class Movement(models.Model):
    movement_ID = models.CharField(max_length=20, primary_key=True)
    movement_Number = models.IntegerField()
    movement_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.movement_Name


class Composition(models.Model):
    composition_ID = models.AutoField(primary_key=True)
    composer_Name = models.CharField(max_length=20)
    composition_Name = models.CharField(max_length=20)
    movement_ID = models.ForeignKey(Movement, on_delete=models.CASCADE, blank=True, default=None, null=True)
    date_Last_Performed = models.DateField()

    def __str__(self):
        return self.composition_Name


class Conductor(models.Model):
    conductor_ID = models.AutoField(primary_key=True)
    conductor_Name = models.CharField(max_length=20)

    # concerts = models.ManyToManyField(Concert, blank=True, null=True, default=None)

    def __str__(self):
        return self.conductor_Name


class Concert(models.Model):
    compositions = models.ManyToManyField(Composition)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, blank=True, null=True)
    concert_Date = models.ForeignKey(ConcertDate, on_delete=models.CASCADE)
    time = models.TimeField(default=now.time())

    def get_compositions(self):
        return self.compositions.all()

    def __str__(self):
        return str(self.concert_Date)


class ConcertSeason(models.Model):
    opening_date = models.DateField(default=now.date())
    concerts = models.ManyToManyField(Concert)

    def __str__(self):
        return self.opening_date


class Soloist(models.Model):
    soloist_ID = models.AutoField(primary_key=True)
    soloist_Name = models.CharField(max_length=20)
    compositions = models.ManyToManyField(Composition, blank=True, default=None)

    def get_compositions(self):
        return self.compositions.all()

    def __str__(self):
        return self.soloist_Name


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return str(self.user) + " | " + str(self.concert)
