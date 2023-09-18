def sort_list_imperative(numbers):
    maximum = 0
    newList = []
    index = 0

    for i in range(len(numbers)):
        maximum = numbers[i]

        for u in range(index, len(numbers)):

            if maximum < numbers[u]:
                numbers[index] = numbers[u]
                numbers[u] = maximum
                maximum = numbers[index]
        
        newList.append(maximum)
        index += 1

    return newList


def sort_list_declarative(numbers):

    numbers.sort(reverse=True)

    return numbers


numbersImp = [1, 6, 2, 7, 3, 10, 8, 4, 9, 5]
numbersDec = [1, 6, 2, 7, 3, 10, 8, 4, 9, 5]


print(sort_list_imperative(numbersImp), "императивный стиль")
print(sort_list_declarative(numbersDec), "декларативный стиль")