# Generated by Django 3.2 on 2021-04-22 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cathegory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cathegoryName', models.CharField(default='Cathegory Template', max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.JSONField(default={'attribute template': 'value'}, null=True, verbose_name='Attributes'),
        ),
        migrations.CreateModel(
            name='SubCathegory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subCathegoryName', models.CharField(default='Subcathegory Template', max_length=40)),
                ('cathegoryFK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.cathegory')),
            ],
        ),
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attributeName', models.CharField(default='Attribute Template', max_length=30)),
                ('subCathegoryFK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.subcathegory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subCathegoryFK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.subcathegory'),
        ),
    ]
