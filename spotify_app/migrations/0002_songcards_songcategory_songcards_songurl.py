
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songcards',
            name='songCategory',
            field=models.CharField(default='Uncategorized', max_length=100),
        ),
        migrations.AddField(
            model_name='songcards',
            name='songURL',
            field=models.TextField(blank=True, null=True),
        ),
    ]
