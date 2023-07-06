bilet = 0
kolvo = (int(input("Укажите количество билетов:\n")))
for vozrast in range(kolvo):
    vozrast = (int(input("Укажите возраст посетителя:\n")))
    if vozrast < 18:
        bilet = kolvo * 0
    elif vozrast >= 18 and vozrast <= 25:
        bilet = kolvo * 990
    elif vozrast > 25:
        bilet = kolvo * 1390
if kolvo == 0:
    print("Пожалуйста, выберите билет!")
else:
    print("Стоимость Ваших билетов составляет:", "%.2f" % bilet, "руб.")

if kolvo > 3:
    skidka = bilet/100*10
    print("Ваша скидка составляет:", "%.2f" % skidka, "руб.")
    print("Всего к оплате:", "%.2f" % (bilet-skidka), "руб.")
