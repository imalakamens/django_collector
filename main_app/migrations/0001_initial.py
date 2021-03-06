# Generated by Django 3.0.8 on 2020-09-18 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.CharField(max_length=50, verbose_name='reviewer')),
                ('rating', models.CharField(choices=[('1', '1/5 - Not so good...'), ('2', '2/5 - Could be better'), ('3', '3/5 - It was alright'), ('4', '4/5 - Pretty good...'), ('5', '5/5 - AMAZING!')], default='3', max_length=1)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Record')),
            ],
        ),
    ]
