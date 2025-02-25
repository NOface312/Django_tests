# Generated by Django 2.2.5 on 2019-10-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_tests', '0003_auto_20191005_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('comedy', 'Comedy'), ('tragedy', 'Tragedy'), ('drama', 'Drama')], max_length=50),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='models_tests.Publication')),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
    ]
