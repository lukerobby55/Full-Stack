from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from .forms import GameForm

# View to display a list of all games
def game_list(request):
    games = Game.objects.all()  # Retrieve all games from the database
    return render(request, 'shop/game_list.html', {'games': games})

# View to display details of a single game
def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)  # Get game by ID, or return 404 if not found
    return render(request, 'shop/game_detail.html', {'game': game})

# View to filter games by platform
def games_by_platform(request, platform):
    games = Game.objects.filter(platform=platform)  # Retrieve games matching the platform
    return render(request, 'shop/games_by_platform.html', {'games': games, 'platform': platform})

# View to add a game to the shopping cart
def add_to_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)  # Retrieve game by ID
    
    if game.stock > 0:  # Check if the game is in stock
        cart = request.session.get('cart', {})  # Retrieve the cart from session
        game_id = str(game_id)  # Ensure game_id is a string to match session keys
        cart[game_id] = cart.get(game_id, 0) + 1  # Increase quantity in cart
        request.session['cart'] = cart  # Save updated cart to session
        request.session.modified = True  # Mark session as modified

        # Reduce stock count as the game is added to the cart
        game.stock -= 1
        game.save()  # Save updated stock count

    return redirect('basket_view')  # Redirect to the basket page

# View to display the shopping cart
def basket_view(request):
    cart = request.session.get('cart', {})  # Retrieve cart from session
    games = Game.objects.filter(id__in=cart.keys())  # Fetch game objects that are in the cart

    # Attach quantity information to each game object
    for game in games:
        game.quantity = cart.get(str(game.id), 0)  # Ensure IDs are consistent with session keys

    return render(request, 'shop/basket.html', {'games': games})

# View to allow an admin to add a new game
def add_game(request):
    if request.method == "POST":  # If form is submitted
        form = GameForm(request.POST)  # Get data from submitted form
        if form.is_valid():  # Validate form
            form.save()  # Save game to database
            return redirect('game_list')  # Redirect to the game list page
    else:
        form = GameForm()  # If GET request, create a blank form

    return render(request, 'shop/add_game.html', {'form': form})

# View to display console games (PS5, Xbox, Switch)
def console_games(request):
    console_platforms = ['PS5', 'XBOX', 'SWITCH']  # List of console platforms
    games = Game.objects.filter(platform__in=console_platforms)  # Filter games for consoles
    return render(request, 'shop/console_games.html', {'games': games})

# View to display only PC games
def pc_games(request):
    games = Game.objects.filter(platform='PC')  # Retrieve only PC games
    return render(request, 'shop/pc_games.html', {'games': games})
