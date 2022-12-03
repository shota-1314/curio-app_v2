# coding: utf-8

from rest_framework import routers
from .views import LiveViewSet,AlbumViewSet,NewsViewSet,MovieViewSet

router = routers.DefaultRouter()
router.register(r'live', LiveViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'news', NewsViewSet)
router.register(r'movie', MovieViewSet)