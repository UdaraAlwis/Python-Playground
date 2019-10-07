# Python Self Learning - Udara Alwis
# https://www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6
# Learnings from Video 1-14
# Contains: Print, Input, Comments, Strings, Formatting, Numbers

#start app
#Greeting
print("Hello sir!")
#accepting inputs
time_of_day = input("Is it a morning or evening? ")
print(f"Ok then, Good {time_of_day}!")

#Math game
print("Well next, it's time for some math sir!")
val_1 = input("Enter a number please: ")
val_2 = input("Enter another number please: ")
#values accepted as strings
#then convert inputs to number
calc_answer = int(val_1) + int(val_2)

print("Guess the total now!")
user_answer = input("Your answer: ")

#print answer as string
print(f"Well the actual answer is: {str(calc_answer)}")

print("Goodbye sir!")

#end app