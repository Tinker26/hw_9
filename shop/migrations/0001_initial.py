# Generated by Django 3.2.8 on 2021-10-31 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Krasofkalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('image', models.CharField(max_length=400)),
                ('price', models.IntegerField()),
                ('old_price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]