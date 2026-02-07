from rest_framework import serializers
from .models import TempInfoCollect
from datetime import date


class TempInfoCollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempInfoCollect
        fields = ["id","full_name","email","contact_number","skin_type","birthday","created_at","updated_at",]

    def validate(self, attrs):
        full_name = attrs.get("full_name")
        contact_number = attrs.get("contact_number")
        birthday = attrs.get("birthday")

        if full_name and len(full_name) < 3:
            raise serializers.ValidationError(
                {"full_name": "Full name must be at least 3 characters long"}
            )

        if contact_number is not None and contact_number.strip() == "":
            raise serializers.ValidationError(
                {"contact_number": "Contact number cannot be empty"}
            )

        if birthday and birthday > date.today():
            raise serializers.ValidationError(
                {"birthday": "Birthday cannot be a future date"}
            )

        return attrs

    def create(self, validated_data):
        instance = TempInfoCollect.objects.create(**validated_data)
        return instance
    
    def update(self, instance, validated_data):
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.email = validated_data.get("email", instance.email)
        instance.contact_number = validated_data.get("contact_number", instance.contact_number)
        instance.skin_type = validated_data.get("skin_type", instance.skin_type)
        instance.birthday = validated_data.get("birthday", instance.birthday)

        instance.save()
        return instance
