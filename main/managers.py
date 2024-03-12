
from django.db import models

from main.choices import StatisticTypeChoice


class CustomManager(models.Manager):

    def os_statistic(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            statistic__statistic_type=StatisticTypeChoice.OS
        )
        return queryset

    def browser_statistic(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            statistic__statistic_type=StatisticTypeChoice.BROWSER
        )
        return queryset




