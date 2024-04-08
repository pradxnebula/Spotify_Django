
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_app', '0003_songgenres'),
    ]

    operations = [
        migrations.CreateModel(
            name='trendingGenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreName', models.TextField()),
                ('genreThumbnail', models.TextField()),
            ],
        ),
    ]
