import random
print("🎯 Welcome to the Number Guessing Game!")
top_of_range =input ("Type a number: ")

if top_of_range.isdigit(): 
   top_of_range =int (top_of_range)

   if top_of_range<=0:
    print(" ⚠️ Please enter a number larger than 0 next time ")
    quit ()
   
else:
    print("Please type a valid number next time")
    quit()
    
random_number = random.randint(0, top_of_range) 
guesses=0
while True:
   guesses += 1
   user_guess=input("🔢 Make a guess: ")
   if user_guess.isdigit():
      user_guess=int(user_guess)
   else:
      print("Please enter a number next time!")
      continue
   
   if user_guess == random_number:
      print("✅ You got it right")
      break
   elif user_guess > random_number:
         print("⬆️  You are above the number")
   else:
         print("⬇️  You are below the number")   


print(f"🎉 You guessed the number in {guesses} attempts!")

   
   
