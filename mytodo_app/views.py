from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
#from django.http import HttpResponseRedirect
import random



# Create your views here.

def home(request):
    if request.method ==  'POST':
        form = ListForm(request.POST or None)
        if form.is_valid() and request.POST['item'] != '':
            form.save()
            all_items = List.objects.all
            messages.success(request, request.POST['item']+ ' er blevet tilføjet til din opgave list')
            context = {'all_items': all_items}
            return render(request, 'home.html', context)
    else:
        all_items =List.objects.all
        context = {'all_items': all_items}
        return render(request, 'home.html', context)

def about(request):
    name="Maria"
    nick = randomNick()
    context = {'name': name,'nick': nick,}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Opgaven er blevet slettet fra din opgave list')
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    messages.success(request, 'Opgaven er løst, hvor er du bare mega sej')
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    messages.success(request, 'Opgaven var ikke helt løst, no worries det handler bare om at give den en skalle ;-)')
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method ==  'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid() and request.POST['item'] != '':
            form.save()
            all_items = List.objects.all
            messages.success(request, request.POST['item']+ ' er blevet redigeret i din opgave list')
            return redirect('home')
    else:
        item =List.objects.get(pk=list_id)
        context = {'item': item}
        return render(request, 'edit.html', context)


def randomNick():
    thisListNick = ('skønne','dejlige','guddomelige','fantastisk','humør bómbe','kærlige','sexed','smiliende','lystige','krigeriske','kage bagende','rullegardins ekspert')
    thisNick = random.choice(thisListNick)
    print(thisNick)
    return thisNick



