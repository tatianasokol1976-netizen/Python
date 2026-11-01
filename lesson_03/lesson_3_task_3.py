from address import Address
from mailing import Mailing

to_adr = Address("237894", "Санкт-Петербург", "Коваленко", 44, 26)
from_adr = Address("603187", "Уфа", "Коломенская", 44, 15)

mail = Mailing(to_adr, from_adr, 170.15, "3389575664748R")

print(mail)
