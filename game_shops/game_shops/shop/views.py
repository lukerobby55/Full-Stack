from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from .forms import GameForm

def game_list(request):
    games = Game.objects.all()
    return render(request, 'shop/game_list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'shop/game_detail.html', {'game': game})

def games_by_platform(request, platform):
    games = Game.objects.filter(platform=platform)
    return render(request, 'shop/games_by_platform.html', {'games': games, 'platform': platform})

def add_to_cart(request, game_id):
    # Get the shopping cart from session
    cart = request.session.get('cart', {})

    # Convert game_id to string because session keys are stored as strings
    game_id = str(game_id)

    # Increase quantity if game exists, otherwise set to 1
    if game_id in cart:
        cart[game_id] += 1
    else:
        cart[game_id] = 1

    # Save the updated cart back to the session
    request.session['cart'] = cart
    request.session.modified = True  # Ensure session updates

    return redirect('basket_view')  # Redirect to the basket page

def basket_view(request):
    cart = request.session.get('cart', {})  # Get the cart from session
    games = Game.objects.filter(id__in=cart.keys())  # Fetch games in cart

    # Attach the quantity to each game object
    for game in games:
        game.quantity = cart.get(str(game.id), 0)  # Ensure game IDs match session keys

    return render(request, 'shop/basket.html', {'games': games})


def add_game(request):   #admin adding games
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')  # Redirect to all games page
    else:
        form = GameForm()

    return render(request, 'shop/add_game.html', {'form': form})

def console_games(request):
    """Show only console games (PS5, Xbox, Switch)"""
    console_platforms = ['PS5', 'XBOX', 'SWITCH']
    games = Game.objects.filter(platform__in=console_platforms)
    return render(request, 'shop/console_games.html', {'games': games})

def pc_games(request):
    """Show only PC games"""
    games = Game.objects.filter(platform='PC')
    return render(request, 'shop/pc_games.html', {'games': games})





