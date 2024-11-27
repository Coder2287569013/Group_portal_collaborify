from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Portfolio
from .forms import PortfolioForm


def create_portfolio(request):
    if not request.user.is_authenticated:  
        return redirect('login')  

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('portfolio:my_portfolios')
    else:
        form = PortfolioForm()

    return render(request, 'portfolio/portfolio_form.html', {'form': form})


def edit_portfolio(request, pk):
    if not request.user.is_authenticated: 
        return redirect('login')

    portfolio = get_object_or_404(Portfolio, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio:my_portfolios')
    else:
        form = PortfolioForm(instance=portfolio)

    return render(request, 'portfolio/portfolio_form.html', {'form': form})

def delete_portfolio(request, pk):
    if not request.user.is_authenticated: 
        return redirect('login')

    portfolio = get_object_or_404(Portfolio, pk=pk, user=request.user)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('portfolio:my_portfolios')

    return render(request, 'portfolio/portfolio_confirm_delete.html', {'portfolio': portfolio})


def my_portfolios(request):
    if not request.user.is_authenticated: 
        return redirect('login')

    portfolios = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolio/my_portfolios.html', {'portfolios': portfolios})


def all_portfolios(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio/all_portfolios.html', {'portfolios': portfolios})
