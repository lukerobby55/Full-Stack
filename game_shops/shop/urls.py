from django.urls import path
from .views import (
    game_list, game_detail, games_by_platform, add_to_cart, 
    basket_view, add_game, console_games, pc_games
)

urlpatterns = [
    path('', game_list, name='game_list'),  
    # Home page displaying all games

    path('game/<int:game_id>/', game_detail, name='game_detail'),  
    # Game detail page, expects an integer game ID

    path('platform/<str:platform>/', games_by_platform, name='games_by_platform'),  
    # Filter games by platform, expects a platform string

    path('add-to-cart/<int:game_id>/', add_to_cart, name='add_to_cart'),  
    # Add a specific game to the cart using its ID

    path('basket/', basket_view, name='basket_view'),  
    # View shopping cart contents

    path('add-game/', add_game, name='add_game'),  
    # Admin page for adding a new game

    path('console-games/', console_games, name='console_games'),  
    # ✅ Page displaying only console games (PS5, Xbox, Switch)

    path('pc-games/', pc_games, name='pc_games'),  
    # ✅ Page displaying only PC games
]
