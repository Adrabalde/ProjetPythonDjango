# Generated by Django 3.1.2 on 2020-11-14 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_individu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='individu',
            name='img',
            field=models.ImageField(null=True, upload_to='myapp_img/'),
        ),
    ]
