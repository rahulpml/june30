# Generated by Django 4.0.6 on 2022-07-16 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petrolpumpApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fueltype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fueltype', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Tanker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanker_no', models.IntegerField()),
                ('tanker_date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('tanker_des', models.TextField()),
                ('fueltype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='petrolpumpApp.fueltype')),
                ('supplier', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='petrolpumpApp.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_no', models.IntegerField()),
                ('company_name', models.CharField(max_length=255)),
                ('machine_des', models.TextField()),
                ('fueltype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='petrolpumpApp.fueltype')),
            ],
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('fueltype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='petrolpumpApp.fueltype')),
            ],
        ),
    ]