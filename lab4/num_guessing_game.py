# Program for number guessing game

import random 

print(" --- WELCOME TO THE NUMBER GUESSING GAME ---") 
print("     GUESS THE NUMBER BETWEEN 1 TO 100")
print("     MAXIMUM ATTEMPTS: 7 ")
print("     SCORE: 100 POINTS")
points = 100

# picks the number randomly in given range
num = random.randint(1,100)

# initializes the variables
n = 0
attempts = 0
i=0

#  execute until correct answer or attempts are over
while attempts != 7 and n != num:
   
   # input guessed number from user
   print("")
   n = int(input("Enter the number you guessed: "))

   # increment and display the attempts
   attempts = attempts + 1
   print("ATTEMPT: ", attempts)

   # correct answer condition
   if( n == num):
       print("")
       print("YOUR SCORE: ", points)
       print("CORRECT ANSWER, YOU WON THE GAME")
       print("Attempts taken: ", attempts)

   # guess is too low condition
   elif ( n < num and (num - n) > 15):
       print("YOUR GUESS IS TOO LOW.")
       print("HINT: ",end="")
       if(num%3==0):
           print("Number is multiple of 3.")
       else:
           print("Number is NOT a multiple of 3.")
       points = points - 10
       print("current score: ", points)

   # guess is too high condition
   elif ( n > num and (n - num) > 15):
       print("YOUR GUESS IS TOO HIGH.")
       print("HINT: ",end="")
       if(num%5==0):
           print("Number is multiple of 5.")
       else:
           print("Number is NOT a multiple of 5.")

       points = points - 10
       print("current score: ", points)
 
   # guess is close to the number condition
   else:
       print("INCORRECT GUESS.")
       print("HINT: ",end ="")

       # hint for even or odd number
       if( i==0 ):
            if( num%2==0 ):
                print("Number is EVEN.")
            else:
                print("Number is ODD.")
            i = i + 1

       # hint for multiple of 7
       elif( i==2 ):
            if( num%7==0):
                print("Number is multiple of 7.")
            else: 
                print("Number is NOT a multiple of 7.")
            i = i + 1

       # hint for number greater or less than the guessed number    
       elif( i==1 ):
            if( n > num ):
                print("Your guess is MORE than the number.")
            else: 
                print("Your guess is LESS than the number.")
            i = i + 1
            
       # hint for multiple of 11
       elif( i==3 ):
            if( num%11==0):
                print("Number is multiple of 11.")
            else: 
                print("Number is NOT a multiple of 11.")
            
       points = points - 10
       print("current score: ", points)

# attempts over condition 
if( attempts == 7 ):
   points = 0
   print("")
   print("FINAL SCORE: ", points)
   print("Attempts over, YOU LOST.")
   print("The correct answer is: ", num)
   print("")