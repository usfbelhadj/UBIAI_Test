from rest_framework import serializers
from annotated.models import Annotated

class AnnoSeri(serializers.ModelSerializer):
    class Meta:
        model = Annotated
        fields = ["text", "annotations"]
