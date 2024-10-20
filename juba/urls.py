from django.urls import path

from juba import views

urlpatterns = [
    path("slider/", views.SliderPageListAPIView.as_view(), name="slider"),
    path("keys/", views.OURKeysAPIView.as_view(), name="keys"),
    path("solo-main/", views.StaticSoloAPIView.as_view(), name="solo-main"),
    path("result/", views.ResultNumberAPIView.as_view(), name="result"),
    path("client-photo/", views.StaticClientPhotoAPIView.as_view(), name="client"),
    path("team-photo/", views.StaticTeamPhotoAPIView.as_view(), name="team"),
    path("our-contact/", views.OurContactAPIView.as_view(), name="our-contact"),
    path("contact-user/", views.ContactClientAPIView.as_view(), name="contact"),
    path("service/", views.ServiceHomePageAPIView.as_view(), name="service"),
    path("service/solo/<int:service_id>/", views.ServiceDetailSoloAPIView.as_view(), name="service-solo"),
    path("service/pricing/<int:service_id>/", views.ServicePricingAPIView.as_view(), name="service"),
]
