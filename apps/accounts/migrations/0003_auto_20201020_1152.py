# Generated by Django 3.1.2 on 2020-10-20 11:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('representatives', '0001_initial'),
        ('accounts', '0002_auto_20201020_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailuser',
            options={'ordering': ('first_name', 'last_name')},
        ),
        migrations.AddField(
            model_name='emailuser',
            name='representative',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='representatives.representative'),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
