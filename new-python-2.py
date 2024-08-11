# price_house = 10
# good_credit = False
# if good_credit:
#     print(f'You have to put down 10% and your downPayment is {price_house * 0.1}')
# else:
#     print(f'You have to put down 20% and your downPayment is ${price_house * 0.2}')
#

# not_income = True
# ineligible = False
# criminal_record = True
# if not_income or ineligible and criminal_record:
#     print('Your absolutely not eligible for the even')
# else:
#     print('Your absolutely  eligible for the even')

# your_name = input("Enter your name:  ")
# if len(your_name) < 5:
#     print('You have to input more than 5 character.')
# elif 5 < len(your_name) < 50:
#     print(f'Hey, {your_name} we are glad to meet you')

# weight = int(input("Enter your weight: "))
# ask = input("In (L)s or (K)s or both: ");
# if ask.upper() == 'L':
#  converted = weight * 0.45
#  print(f'Your are {converted}Lbs')
# elif ask.upper() == 'K':
#   converted = weight / 0.45
#   print(f'Your are {converted}K')
# elif ask.lower() == 'both':
#   converted_kilo = int(weight / 0.45)
#   converted_lbs = int( weight * 0.45)
#   rounded = round(converted_kilo, 3)
#   rounded_lbs = round(converted_lbs, 3)
#   print(f'Your are {rounded}Kilo and {rounded_lbs}pound')
# else:
#   print("Provide information as 'L' or 'K' or 'both'")
#
# i = 5
# while i <=5:
#     print(i)
#
# secret_number = 7
# guess_count = 0
# remaining_count = 3
# guess_limit = 3
# while guess_count < guess_limit:
#     guess_count +=1
#     remaining_count -=1
#     guess = int(input("Guess the age of this beautiful women: "))
#     if guess == secret_number:
#         print("oh! yeh! you get that misterious number how enigma you are.")
#         break
#     elif guess_count == guess_limit:
#         print('You failed to guess')
#
#     else:
#         print(f"oh! You didn't know the mysterious number, but i will give you {remaining_count} more guesses ")

command = ""
started = False
while command !="quit":
    command = input("> ").lower()
    if command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit the car
        """)
    elif command == "stop":
        if not started:
             print('Car is already stopped')
        else:
          print('Car is stopped')
          started = False

    elif command == "start":
        if started:
          print("Car is already started")
        else:
         print("Car started")
         started = True


    elif command == "quit":
        break
    else:
        print("Invalid command")


