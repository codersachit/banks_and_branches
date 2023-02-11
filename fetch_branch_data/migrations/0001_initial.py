# Generated by Django 3.2.17 on 2023-02-11 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=49)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=11)),
                ('branch', models.CharField(max_length=74)),
                ('address', models.CharField(max_length=195)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fetch_branch_data.bank')),
            ],
        ),
    ]
