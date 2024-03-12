from django.db import models


class StatisticTypeChoice(models.TextChoices):
    VISITORS = 'Visitors'
    BROWSER = 'Browsers'
    PROVIDER = 'Providers'
    COUNTRY = 'Countries'
    OS = 'Operating systems'
    SCREEN_RES = 'Screens resolution'
    ENTRY_POINT = 'Entry points'
    EXIT_POINT = 'Exits points'
    SEARCH_ENGINE = 'Search engines'
    DEVICE = 'Devices'
