from django.db import models

# Create your models here.

class Si_Personnel(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    num_siham = models.IntegerField(db_column='NUM_SIHAM', unique=True)  # Field name made lowercase.
    d_creation = models.DateField(db_column='D_CREATION', blank=True, null=True)  # Field name made lowercase.
    d_modification = models.DateField(db_column='D_MODIFICATION', blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=20)  # Field name made lowercase.
    prenom = models.CharField(db_column='PRENOM', max_length=20)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cnu = models.IntegerField(db_column='CNU')  # Field name made lowercase.
    miage = models.IntegerField(db_column='MIAGE')  # Field name made lowercase.
    fid_statut = models.IntegerField(db_column='FID_STATUT')  # Field name made lowercase.

    class Meta: 
        managed = False
        db_table = 'SI_PERSONNEL'

    def __str__(self):
        return self.prenom + "." + self.nom + ', Statut='+ str(self.fid_statut) 

class Si_Statut(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=20)  # Field name made lowercase.
    nb_h_min = models.IntegerField(db_column='NB_H_MIN')  # Field name made lowercase.
    nb_h_max = models.IntegerField(db_column='NB_H_MAX', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SI_STATUT'

    def __str__(self):
        return self.libelle+'/ id ='+str(self.id)

class Si_Ec(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_liaison = models.IntegerField(db_column='ID_LIAISON')  # Field name made lowercase.
    credit = models.DecimalField(db_column='CREDIT', max_digits=3, decimal_places=1)  # Field name made lowercase.
    d_creation = models.DateField(db_column='D_CREATION')  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=100)  # Field name made lowercase.
    h_cm = models.IntegerField(db_column='H_CM')  # Field name made lowercase.
    h_td = models.IntegerField(db_column='H_TD')  # Field name made lowercase.
    h_tp = models.IntegerField(db_column='H_TP', blank=True, null=True)  # Field name made lowercase.
    h_stage = models.IntegerField(db_column='H_STAGE', blank=True, null=True)  # Field name made lowercase.
    lmd = models.IntegerField(db_column='LMD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'si_ec'

    def __str__(self):
        return self.libelle+'/ id ='+str(self.id)    


class Si_View_Ls(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=20)  # Field name made lowercase.
    prenom = models.CharField(db_column='PRENOM', max_length=20)  # Field name made lowercase.
    fid_pers = models.IntegerField(db_column='FID_PERS')  # Field name made lowercase.
    libelle_ec = models.CharField(db_column='LIBELLE_EC', max_length=100)  # Field name made lowercase.
    fid_ec = models.IntegerField(db_column='FID_EC', blank=True, null=True)  # Field name made lowercase.
    groupe = models.CharField(db_column='GROUPE', max_length=25)  # Field name made lowercase.
    sem = models.CharField(db_column='SEM', max_length=2)  # Field name made lowercase.
    h_cm = models.DecimalField(db_column='H_CM', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    h_td = models.DecimalField(db_column='H_TD', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    hetd = models.DecimalField(db_column='HETD', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return 'LIGNE : '+ self.id +' :' + self.nom + "." + self.prenom + "." + self.ec + "." + self.groupe

    class Meta:
        managed = False
        db_table = 'SI_VIEW_LS'

