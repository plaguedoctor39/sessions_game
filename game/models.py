from django.db import models


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True, verbose_name='id игрока')
    games = models.ManyToManyField('Game', through='PlayerGameInfo', through_fields=('player', 'game', 'attempts', 'is_author'))

    class Meta:
        db_table = 'players'
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Game(models.Model):
    game_id = models.IntegerField(primary_key=True, verbose_name='id игры')

    class Meta:
        db_table = 'games'
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    attempts = models.IntegerField(default=0, verbose_name='Количество попыток')
    number_answer = models.IntegerField(null=True)
    is_answer_true = models.BooleanField(default=False)
    is_author = models.BooleanField()

    class Meta:
        db_table = 'Players_and_games'
