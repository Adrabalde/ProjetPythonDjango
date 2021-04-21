from django.shortcuts import render,redirect
from .models import Statut,Annuaire,Individu,Groupe,GroupeIndividu
from .forms import IndividuForm,GroupeForm,GroupeIndividuForm
from django.http import HttpResponse,JsonResponse
import csv, io
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .seriallizers import IndividuSerializer 

# Create your views here.
def listestatut(request):
    listestatut = Statut.objects.all()
    return render(request, 'listestatut.html',{'listestatut': listestatut})
def annuaire(request):
    annuaires = Annuaire.objects.all()
    return render(request, 'annuaire.html',{'annuaires': annuaires})
def individu(request):
    individus = Individu.objects.all()
    return render(request, 'individu.html',{'individus': individus})  
def groupe(request):
    groupes = Groupe.objects.all()
    return render(request, 'groupe.html',{'groupes': groupes})  
def ajouterIndividu(request):
    if request.method=="POST": 
        form=IndividuForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('individu')
    else :
        form=IndividuForm
    f={'form':form}    
    return render(request, 'ajouterIndividu.html', context=f)

def ajouterGroupe(request):
    if request.method=="POST": 
        form=GroupeForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('groupe')
    else :
        form=GroupeForm
    f={'form':form}    
    return render(request, 'ajouterGroupe.html', context=f)

def modifierIndividu(request,id):
    indiv=Individu.objects.get(id=id) 
    if request.method=="POST": 
        form=IndividuForm(request.POST,instance=indiv)
        if form.is_valid():
            form.save() 
            return redirect('individu')
    else :
        form=IndividuForm(instance=indiv)
    f={'form':form,'indiv':indiv}    
    return render(request, 'modifierIndividu.html', context=f)
    
def supprimerIndividu(request,id):
    indiv=Individu.objects.get(id=id) 
    indiv.delete()
    return redirect("individu")
def modifierGroupe(request,id):
    group=Groupe.objects.get(id=id) 
    if request.method=="POST": 
        form=GroupeForm(request.POST,instance=group)
        if form.is_valid():
            form.save() 
            return redirect('groupe')
    else :
        form=GroupeForm(instance=group) 
    f={'form':form,'group':group}    
    return render(request, 'modifierGroupe.html', context=f)    
def supprimerGroupe(request,id):
    group=Groupe.objects.get(id=id) 
    group.delete()
    return redirect("groupe")    
def individuX(request, id):
    individu = Individu.objects.filter(id=id).get()
    return render(request, 'individuX.html', {'individu': individu}) 
def groupeX(request, id):
    groupe = GroupeIndividu.objects.filter(codeGroupe=id) 
    liste = []
    for g in groupe :
        liste.append(g.codeindividu_id)
    indiv=tuple(liste) 
    print(liste) 
    individus= Individu.objects.filter(id__in=indiv)     
    return render(request, 'groupeX.html', {'individus': individus})        
def importcsv(request):
    # declaring template
    template = "importcsv.html"
    data = Individu.objects.all() # Pour selectionner tous les enregistrements pour le modele individu 
    prompt = {   # C'est un message 
        'order': ' Le fichier csv doit respecter l\'ordre suivant: nom, prenom, email,num,annuaire,statut',
        'individus': data   # c'est la liste des individus  
              }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # Tester si le fichier est de type csv 
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Attention le fichier importer n\'est pas de format CSV')  
    data_set = csv_file.read().decode('UTF-8') 
    # Convertir le contenu du fichier csv vers une chaine de caractère
    io_string = io.StringIO(data_set) 
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"): 
        created = Individu.objects.update_or_create(
        nom=column[0], 
        prenom=column[1],
        email=column[2],
        num=column[3],
        annuaire=column[4],
        statut=column[5],
    )
    context = {}
    return render(request, template, context)    
def exportcsv (request) :
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="individus.csv"'
    individus=Individu.objects.all() 
    writer=csv.writer(response) 
    for individu in individus : 
        writer.writerow([individu.nom,individu.prenom,individu.email]) 
    return response 

def AssocierIndividuGroupe(request):
    if request.method=="POST": 
        form=GroupeIndividuForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('groupe')
    else :
        form=GroupeIndividuForm
    f={'form':form}    
    return render(request, 'GroupeIndividu.html', context=f) 
class TestApi(APIView) :
    def get(self,request,*args,**kwargs):
        data=Individu.objects.all()
        serializer=IndividuSerializer(data,many=True) 
        return  Response(serializer.data) 
    def post(self,request,*args,**kwargs):
        serializer=IndividuSerializer(data=request.data) 
        if serializer.is_valid() :
            serializer.save() 
            return  Response(serializer.data)  
        else : 
            return  Response(serializer.errors)  
    

# def testapi(request) :
#     data={
#         'nom':'BALDE', 
#         'age': 56
#             }    
#     return  JsonResponse(data) 
