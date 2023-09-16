print("Rollercoster user verification")
height=int(input("Enter your height in cm   "))
bill = 0

if height >=120:
  print("YOU CAN RIDE THE ROLLERCOSTER")
  age=int(input("Enter your age   "))
  if age < 12:
    bill = 5
    print("5$")
  elif age<=18:
    bill = 7
    print('7$')
  elif age >= 45 and age <= 55:
    print("Have a free ride")
  else:
    bill = 12
    print("12$")
    
  photo = input("Do you want photos with ticket? Y/N ")
  if photo=='Y':
   bill += 3
  print(f"your total bill is {bill}")
else:
  print('you are not eligible')
