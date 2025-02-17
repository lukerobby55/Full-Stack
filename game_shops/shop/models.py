from django.db import models

class Game(models.Model):
    # Choices for gaming platforms
    PLATFORM_CHOICES = [
        ('PS5', 'PlayStation 5'),
        ('XBOX', 'Xbox One'),
        ('SWITCH', 'Nintendo Switch'),
        ('PC', 'PC'),
    ]
    
    # Choices for game genres
    GENRE_CHOICES = [
        ('SHOOTER', 'Shooter'),
        ('ACTION', 'Action'),
        ('ADVENTURE', 'Adventure'),
        ('RPG', 'RPG'),
        ('SPORTS', 'Sports'),
    ]

    name = models.CharField(max_length=255)  # Game title with a max length of 255 characters
    description = models.TextField()  # Detailed description of the game
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)  # Platform dropdown selection
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)  # Genre dropdown selection
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price with 2 decimal places (max 9999.99)
    stock = models.PositiveIntegerField(default=0)  # Stock count, ensures only non-negative values

    def __str__(self):
        return self.name  # Returns the game name when object is printed

