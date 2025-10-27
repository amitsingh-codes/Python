#Take a paragraph and show which words appear most often.
sentence = input("Enter the sentence lil bro :")
a = sentence.lower()
b=list(a)
c=list(a)
i = 0
while i<=len(c):
    try:
        if "." in b :
            b.remove(".")
        elif "," in b:
            b.remove(",")
        elif("!") in b:
            b.remove("!")
        elif("?") in b:
            b.remove("?")
    except ValueError:
        pass
    i+=1
a = ''.join(b)
b = a.split()
list1 = []
occur = []
count = 0
for word in a.split():
    if word not in list1:
        for i in a.split():
            if i == word:
                count = count + 1
        occur.append(count)
        list1.append(word)
        count = 0
    else:
        continue
occurance=max(occur)
index = occur.index(occurance)
maxoccur = list1[index]
print(f"The most occuring word in the Sentence is {maxoccur} which have repeated {occurance} times")