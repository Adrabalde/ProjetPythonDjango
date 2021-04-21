from django.db import models
import datetime
# Create your models here.
class Statut(models.Model) :
    nom=models.CharField(max_length=50) 
    def __str__(self) :
        return self.nom 

class Annuaire(models.Model) :
    nom=models.CharField(max_length=50) 
    def __str__(self) :
        return self.nom     
class Individu(models.Model) :
    APOGEE='01'
    HARPEGE='02'
    FOMASUP='03' 
    annuaire = [
        (APOGEE, 'étudiant'),
        (HARPEGE, 'enseignant'),
        (FOMASUP, 'apprenant en formation continue')
    ]
    nom=models.CharField(max_length=50)  
    prenom=models.CharField(max_length=50)  
    email=models.EmailField(max_length=50)   
    num=models.CharField( 
        max_length=2, 
        choices=annuaire,
        default=APOGEE
        )
    annuaire=models.CharField(max_length=20, null=True)  
    statut=models.CharField(max_length=20, null=True)  
    img=models.ImageField(upload_to='myapp_img/',null=True) 
    created: models.DateTimeField(default=datetime.datetime.now())
    def __str__(self) :
        return self.prenom 

class Groupe(models.Model) :
    nom=models.CharField(max_length=50) 
    def __str__(self) :
        return self.nom     

class GroupeIndividu(models.Model) :
    codeindividu=models.ForeignKey(Individu,on_delete =models.CASCADE) 
    codeGroupe=models.ForeignKey(Groupe,on_delete =models.CASCADE) 
