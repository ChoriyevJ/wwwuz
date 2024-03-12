from django.utils import timezone

from django.db import models
from django.utils.text import slugify

from utils.models import BaseModel
from main.managers import CustomManager
from main.choices import StatisticTypeChoice


class Category(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Site(BaseModel):

    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    in_tasix = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)
    visitors_number = models.PositiveIntegerField(default=0)
    views_number = models.PositiveIntegerField(default=0)

    categories = models.ManyToManyField(Category, related_name="sites")
    test_date = models.DateField(default=timezone.now())

    objects = models.Manager()
    customs = CustomManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Statistic(BaseModel):

    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    statistic_type = models.CharField(max_length=31, choices=StatisticTypeChoice.choices)
    title = models.CharField(max_length=255)
    extra = models.CharField(max_length=31, blank=True, null=True)

    visitors_number = models.PositiveIntegerField(default=0)
    visitors_tas_ix = models.PositiveIntegerField(default=0, blank=True, null=True)

    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField()

    def __str__(self):
        return self.statistic_type


"""
class VisitorsStatistic(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE,
                             related_name='date_statistics')
    visitors_number = models.PositiveIntegerField(default=0)
    visitors_tas_ix = models.PositiveIntegerField(default=0)
    date = models.DateField()


class BrowserStatistic(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE,
                             related_name="browser_statistics")
    browser = models.CharField(max_length=63, blank=True, null=True)
    version = models.CharField(max_length=31, blank=True, null=True)
    visitors = models.CharField(default=0)
    date = models.DateField()


class ProviderStatistic(BaseModel):

    site = models.ForeignKey(Site, on_delete=models.CASCADE,
                             related_name="providers")
    provider = models.CharField(max_length=63, blank=True, null=True)
    visitors_number = models.PositiveIntegerField(default=0)
    date = models.DateField()


class CountryStatistic(BaseModel):

    site = models.ForeignKey(Site, on_delete=models.CASCADE,
                             related_name="countries")
    country = models.CharField(max_length=255)
    visitors_number = models.PositiveIntegerField(default=0)
    date = models.DateField()


class OSStatistic(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE,
                             related_name="countries")
    os = models.CharField(max_length=255)
    version = models.CharField(max_length=31)
    visitors_number = models.PositiveIntegerField(default=0)
    date = models.DateField()


class ScreenResolutionStatistic(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE,
                             related_name="countries")
    screen = models.CharField(max_length=255)
    visitors_number = models.PositiveIntegerField(default=0)
    date = models.DateField()


class UserPointsStatistic(BaseModel):

    class PointTypeChoice(models.TextChoices):
        ENTRY = 'Entry'
        EXIT = 'Exit'

    site = models.ForeignKey(Site, on_delete=models.CASCADE,
                             related_name="points")
    point = models.CharField(max_length=511)
    point_type = models.CharField(max_length=15, choices=PointTypeChoice.choices)
    visitors_number = models.PositiveIntegerField(default=0)


class SearchEngineStatistic(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE,
                             related_name="points")
    search_engine = models.CharField(max_length=511)
    visitors_number = models.PositiveIntegerField(default=0)
    date = models.DateField()

"""




