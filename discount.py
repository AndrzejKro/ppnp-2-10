# Kalendarze i czas


from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-10-04
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2023-10-04 09:55:44.970397
print(type(time))  # <class 'datetime.datetime'>


print(time.hour) # wyrzuca godzinę wynik = 9
print(today.day) # wyrzuca dzień miesiąca wynik = 4



print(today.year) # wyrzuca rok  wynik = 2023

formatted_date = datetime.now().strftime('%d/%m/%Y')  # formatujemy datę
print(formatted_date)  # 04/10/2023


formatted_time = datetime.now().strftime('%H:%M')  # formatujemy godzinę
print(formatted_time)  # 10:06

formatted_datetime = datetime.now().strftime('%d.%m.%Y %H:%M:%S')  # formatujemy datę i godzinę
print(formatted_datetime)  # 10:06

#tomorrow = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'

tomorrow = today + timedelta(days=1) # rozwinięcie o kolejne dnień
print(tomorrow) # 2023-10-05

# tomorrow = today + timedelta(hourse=12) # rozwinięcie o kolejne dnień
# print(tomorrow) # 2023-10-05

products = [
    {"sku":1, "exp_date":today, "price":100.0},
    {"sku":2, "exp_date":today, "price":80.0},
    {"sku":3, "exp_date":tomorrow, "price":20.0},
    {"sku":4, "exp_date":today, "price":50.0},
]

print(products)   #[{'sku': 1, 'exp_date': datetime.date(2023, 10, 4), 'price': 100.0}, {'sku': 2, 'exp_date': datetime.date(2023, 10, 4), 'price': 80.0}, {'sku': 3, 'exp_date': datetime.date(2023, 10, 5), 'price': 20.0}, {'sku': 4, 'exp_date': datetime.date(2023, 10, 4), 'price': 50.0}]


for product in products:
    print(products)
    if product['exp_date'] != today:
        continue

    product['price'] *=0.8
    print(f"""
    Price for sku= {product['sku']}
    is now {product['price']}""")




