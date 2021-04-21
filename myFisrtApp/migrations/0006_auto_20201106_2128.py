# Generated by Django 3.1.2 on 2020-11-06 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFisrtApp', '0005_statut_commentaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Si_Ec',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('id_liaison', models.IntegerField(db_column='ID_LIAISON')),
                ('credit', models.DecimalField(db_column='CREDIT', decimal_places=1, max_digits=3)),
                ('d_creation', models.DateField(db_column='D_CREATION')),
                ('libelle', models.CharField(db_column='LIBELLE', max_length=100)),
                ('h_cm', models.IntegerField(db_column='H_CM')),
                ('h_td', models.IntegerField(db_column='H_TD')),
                ('h_tp', models.IntegerField(blank=True, db_column='H_TP', null=True)),
                ('h_stage', models.IntegerField(blank=True, db_column='H_STAGE', null=True)),
                ('lmd', models.IntegerField(blank=True, db_column='LMD', null=True)),
            ],
            options={
                'db_table': 'si_ec',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Si_Personnel',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('num_siham', models.IntegerField(db_column='NUM_SIHAM', unique=True)),
                ('d_creation', models.DateField(blank=True, db_column='D_CREATION', null=True)),
                ('d_modification', models.DateField(blank=True, db_column='D_MODIFICATION', null=True)),
                ('nom', models.CharField(db_column='NOM', max_length=20)),
                ('prenom', models.CharField(db_column='PRENOM', max_length=20)),
                ('mail', models.CharField(blank=True, db_column='MAIL', max_length=50, null=True)),
                ('cnu', models.IntegerField(db_column='CNU')),
                ('miage', models.IntegerField(db_column='MIAGE')),
                ('fid_statut', models.IntegerField(db_column='FID_STATUT')),
            ],
            options={
                'db_table': 'SI_PERSONNEL',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Si_Statut',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('libelle', models.CharField(db_column='LIBELLE', max_length=20)),
                ('nb_h_min', models.IntegerField(db_column='NB_H_MIN')),
                ('nb_h_max', models.IntegerField(blank=True, db_column='NB_H_MAX', null=True)),
            ],
            options={
                'db_table': 'SI_STATUT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Si_View_Ls',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('nom', models.CharField(db_column='NOM', max_length=20)),
                ('prenom', models.CharField(db_column='PRENOM', max_length=20)),
                ('fid_pers', models.IntegerField(db_column='FID_PERS')),
                ('libelle_ec', models.CharField(db_column='LIBELLE_EC', max_length=100)),
                ('fid_ec', models.IntegerField(blank=True, db_column='FID_EC', null=True)),
                ('groupe', models.CharField(db_column='GROUPE', max_length=25)),
                ('sem', models.CharField(db_column='SEM', max_length=2)),
                ('h_cm', models.DecimalField(blank=True, db_column='H_CM', decimal_places=2, max_digits=4, null=True)),
                ('h_td', models.DecimalField(blank=True, db_column='H_TD', decimal_places=2, max_digits=4, null=True)),
                ('hetd', models.DecimalField(blank=True, db_column='HETD', decimal_places=3, max_digits=7, null=True)),
            ],
            options={
                'db_table': 'SI_VIEW_LS',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Statut',
        ),
        migrations.DeleteModel(
            name='Individu',
        ),
    ]