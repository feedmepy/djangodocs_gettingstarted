# Generated by Django 2.1.7 on 2019-02-14 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('relationship_status', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
            ],
        ),
    ]
