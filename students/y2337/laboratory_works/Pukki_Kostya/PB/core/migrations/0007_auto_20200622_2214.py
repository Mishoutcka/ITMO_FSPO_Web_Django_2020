# Generated by Django 3.0.5 on 2020-06-22 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('index', models.IntegerField()),
                ('board', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('index', models.IntegerField()),
                ('panel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Panel')),
            ],
        ),
    ]