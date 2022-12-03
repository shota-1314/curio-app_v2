from django.db import models

# ライブハウス一覧
class Live(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=50,null=True,verbose_name='ライブタイトル')
    live_house_name = models.CharField(max_length=50,null=True,verbose_name='ライブハウス名')
    address = models.CharField(max_length=50,null=True,verbose_name='ライブハウス住所')
    live_date = models.DateTimeField(editable=True,null=True,verbose_name='ライブ日')
    open_time = models.TimeField(editable=True,null=True,verbose_name='開場時刻')
    start_time = models.TimeField(editable=True,null=True,verbose_name='開演時刻')
    adv_price = models.IntegerField(null=True,verbose_name='前売り、取り置き料金')
    door_price = models.IntegerField(null=True,verbose_name='当日料金')
    image = models.ImageField(upload_to='images/', null=True,verbose_name='フライヤー写真')
    url = models.URLField(editable=True, null=True,verbose_name='詳細url')
    detail = models.TextField(editable=True, null=True,verbose_name='対バン等')

# アルバム一覧
class Album(models.Model):
    album_id = models.CharField(max_length=10, primary_key=True,verbose_name='アルバムID')
    title = models.CharField(max_length=50,null=True,verbose_name='アルバムタイトル')
    section = models.CharField(max_length=50,null=True,verbose_name='シングル/アルバム区分')
    degital = models.BooleanField(default=True,verbose_name='デジタル配信フラグ')
    releasedate = models.DateTimeField(editable=True,null=True,verbose_name='発売日')
    price = models.IntegerField(null=True,verbose_name='販売価格')
    image = models.URLField(editable=True, null=True,verbose_name='ジャケット写真')
    apple_url = models.URLField(editable=True, null=True,verbose_name='appleMusicURL')
    spotify_url = models.URLField(editable=True, null=True,verbose_name='spotifyURL')
    line_url = models.URLField(editable=True, null=True,verbose_name='LINEミュージック')
    url = models.URLField(editable=True, null=True,verbose_name='詳細url')


# アルバムの曲一覧
class Track(models.Model):
    # アルバムID
    album_id = models.OneToOneField(Album, on_delete=models.CASCADE)
    # 曲一覧
    track_1 = models.CharField(max_length=50,null=True, blank=True)
    track_2 = models.CharField(max_length=50,null=True, blank=True)
    track_3 = models.CharField(max_length=50,null=True, blank=True)
    track_4 = models.CharField(max_length=50,null=True, blank=True)
    track_5 = models.CharField(max_length=50,null=True, blank=True)
    track_6 = models.CharField(max_length=50,null=True, blank=True)
    track_7 = models.CharField(max_length=50,null=True, blank=True)
    track_8 = models.CharField(max_length=50,null=True, blank=True)
    track_9 = models.CharField(max_length=50,null=True, blank=True)
    track_10 = models.CharField(max_length=50,null=True, blank=True)
    track_11 = models.CharField(max_length=50,null=True, blank=True)
    track_12 = models.CharField(max_length=50,null=True, blank=True)
    track_13 = models.CharField(max_length=50,null=True, blank=True)
    track_14 = models.CharField(max_length=50,null=True, blank=True)
    track_15 = models.CharField(max_length=50,null=True, blank=True)

# ニュース一覧
class News(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100,null=True,verbose_name='タイトル')
    news_date = models.DateTimeField(editable=True,null=True,verbose_name='投稿日')
    detail = models.TextField(editable=True, null=True,verbose_name='内容')

# 動画一覧
class Movie(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100,null=True,verbose_name='タイトル')
    post_date = models.DateTimeField(editable=True,null=True,verbose_name='投稿日')
    url = models.URLField(editable=True, null=True,verbose_name='url')
    thumbnail = models.URLField(editable=True, null=True,verbose_name='サムネイル')
    

