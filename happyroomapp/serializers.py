from rest_framework import serializers
from . models import hrusers

class hruserSerializers(serializers.ModelSerializer):

    class Meta:
        model= hrusers
        fields= '__all__'