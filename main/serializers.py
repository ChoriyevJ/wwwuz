from rest_framework import serializers

from main import models


class MainListStatisticsSerializer(serializers.Serializer):

    sites_count = serializers.IntegerField()
    visitors_count = serializers.IntegerField()
    views_count = serializers.IntegerField()
    mobile_percentage = serializers.FloatField()


class SiteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Site
        fields = (
            'url',
            'title',
            'visitors_number',
            'views_number',
            'in_tasix',
        )


class CategorySerializer(serializers.ModelSerializer):

    is_new = serializers.BooleanField()

    class Meta:
        model = models.Category
        fields = (
            "title",
            "is_new",
        )


class IncreaseECommerceResourceSerializer(serializers.ModelSerializer):

    year = serializers.CharField()
    count = serializers.IntegerField()

    class Meta:
        model = models.Site
        fields = (
            'year',
            'count'
        )


class MainListOSDiagramSerializer(serializers.Serializer):

    windows = serializers.FloatField()
    android = serializers.FloatField()
    ios = serializers.FloatField()
    others = serializers.FloatField()


class MainListBrowserSerializer(serializers.Serializer):

    mobile_safari = serializers.FloatField()
    chrome = serializers.FloatField()
    chrome_mobile = serializers.FloatField()
    others = serializers.FloatField()


class MainListCategoryResourcesSerializer(serializers.ModelSerializer):

    resource_percentage = serializers.FloatField()

    class Meta:
        model = models.Category
        fields = (
            "title",
            "resource_percentage"
        )

