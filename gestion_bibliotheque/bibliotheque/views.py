from django.shortcuts import render, redirect 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LivreForm
from .models import Livre

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('liste_livres')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})

@login_required
def livre_create(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            livre = form.save(commit=False) 
            livre.ajout_par = request.user
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm()
    return render(request, 'bibliotheque/livre_form.html', {'form': form})

def liste_livres(request):
    livres = Livre.objects.all().order_by('-date_ajout')
    return render(request, 'bibliotheque/livre_list.html', {'livres': livres})

def livre_detail(request, pk):
    livre = Livre.objects.get(pk=pk)
    return render(request, 'bibliotheque/livre_detail.html', {'livre': livre})

@login_required
def livre_update(request, pk):
    livre = Livre.objects.get(pk=pk)
    if request.user != livre.ajout_par:
        return redirect('liste_livres')
    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm(instance=livre)
    return render(request, 'bibliotheque/livre_form.html', {'form': form})

@login_required
def livre_delete(request, pk):
    livre = Livre.objects.get(pk=pk)
    if request.user != livre.ajout_par:
        return redirect('liste_livres')
    if request.method == 'POST':
        livre.delete()
        return redirect('liste_livres')
    return render(request, 'bibliotheque/livre_confirm_delete.html', {'livre': livre})





