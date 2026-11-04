from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Redmi Note 10", "+79537546859"),
    Smartphone("Samsung", "Galaxy A50", "+79034877793"),
    Smartphone("Nokia", "3310", "+79874563288"),
    Smartphone("Motorola", "Edge 50 Pro", "+79994563754"),
    Smartphone("Sony", "Ericsson", "+79524905674")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}.")