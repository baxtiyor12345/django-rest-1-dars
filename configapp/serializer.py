from rest_framework import serializers
from .models import *

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Movie
#         fields='__all__'

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actors
        fields='__all__'

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=200)
    slug=serializers.SlugField(read_only=True)
    year=serializers.IntegerField()
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actors.objects.all())
    genre=serializers.CharField()


    def create(self, validated_data):
        actors_data = validated_data.pop('actors')
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors_data)
        return movie

