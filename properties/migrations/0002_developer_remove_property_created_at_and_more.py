# Generated by Django 5.1.1 on 2024-09-27 21:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('founded_year', models.IntegerField()),
                ('website', models.URLField(blank=True, null=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='property',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='property',
            name='price',
        ),
        migrations.RemoveField(
            model_name='property',
            name='title',
        ),
        migrations.AddField(
            model_name='property',
            name='ceiling_height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='property',
            name='completion_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='construction_class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='finishing',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='metro_station',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='property',
            name='number_of_blocks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='number_of_floors',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='parking',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='price_from',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='price_per_sqm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='total_flats',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='transport_time_to_metro',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='walking_time_to_metro',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='developer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='properties.developer'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('developer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='developer_reviews', to='properties.developer')),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_reviews', to='properties.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
