# Create your views here.
from team.models import Roster, Players
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    context = {
        'players_count': Players.objects.count(),
        'roster_count' : Roster.objects.count(),
    }
    return render(request, "team/home.html", context)

def roster(request, pk):
    #roster = Roster.objects.order_by('?')[0]
    players = Players.objects.order_by('?')[0]
    roster = get_object_or_404(Roster, id=pk)
    return render(request, "team/roster.html", {'roster': roster})

def rosterList(request):
    roster_list = Roster.objects.all()
    
    return render(request, 'team/roster_list.html', {"rosters": roster_list})

def players(request, pk):
    #players = Players.objects.order_by('?')[0]
    players = get_object_or_404(Players, id=pk)
    return render(request, "team/players.html", {'players': players})

def playersList(request):
    #players = Players.objects.order_by('?')[0]
    players_list = Players.objects.all()
    paginator = Paginator(players_list, 25)
    page = request.GET.get('page')
    try:
        players= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        players = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        players = paginator.page(paginator.num_pages)

    return render(request, 'team/players_list.html', {"players": players})
    
    
    #players = get_object_or_404(Players)
    #return render(request, "team/players_list.html", {'players': players})

