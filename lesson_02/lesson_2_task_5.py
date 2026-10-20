def month_to_season(num):
    if 3 <= num <= 5:
        return("Весна")
    elif 6 <= num <= 8:
        return("Лето")
    elif 9 <= num <= 11:
        return("Осень")
    else:
        return("Зима")

while True:
   user_month = int(input("Введите число от 1 до 12: "))
   if 1 <= user_month <= 12:
       print(month_to_season(user_month))
       break
   else:
       print("Не верное число, попробуйите еще раз: \n")
    
  