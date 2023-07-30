from rest_framework import serializers
from .models import Thing,Post

class ThingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thing
        fields =['id','owner', 'name', 'desc']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'