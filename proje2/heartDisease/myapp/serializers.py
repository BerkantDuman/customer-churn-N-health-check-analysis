from myapp.models import Person, Values
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class ValuesSerializer(serializers.ModelSerializer):
    person = PersonSerializer(many=False, read_only=True)
    class Meta:
        model = Values
        fields = '__all__'