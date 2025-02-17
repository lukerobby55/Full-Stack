from django.urls import path
from .views import game_list, game_detail, games_by_platform, add_to_cart, basket_view, add_game, console_games, pc_games

urlpatterns = [
    path('', game_list, name='game_list'),
    path('game/<int:game_id>/', game_detail, name='game_detail'),
    path('platform/<str:platform>/', games_by_platform, name='games_by_platform'),
    path('add-to-cart/<int:game_id>/', add_to_cart, name='add_to_cart'),
    path('basket/', basket_view, name='basket_view'),
    path('add-game/', add_game, name='add_game'),
    path('console-games/', console_games, name='console_games'),  # ✅ Console games page
    path('pc-games/', pc_games, name='pc_games'),  # ✅ PC games page
]
