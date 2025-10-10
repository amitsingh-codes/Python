#Take a sentence as input and decide if it’s positive, negative, or neutral based on words/emojis. 

# String -> I am Amit . I Love coding and I feel very HAPPY while solving problems 😍 , I am a part of Geek room in AI department 😍 , I love being a part of it , I hate only one thing "Theory" it just feels boring 😫 but again I believe the thing which makes you sad makes you happy in long run.

count = 0
sentence = input("Enter a sentence with emojis: ") 
mood_dict = {"love": 1, "😍": 1, "happy": 1, "hate": -1, "😫": -1, "sad": -1} 
sent_low=sentence.lower()

for word in sent_low.split(" "):
    if  word in mood_dict:
            count = count + mood_dict[word]
print(count)
if count>0:
    print("The overall mood is Positive")
elif count<0:
    print("The overall mood is Negative")
else :
    print("The overall mood is Neutral")