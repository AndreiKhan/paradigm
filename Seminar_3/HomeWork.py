def x_o():
    # Варианты победы
    solutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    # Поле для заполнения
    field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # список ходов
    symbols = ['X', 'O']
    symbol = ''

    # Выводим поле для пользователя
    print('___________________')
    print('|     |     |     |')
    print(f'|  {field[0]}  |  {field[1]}  |  {field[2]}  |')
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print(f'|  {field[3]}  |  {field[4]}  |  {field[5]}  |')
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print(f'|  {field[6]}  |  {field[7]}  |  {field[8]}  |')
    print('|_____|_____|_____|')

    # цикл ходов
    for i in range(9):
        # если ход четный то ходят крестики, так символ сам меняется на нужный
        if i % 2 == 0:
            symbol = symbols[0]
        else:
            symbol = symbols[1]

        # Вводим цифру куда поставить символ
        turn = int(input(f'введите цифру куда поставить {symbol}\n'))

        field[turn - 1] = symbol

        print('___________________')
        print('|     |     |     |')
        print(f'|  {field[0]}  |  {field[1]}  |  {field[2]}  |')
        print('|_____|_____|_____|')
        print('|     |     |     |')
        print(f'|  {field[3]}  |  {field[4]}  |  {field[5]}  |')
        print('|_____|_____|_____|')
        print('|     |     |     |')
        print(f'|  {field[6]}  |  {field[7]}  |  {field[8]}  |')
        print('|_____|_____|_____|')

        # проверяем условие победы
        for u in solutions:
            if field[u[0]] == field[u[1]] and field[u[1]] == field[u[2]]:
                return f'Победили {symbol}'

    # Если ходы кончились и условие победы не сработало, то объявляется ничья
    return 'Ничья'

print(x_o())