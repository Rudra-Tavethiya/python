from rest_framework import serializers
from myapp.models import * 



class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
        # fields = ["id","name"]
        # exclude = ["name"]

class empserializer(serializers.ModelSerializer):
    class Meta:
        model = emp
        fields = '__all__'

class productserializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'