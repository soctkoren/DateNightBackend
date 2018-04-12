# Generated by Django 2.0.2 on 2018-04-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datenight_backend', '0003_auto_20180412_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=280)),
                ('is_hidden', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DestinationNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to='imgs/')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.SmallIntegerField()),
                ('is_hidden', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TravelNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_method', models.TextField()),
            ],
        ),
    ]
