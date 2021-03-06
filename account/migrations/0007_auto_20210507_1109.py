# Generated by Django 3.2 on 2021-05-07 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0006_auto_20210505_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='users/projects_icon/')),
                ('link', models.TextField(blank=True, null=True)),
                ('name_project', models.TextField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='role',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='GMT',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_reg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='interest',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tools',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='work_time',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/avatars/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(max_length=16, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
