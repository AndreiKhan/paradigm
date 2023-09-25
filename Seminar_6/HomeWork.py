import time

def stopWatch():
    # Меню
    print('Введите цифру:')
    print('1 - запустить секундомер')
    print('2 - приостановить секундомер')
    print('3 - снять с паузы секундомер')
    print('4 - остановить секундомер')
    print()

    startTime = 0
    pause = 0
    start = True

    while start:
        command = input()

        if command == '1':
            startTime = time.time()
            print('Секундомер запущен')

        elif command == '2':
            pause += (round(time.time() - startTime, 2))
            print(f'Секундомер приостановлен, текущее время - {round(pause, 2)}')

        elif command == '3':
            startTime = time.time()
            print(f'Секундомер снят с паузы')

        elif command == '4':
            print(f'Времени прошло {round((time.time() - startTime) + pause, 2)}')
            print('Секундомер остановлен')
            start = False

stopWatch()