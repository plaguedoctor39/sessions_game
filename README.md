# Игра "Угадай число" (Сессии)

## Задание

Необходимо реализовать игру "Угадай число" для двух пользователей. Суть заключается в следующем:
один игрок загадывает число, а второй отгадывает. Когда первый игрок заходит на главную страницу сайта, то он генерирует случайное число,
в любом удобном диапазоне, которое отображется на этой странице. Данный игрок является создателем игры.
Когда на эту же страницу попадает другой игрок, он не видит это число, но перед ним появляется форма с предложением
угадать число. Форма очень простая: поле для ввода угадываемого числа, и кнопка для его проверки.
Когда второй игрок вводит число и нажимает на кнопку, он получает одно из следующих сообщений:
* Вы угадали загаданное число!
* Введенное число меньше угадываемого.
* Введенное число больше угадываемого.
Если число было угадано, то у создателя игры (при обновлении страницы) отображается сообщение: "Ваше число угадали с 3 попыток".
Следующим число загадывает тот игрок, который раньше обновит страницу.
