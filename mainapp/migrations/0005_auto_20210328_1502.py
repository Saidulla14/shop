# Generated by Django 3.1.7 on 2021-03-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210328_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличия SD карты'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volune_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный обЪем встроенный памяти'),
        ),
    ]
