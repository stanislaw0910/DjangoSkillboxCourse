# Generated by Django 4.0.2 on 2022-02-22 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0004_alter_advertisement_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisement.author'),
        ),
    ]
