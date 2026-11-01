class Address:
    def __init__(self, postcode, city, street, house, apartment):
        self.postcode = postcode
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return f"{self.postcode} г. {self.city}, ул. {self.street}, д. {self.house} - кв. {self.apartment}"
