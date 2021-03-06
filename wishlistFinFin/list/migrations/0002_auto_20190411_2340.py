# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-04-11 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cartId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cover', models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/b/b9/No_Cover.jpg',
                                           max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SavedForLater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Cart')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Product')),
            ],
        ),
        migrations.AddField(
            model_name='cartitems',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Product'),
        ),
    ]
