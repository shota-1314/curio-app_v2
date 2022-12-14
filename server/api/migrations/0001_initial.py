# Generated by Django 3.2.12 on 2022-12-03 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='アルバムID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='アルバムタイトル')),
                ('section', models.CharField(max_length=50, null=True, verbose_name='シングル/アルバム区分')),
                ('degital', models.BooleanField(default=True, verbose_name='デジタル配信フラグ')),
                ('releasedate', models.DateTimeField(null=True, verbose_name='発売日')),
                ('price', models.IntegerField(null=True, verbose_name='販売価格')),
                ('image', models.URLField(null=True, verbose_name='ジャケット写真')),
                ('apple_url', models.URLField(null=True, verbose_name='appleMusicURL')),
                ('spotify_url', models.URLField(null=True, verbose_name='spotifyURL')),
                ('line_url', models.URLField(null=True, verbose_name='LINEミュージック')),
                ('url', models.URLField(null=True, verbose_name='詳細url')),
            ],
        ),
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='ライブタイトル')),
                ('live_house_name', models.CharField(max_length=50, null=True, verbose_name='ライブハウス名')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='ライブハウス住所')),
                ('live_date', models.DateTimeField(null=True, verbose_name='ライブ日')),
                ('open_time', models.TimeField(null=True, verbose_name='開場時刻')),
                ('start_time', models.TimeField(null=True, verbose_name='開演時刻')),
                ('adv_price', models.IntegerField(null=True, verbose_name='前売り、取り置き料金')),
                ('door_price', models.IntegerField(null=True, verbose_name='当日料金')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='フライヤー写真')),
                ('url', models.URLField(null=True, verbose_name='詳細url')),
                ('detail', models.TextField(null=True, verbose_name='対バン等')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='タイトル')),
                ('post_date', models.DateTimeField(null=True, verbose_name='投稿日')),
                ('url', models.URLField(null=True, verbose_name='url')),
                ('thumbnail', models.URLField(null=True, verbose_name='サムネイル')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='タイトル')),
                ('news_date', models.DateTimeField(null=True, verbose_name='投稿日')),
                ('detail', models.TextField(null=True, verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_1', models.CharField(blank=True, max_length=50, null=True)),
                ('track_2', models.CharField(blank=True, max_length=50, null=True)),
                ('track_3', models.CharField(blank=True, max_length=50, null=True)),
                ('track_4', models.CharField(blank=True, max_length=50, null=True)),
                ('track_5', models.CharField(blank=True, max_length=50, null=True)),
                ('track_6', models.CharField(blank=True, max_length=50, null=True)),
                ('track_7', models.CharField(blank=True, max_length=50, null=True)),
                ('track_8', models.CharField(blank=True, max_length=50, null=True)),
                ('track_9', models.CharField(blank=True, max_length=50, null=True)),
                ('track_10', models.CharField(blank=True, max_length=50, null=True)),
                ('track_11', models.CharField(blank=True, max_length=50, null=True)),
                ('track_12', models.CharField(blank=True, max_length=50, null=True)),
                ('track_13', models.CharField(blank=True, max_length=50, null=True)),
                ('track_14', models.CharField(blank=True, max_length=50, null=True)),
                ('track_15', models.CharField(blank=True, max_length=50, null=True)),
                ('album_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.album')),
            ],
        ),
    ]
