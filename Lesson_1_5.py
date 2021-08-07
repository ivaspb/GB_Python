proceeds = float(input('Введите значение выручки: '))
costs = float(input('Введите значение расходов: '))

if proceeds < costs:
    print('Вы теряете деньги. С этим срочно нужно что-то делать!')
    print('Ваши потери:', costs - proceeds)
elif proceeds > costs:
    print('Поздравляю! Дела идут хорошо!')
    print('Вы заработали:', proceeds - costs)
    staff = int(input('Сколько людей у вас работает? Введите значение: '))
    print(f'Каждый сотрудник приносит вам %.2f рублей выручки' %(proceeds / staff))
