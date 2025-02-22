
'''
#1. Write a function called count_vowels(input) that takes a string
#and returns the number of vowels (a, e, i, o, u) in it.
'''
def count_vowels(input): 
    #this is to define the vowels
    vowels = "aeiouAEIOU"
    count = 0
    #so we can loop through all of the characters we need write this 
    for char in input:
        if char in vowels: 
            count += 1 
    return count 
#Now to test the function! 

Test_string = input("Please enter a valid string")
Result = count_vowels(Test_string)
print(Result)
'''
#2. Write a function called is_palindrome(s) that checks whether a string is a
palindrome
(reads the same forward and backward, ignoring case). The function should
returns either True or False.
Test: racecar (True), pikachu (False), Racecar (True)
Input: string (s)
Output: boolean
Function body: lowercase s, flip s and save to new variable (flipped_s), and then compare s & flipped_s
'''
def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return lower_s == flipped_s 
    
print(is_palindrome("life"))
print(is_palindrome("racecar"))
print(is_palindrome("Workout"))
'''

#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
For example, water is very effective to fight fire.
Write a function called type_advantage(attacker, defender) that takes two
Pokémon types as
strings and returns "Super Effective", "Not Very Effective", or "Neutral" based
on
simple type effectiveness rules. Your solution only needs to work for these
three sets of input:
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
'''
def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    elif attacker == "Grass" and defender == "Fire": 
        return "Not Very Effective" 
    elif attacker == "Grass" and defender == "Electric": 
        return "Neutral" 
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Grass", "Fire")) # "Not Very Effective"
print(type_advantage("Grass", "Electric")) # "Neutral"
    
'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare
based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
'''
def ferry_age(age, vehicle): 
    age = int(age)
    if 19 <= age <=64:
        return "Adults (19-64): $10 without a vehicle, $20 with a vehicle."
    elif int (age) >= 65: 
        return "Seniors (65+): $5 without a vehicle, $15 with a vehicle."
    else: 
        return "Free!"
Price = input("Please enter your age to know the price of the ferry")
Vehicle = input("Do you have a vehicle? (yes/no").strip().lower() == "yes"
Result = ferry_age(Price, Vehicle)
print(Result) 
        
'''
#5. Write a function called level_up(experience) that takes a player's experience
points
and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3
'''
def level_up(experience): 
    if experience < 100:
        return "You're level 1!"
    elif experience < 200:
        return "You're level 2!"
    else: 
        return "You're level 3!" 
xp = int(input("Enter the amount of xp you have recieved to know your level:" ))
print(level_up(xp))
    

