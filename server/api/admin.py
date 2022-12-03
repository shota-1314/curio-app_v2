from django.contrib import admin


from .models import Live,Album,Track,News,Movie


@admin.register(Live)
class LiveAdmin(admin.ModelAdmin):
    pass
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    pass
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass