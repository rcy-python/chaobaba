from rest_framework.generics import ListAPIView


from home.models import Banner,Nav
from home.serializers import BannerModelSerializer, HeaderFooterModelSerializer


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = BannerModelSerializer

class HeaderListAPIview(ListAPIView):
    queryset = Nav.objects.filter(is_delete=False,is_show=True,position=1).order_by('orders')
    serializer_class = HeaderFooterModelSerializer

class FooterListAPIview(ListAPIView):
    queryset = Nav.objects.filter(is_delete=False,is_show=True,position=2).order_by('orders')
    serializer_class = HeaderFooterModelSerializer