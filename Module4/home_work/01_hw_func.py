# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    left_side = str(ticket_number // 1000)
    right_side = str(ticket_number % 1000)
    summ_left = 0
    summ_right = 0
    for i in left_side:
        summ_left += int(i)

    for i in right_side:
        summ_right += int(i)

    if summ_left == summ_right:
        print("Этот билет счастливый!")
    else:
        print("Этот билет НЕ счастливый (")
    pass


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
