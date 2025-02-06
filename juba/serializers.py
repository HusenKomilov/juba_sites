from rest_framework import serializers

from juba import models


class MainSoloAdmin(serializers.ModelSerializer):
    class Meta:
        model = models.Slider
        fields = ("id", "title", "short_description", "photo")


class HashtagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hashtags
        fields = ("id", "title")


class OurKeysSerializer(serializers.ModelSerializer):
    service = serializers.StringRelatedField()
    hashtags = HashtagsSerializer(many=True, read_only=True)

    class Meta:
        model = models.OurKeys
        fields = ("id", "title", "photo", "url", "service", "hashtags")


class StaticSoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StaticSolo
        fields = ("id", "photo", "description")


class ResultNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResultNumber
        fields = ("id", "title", "result")


class StaticPhotoClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StaticPhoto
        fields = ("id", "photo_type", "photo")


class StaticPhotoTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StaticPhoto
        fields = ("id", "username", "job_title", "photo_type", "photo", "background_image")


class OurContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = (
            "id", "phone_number", "longitude", "latitude", "email", "telegram_url", "instagram_url", "facebook_url")


class ContactUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUser
        fields = ("id", "name", "phone_number")


class ServiceHomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Services
        fields = ("id", "title", "short_description")


class ServiceDetailSoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceDetailSolo
        fields = ("id", "description", "photo")


class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pricing
        fields = ("id", "title", "price", "description")


class ServiceTypeTopSerializer(serializers.ModelSerializer):
    services = serializers.StringRelatedField()

    class Meta:
        model = models.ServiceType
        fields = ("id", "title", "services", "description", "is_top")


class ServiceTypeBottomSerializer(serializers.ModelSerializer):
    services = serializers.StringRelatedField()

    class Meta:
        model = models.ServiceType
        fields = ("id", "title", "services", "description", "photo", "is_top")


class ServiceDetailShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Services
        fields = ("id", "detail_title", "detail_description")


class WorksServiceSerializer(serializers.ModelSerializer):
    services = serializers.StringRelatedField()

    class Meta:
        model = models.Works
        fields = ("id", "short_description", "services", "photo")


class SEOTextSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = models.SEOText
        fields = (
            "id",
            "title",
            "description",
            "keywords",
            "slug",
            "image"
        )

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
