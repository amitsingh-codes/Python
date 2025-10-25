#Take a paragraph and show which words appear most often.
sentence = input("Enter the sentence lil bro :")
a = sentence.lower()
list = []
occur = []
count = 0
for word in a.split():
    if word not in list:
        for i in a.split():
            if i == word:
                count = count + 1
        occur.append(count)
        list.append(word)
        count = 0
    else:
        continue
occurance=max(occur)
index = occur.index(occurance)
maxoccur = list[index]
print(f"The most occuring word in the Sentence is {maxoccur} which have repeated {occurance} times")