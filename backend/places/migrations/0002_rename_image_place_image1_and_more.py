# Generated by Django 4.2.5 on 2023-10-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='image',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='top_deal',
            new_name='top_places',
        ),
        migrations.AddField(
            model_name='place',
            name='image2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media/places'),
        ),
        migrations.AddField(
            model_name='place',
            name='image3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media/places'),
        ),
        migrations.AddField(
            model_name='place',
            name='image4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media/places'),
        ),
        migrations.AddField(
            model_name='place',
            name='image5',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media/places'),
        ),
    ]
