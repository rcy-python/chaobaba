from rest_framework.serializers import ModelSerializer

from home.models import Banner, Nav


class BannerModelSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = ("img", "link", "title")


class HeaderFooterModelSerializer(ModelSerializer):
    class Meta:
        model = Nav
        fields = ( "link", "title")