usd = 75
euro = 80

money = int(input("Введите сумму, которую хотите обменять: "))
currency = int(input("Укажите код валюты(доллары-400, евро-401):"))

if currency == 400:
    cash = round(money / usd, 2)
    print("Валюта: доллары США")
elif currency == 401:
    cash = round(money / euro, 2)
    print("Валюта: евро")
else:
    cash = 0
    print("Неизвестная валюта")

print("к получению:", cash)

