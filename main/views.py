from django.shortcuts import render
from django.db import models
from django.utils import timezone
from django.utils.timezone import timedelta

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db import models
from django.db.models import functions

from main.models import Category, Site, Statistic
from main.choices import StatisticTypeChoice
from main import serializers


class MainListStatisticsAPI(APIView):

    def get(self, request):
        statistics = Site.objects.aggregate(
            sites_count=models.Count("pk", distinct=True),
            visitors_count=functions.Coalesce(models.Sum("visitors_number"), 0),
            views_count=functions.Coalesce(models.Sum("views_number"), 0),
            mobile_count=functions.Coalesce(
                models.Count(
                    "statistic__pk", filter=models.Q(
                        statistic__statistic_type=StatisticTypeChoice.DEVICE
                    ) & models.Q(statistic__title__icontains="mobile"), distinct=True
                ), 0
            ),
            mobile_percentage=models.F("mobile_count") * 100 / models.F("sites_count"),

        )

        serializer = serializers.MainListStatisticsSerializer(
            data={
                "sites_count": statistics['sites_count'],
                "visitors_count": statistics['visitors_count'],
                "views_count": statistics['views_count'],
                "mobile_percentage": statistics["mobile_percentage"]
            }
        )
        serializer.is_valid()
        return Response(serializer.data)


class SiteListAPI(generics.ListAPIView):
    queryset = Site.objects.all().order_by(
        "-visitors_number"
    )
    serializer_class = serializers.SiteListSerializer


class MainListCategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all().annotate(
        is_new=models.Case(
            models.When(
                created_at__gt=timezone.now() - timedelta(days=2),
                then=True
            ),
            default=False,
            output_field=models.BooleanField()
        )
    )
    serializer_class = serializers.CategorySerializer


class IncreaseECommerceResourceAPI(APIView):

    def get(self, request):

        queryset = Site.objects.filter(
            categories__code="e_commerce"
        ).annotate(
            year=functions.ExtractYear('test_date')
        ).values('year').annotate(
            count=models.Count(
                'year'
            )
        )
        serializer = serializers.IncreaseECommerceResourceSerializer(data=queryset, many=True)
        serializer.is_valid()

        return Response(serializer.data)


class MainListOSStatisticsAPI(APIView):

    def get(self, request):
        data = dict()
        counts = Site.customs.os_statistic().aggregate(
            all=functions.Coalesce(
                models.Count(
                    'pk', distinct=True
                ), 0

            ),
            windows=functions.Coalesce(
                models.Count(
                    'pk', distinct=True,
                    filter=models.Q(statistic__title__icontains="windows")
                ), 0
            ),
            android=functions.Coalesce(
                models.Count(
                    'pk', distinct=True,
                    filter=models.Q(statistic__title__icontains="android")
                ), 0
            ),
            ios=functions.Coalesce(
                models.Count(
                    'pk', distinct=True,
                    filter=models.Q(statistic__title__icontains="ios")
                ), 0
            ),
            others=models.F("all") - models.F("windows") - models.F("android") - models.F("ios")
        )
        try:
            data['windows'] = counts['windows'] * 100 / counts['all']
            data['android'] = counts['android'] * 100 / counts['all']
            data['ios'] = counts['ios'] * 100 / counts['all']
            data['others'] = counts['others'] * 100 / counts['all']

        except ZeroDivisionError:
            data['windows'] = counts['windows']
            data['android'] = counts['android']
            data['ios'] = counts['ios']
            data['others'] = counts['others']

        serializer = serializers.MainListOSDiagramSerializer(data=data)
        serializer.is_valid()

        return Response(serializer.data)


class MainListBrowserStatisticsAPI(APIView):

    def get(self, request):
        data = dict()
        counts = Site.customs.browser_statistic().aggregate(
            all=functions.Coalesce(
                models.Count(
                    'pk', distinct=True
                ), 0

            ),
            mobile_safari=functions.Coalesce(
                models.Count(
                    'pk', distinct=True,
                    filter=models.Q(statistic__title__icontains="mobile safari")
                ), 0
            ),
            chrome=functions.Coalesce(
                models.Count(
                    'pk', distinct=True,
                    filter=models.Q(statistic__title__icontains="chrome")
                ), 0
            ),
            chrome_mobile=functions.Coalesce(
                models.Count(
                    'pk', distinct=True,
                    filter=models.Q(statistic__title__icontains="chrome mobile")
                ), 0
            ),
            others=models.F("all") - models.F("mobile_safari") - models.F("chrome") - models.F("chrome_mobile")
        )

        try:
            data['mobile_safari'] = counts['mobile_safari'] * 100 / counts['all']
            data['chrome'] = counts['chrome'] * 100 / counts['all']
            data['chrome_mobile'] = counts['chrome_mobile'] * 100 / counts['all']
            data['others'] = counts['others'] * 100 / counts['all']

        except ZeroDivisionError:
            data['mobile_safari'] = counts['mobile_safari']
            data['chrome'] = counts['chrome']
            data['chrome_mobile'] = counts['chrome_mobile']
            data['others'] = counts['others']

        serializer = serializers.MainListOSDiagramSerializer(data=data)
        serializer.is_valid()


class MainListResourceStatisticsAPI(APIView):

    def get(self, request):
        resources_count = Site.objects.all().count()
        counts = Category.objects.annotate(
            resources=models.Count(
                "sites"
            ),
            resource_percentage=models.F("resources") * 100 / resources_count
        ).values("title", "resources")




