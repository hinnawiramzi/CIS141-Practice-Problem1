'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
it.

Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''
file = open("gardening_tips.txt.txt", "r")
content = file.read()
print(content)
file.close()
'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
while True:
    hike_name = input ("Enter the name of the hike (0 to exit):")
    if hike_name == "0":
        break
    distance = input("Enter the distance of the hike in miles: ")
    file = open("hiking_information", "a")
    file.write(hike_name + " - " + str(distance) + "\n")

file = open("hiking_information", "r")
print(file.read())
file.close()
'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the
frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''
file = open("lyrics.txt.txt", "r")
lyrics = file.read().lower() 
file.close()

user_words = []
for i in range(5):
    words = input("enter word count").lower() 
    user_words.append(words)
   
word_count = {}
for word in user_words:
    count = lyrics.split().count(word) 
    word_count[word] = count 
print(word_count)
print()
'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas.
Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''
file = open("polls.txt.txt", "r")
data_poll = file.read().strip()
votes = data_poll.split(",")
votes = [vote.strip() for vote in votes]

yea_count = votes.count("yea")
nay_count = votes.count("nay") 

print(f" Amount of yea votes: {yea_count}")
print(f" Amount of nay votes: {nay_count}")
