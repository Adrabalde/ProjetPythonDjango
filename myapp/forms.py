from django import forms
from django.forms import ModelForm
from .models import Individu,Groupe,GroupeIndividu 

class IndividuForm(forms.ModelForm):
    class Meta:
        model = Individu
        fields= ['nom','prenom','email','num','statut','annuaire'] 
class GroupeForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields= ['nom'] 
class GroupeIndividuForm(forms.ModelForm):
    class Meta:
        model = GroupeIndividu
        fields= ['codeindividu', 'codeGroupe']  
        
                