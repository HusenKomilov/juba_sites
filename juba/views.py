from rest_framework import generics

from juba import models, serializers, choices


class SliderPageListAPIView(generics.ListAPIView):
    queryset = models.Slider.objects.all()
    serializer_class = serializers.MainSoloAdmin


class OURKeysAPIView(generics.ListAPIView):
    queryset = models.OurKeys.objects.all().select_related("service").prefetch_related("hashtags")
    serializer_class = serializers.OurKeysSerializer


class StaticSoloAPIView(generics.ListAPIView):
    queryset = models.StaticSolo.objects.all()
    serializer_class = serializers.StaticSoloSerializer


class ResultNumberAPIView(generics.ListAPIView):
    queryset = models.ResultNumber.objects.all()
    serializer_class = serializers.ResultNumberSerializer


class StaticClientPhotoAPIView(generics.ListAPIView):
    queryset = models.StaticPhoto.objects.filter(photo_type=choices.PhotoTypeChoices.CLIENTS)
    serializer_class = serializers.StaticPhotoClientSerializer


class StaticTeamPhotoAPIView(generics.ListAPIView):
    queryset = models.StaticPhoto.objects.filter(photo_type=choices.PhotoTypeChoices.TEAMS)
    serializer_class = serializers.StaticPhotoTeamSerializer


class OurContactAPIView(generics.ListAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.OurContactSerializer


class ContactClientAPIView(generics.CreateAPIView):
    queryset = models.ContactUser.objects.all()
    serializer_class = serializers.ContactUserSerializer


class ServiceHomePageAPIView(generics.ListAPIView):
    queryset = models.Services.objects.all()
    serializer_class = serializers.ServiceHomePageSerializer


class ServiceDetailSoloAPIView(generics.ListAPIView):
    queryset = models.ServiceDetailSolo.objects.all().select_related("service")
    serializer_class = serializers.ServiceDetailSoloSerializer

    def get_queryset(self):
        service_id = self.kwargs.get("service_id")
        return self.queryset.filter(service_id=service_id)


class ServicePricingAPIView(generics.ListAPIView):
    queryset = models.Pricing.objects.all().select_related("service")
    serializer_class = serializers.PricingSerializer

    def get_queryset(self):
        service_id = self.kwargs.get("service_id")
        return self.queryset.filter(service_id=service_id)


class ServiceTypeTopAPIView(generics.ListAPIView):
    queryset = models.ServiceType.objects.filter(is_top=True).order_by("index").select_related("services")
    serializer_class = serializers.ServiceTypeTopSerializer


class ServiceTypeBottomAPIView(generics.ListAPIView):
    queryset = models.ServiceType.objects.filter(is_top=False).select_related("services")
    serializer_class = serializers.ServiceTypeBottomSerializer

    def get_queryset(self):
        service_id = self.kwargs.get("service_id")
        return self.queryset.filter(services=service_id)


class ServiceKeysAPIView(generics.ListAPIView):
    queryset = models.OurKeys.objects.all().select_related("service").prefetch_related("hashtags")
    serializer_class = serializers.OurKeysSerializer

    def get_queryset(self):
        service_id = self.kwargs.get("service_id")
        return self.queryset.filter(service_id=service_id)


class ServiceDetailShortAPIView(generics.ListAPIView):
    queryset = models.Services.objects.all()
    serializer_class = serializers.ServiceDetailShortSerializer

    def get_queryset(self):
        service_id = self.kwargs.get("service_id")
        return self.queryset.filter(id=service_id)


class WorksAPIView(generics.ListAPIView):
    queryset = models.Works.objects.all().select_related("services")
    serializer_class = serializers.WorksServiceSerializer

    def get_queryset(self):
        service_id = self.kwargs.get("service_id")
        return self.queryset.filter(services_id=service_id)
