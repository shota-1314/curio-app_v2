# coding: utf-8

from rest_framework import serializers
import datetime
from .models import Live,Album,Track,News,Movie


class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    track = TrackSerializer()
    class Meta:
        model = Album
        fields = [
            'album_id',
            'title',
            'section',
            'degital',
            'releasedate',
            'price',
            'image',
            'apple_url',
            'spotify_url' ,
            'line_url',
            'url',
            'track',
        ]

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
