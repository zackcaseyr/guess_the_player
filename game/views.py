from django.shortcuts import render
from .models import Player
import random

def guess_the_player(request):
    player = random.choice(Player.objects.all())  # Get a random player from the database

    if request.method == 'POST':
        guessed_name = request.POST.get('guess')
        if guessed_name.lower() == player.name.lower():
            result = "Correct!"
        else:
            result = "Wrong! The correct answer was " + player.name
        return render(request, 'game/result.html', {'result': result})

    # Make sure the player object is passed in the context
    return render(request, 'game/guess.html', {'player': player})
