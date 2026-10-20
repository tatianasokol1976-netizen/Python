def is_year_leap(num):
    return num % 4 == 0

while True:
    year_str = input("Введите год(ГГГГ): ")
    if len(year_str) == 4 and year_str.isdigit():
          year = int(year_str)
          break
    else:
        print("Неверно введен год, попробуйте еще раз \n")

result = is_year_leap(year)
print(f"год {year}: {result}")
