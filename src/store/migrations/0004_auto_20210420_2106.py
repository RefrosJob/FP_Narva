# Generated by Django 3.1.7 on 2021-04-20 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210420_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imageMain',
            field=models.ImageField(default='img/norm_def.png', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagePreview',
            field=models.ImageField(default='img/small_def.png', upload_to='img/'),
        ),
    ]