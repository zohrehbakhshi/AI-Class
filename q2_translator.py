words={
    "I": "من",
    "love": "دوست دارم",
    "Python": "پایتون",
    "and": "و",
    "ai": "هوش مصنوعی",
    "hello": "سلام",
    "book": "کتاب",
    "computer": "کامپیوتر",   
}

sentence="I love python and Ai"

transelated_words=[]

for word in sentence.lower().split():
    if word in words:
        transelated_words.append(words[word])
    else:
        transelated_words.append("["+ word +"]")

print("".join(transelated_words))

transelated_count=0
not_transelated_count=0

for word in sentence.lower().split():
    if word in words:
        transelated_count+=1
    else:
        not_transelated_count+=1    

print("Number of Translated Words:", transelated_count)
print("Number of Not Translated Words:", not_transelated_count)
