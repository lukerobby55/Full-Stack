# Generated by Django 5.1.6 on 2025-02-17 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('platform', models.CharField(choices=[('PS5', 'PlayStation 5'), ('XBOX', 'Xbox One'), ('SWITCH', 'Nintendo Switch'), ('PC', 'PC')], max_length=10)),
                ('genre', models.CharField(choices=[('SHOOTER', 'Shooter'), ('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('RPG', 'RPG'), ('SPORTS', 'Sports')], max_length=15)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
