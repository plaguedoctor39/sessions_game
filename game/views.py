from django.shortcuts import render
from game.models import Game, Player, PlayerGameInfo
import random
from game.forms import AnswerForm


def show_home(request):
    # request.session.flush()

    if not Game.objects.first():
        print('Создание игры')
        Game.objects.create()
        game = Game.objects.last()
        print('~ создание игрока-автора')
        Player.objects.create()
        player = Player.objects.last()
        player.save()
        answer = random.randint(1, 100)
        PlayerGameInfo.objects.create(game=game, player=player, number_answer=answer, is_author=True)
        current_game_info = PlayerGameInfo.objects.last()
        request.session['game_ended'] = 'no'
        request.session['game_id'] = game.game_id
        request.session['player_id'] = player.player_id
        context = {'answer': answer,
                   'game_info': current_game_info}
    else:
        game = Game.objects.first()
        print(f"id игры {request.session.get('game_id', 'no game')}")
        print(f"id игрока {request.session.get('player_id', 'no player')}")
        if request.session.get('game_id', 'no game') == 'no game' or request.session.get('player_id', 'no player') == 'no player' or not Player.objects.filter(player_id=request.session.get('player_id')):
            request.session['game_id'] = game.game_id
            print('~ создание игрока')
            Player.objects.create()
            player = Player.objects.last()
            PlayerGameInfo.objects.create(game=game, player=player, is_author=False)
            # request.session['game_id'] = game.game_id
            request.session['player_id'] = player.player_id
        current_game_info = PlayerGameInfo.objects.get(game=game, player_id=request.session.get('player_id'))
        answer_from_author = PlayerGameInfo.objects.first()
        current_game_info.number_answer = answer_from_author.number_answer
        answer = current_game_info.number_answer
        if current_game_info.is_author:
            if answer_from_author.is_answer_true:
                context = {'answer': answer,
                           'attempts': answer_from_author.attempts}
                Game.objects.all().delete()
                Player.objects.all().delete()
                PlayerGameInfo.objects.all().delete()
                request.session['game_id'] = 'no game'
            else:
                context = {'answer': answer}
        else:
            context = {}
            if request.method == 'POST':
                form = AnswerForm(request.POST)
                post_answer = int(request.POST['answer'])
                print(f'Отправлен ответ: {post_answer}')
                if answer == post_answer:
                    answer_from_author.is_answer_true = True
                    answer_from_author.attempts = current_game_info.attempts
                    answer_from_author.save()
                    print(f'Ответ {post_answer} верный')
                    text = 'Вы угадали число!'

                elif post_answer > answer:
                    current_game_info.attempts += 1
                    current_game_info.save()
                    print(f'Ответ {post_answer} неверный')
                    text = f'Загаданное число меньше числа {post_answer}'
                else:
                    current_game_info.attempts += 1
                    current_game_info.save()
                    print(f'Ответ {post_answer} неверный')
                    text = f'Загаданное число больше числа {post_answer}'
                context = {
                           'text': text}
            else:
                form = AnswerForm()
            context.update({'form': form,
                       })

        context.update({'game_info': current_game_info})

    return render(
        request,
        'home.html', context
    )
