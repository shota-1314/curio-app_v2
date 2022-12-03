from django.shortcuts import render
import datetime
# coding: utf-8

import django_filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Live,Album,News,Movie
from .serializer import LiveSerializer,AlbumSerializer,NewsSerializer,MovieSerializer


class LiveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Live.objects.order_by('-live_date')
    serializer_class = LiveSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    """アルバム情報を取得"""
    queryset = Album.objects.order_by('-releasedate')
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    """ニュース情報を取得"""
    queryset = News.objects.order_by('-news_date')
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """動画情報を取得"""
    queryset = Movie.objects.order_by('-post_date')
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)