
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_app', '0002_songcards_songcategory_songcards_songurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongGenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreName', models.TextField()),
                ('genreThumbnail', models.TextField()),
                ('genreColor', models.CharField(default='#358a6e', max_length=10)),
            ],
        ),
    ]
