price_total = 0
ticket_number = int(input('Какое количество билетов Вы хотите приобрести?\n'))
for i in range(ticket_number):
    i += 1
    age_for_ticket = int(input(f'Укажите возраст участника для билета №{i}?\n'))
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 25 > age_for_ticket >= 18:
        price_total += 990
        print('Стоимость билета: 990 руб.')
    else:
        price_total += 1390
        print('Стоимость билета: 1390 руб.')
if ticket_number > 3:
    price_total = price_total - ((price_total / 100) * 10)
    print(f'Сумма к оплате {price_total} руб. с учетом 10%-ой скидки за покупку более 3-х билетов.')
else:
    print(f'Сумма к оплате {price_total} руб.')
