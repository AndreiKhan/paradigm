import time

def stopWatch():
    # Меню
    print('Введите цифру:')
    print('1 - запустить секундомер')
    print('2 - приостановить секундомер')
    print('3 - снять с паузы секундомер')
    print('4 - остановить секундомер')
    print()

    # Переменные для запоминания времени, последней команды и остановили ли секундомер
    startTime = 0
    pause = 0
    lastCommand = 0
    start = True

    # бесконечный цикл пока его не остановят
    while start:
        command = input()

        # Подкорректированы условия чтобы не сломать секундомер
        # Запустить можно только один раз первой командой
        if command == '1' and lastCommand == 0:
            startTime = time.time()
            lastCommand = '1'
            print('Секундомер запущен')

        # Приостановить можно только если секундомер запущен
        elif command == '2' and lastCommand != '2' and lastCommand != 0:
            pause += (round(time.time() - startTime, 2))
            lastCommand = '2'
            print(f'Секундомер приостановлен, текущее время - {round(pause, 2)}')

        # Снять с паузы можно только если секундомер был приостановлен
        elif command == '3' and lastCommand == '2':
            startTime = time.time()
            lastCommand = '3'
            print(f'Секундомер снят с паузы')

        # Остановить можно только если секундомер запущен
        elif command == '4' and lastCommand != 0 and lastCommand != '2':
            print(f'Времени прошло {round((time.time() - startTime) + pause, 2)}')
            print('Секундомер остановлен')
            start = False

        # Если введено чтото не то, то выдаст сообщение
        elif True:
            print('Нельзя это сделать')

stopWatch()