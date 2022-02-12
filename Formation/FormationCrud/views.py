from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Formation

def List(request):
    formations = Formation.objects.all()
    return render(request,'FormationCrud/Liste_formations.html',{'formations': formations})

def List_web(request):
    formations = Formation.newmanager.get_queryset()
    return render(request,'FormationCrud/Liste_formations_web.html',{'formations': formations})

def List_Mobile(request):
    formation_mob = Formation.newmanager.get_querymobile()
    return render(request,'FormationCrud/Liste_formations_web.html',{'formations': formation_mob})

def List_Cloud(request):
    formation_mob = Formation.newmanager.get_querycloud()
    return render(request,'FormationCrud/Liste_formations_web.html',{'formations': formation_mob})

def add(request):
    return render(request,'FormationCrud/Ajout_Formation.html')

def update(request):
    return render(request,'FormationCrud/Modifier_Formation.html')

def recherche(request):
    query = request.GET.get('query')
    if not query:
        formations = Formation.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        formations = Formation.objects.filter(titre__icontains=query)

    if not formations.exists():
        message = "Cette formation n'existe pas encore !"
        args = {}
        args['mytext'] = message
        return render(request,'FormationCrud/Liste_formations.html', args)
    else:

        return render(request,'FormationCrud/Liste_formations.html',{'formations': formations})

class FormationDetailView(DetailView):
    model = Formation