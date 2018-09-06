import read
from collections import Counter

df = read.load_data()
finalstring = ""
for index, row in df.iterrows():
    finalstring += (str(row['headline']) + " "
    
finalstring = finalstring.lower()
words = finalstring.split(" ")

hundred_words=Counter(words).most_common(100)
print(hundred_words)