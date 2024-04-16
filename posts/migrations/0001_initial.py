# Generated by Django 5.0.1 on 2024-04-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('categories', models.CharField(choices=[('school', 'School'), ('national', 'National'), ('international', 'International'), ('opinion', 'Opinion'), ('feature', 'Feature')], default='school', max_length=15)),
                ('datetime', models.DateField(null=True)),
                ('slug', models.SlugField(default='')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=1)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]