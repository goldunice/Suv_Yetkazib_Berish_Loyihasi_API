from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = "__all__"

    def validate_litr(self, qiymat):
        if qiymat > 19:
            raise ValidationError("Bunday katta litrlarda suv sotilmaydi")
        else:
            return qiymat


class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"

    def validate_qarz(self, qiymat):
        if qiymat > 500000:
            raise ValidationError("Qarzingiz juda ko’p, buyurtma qilolmaysiz!")
        else:
            return qiymat


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = "__all__"


class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"
