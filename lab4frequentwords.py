import re
import matplotlib.pyplot as plt
alicefile= open('/users/ICT LAPTOP/Desktop/AI/alice.txt','r')
filelines=alicefile.read().lower()


def word_count(x):
    """Function to count the frequency of words using a regex to find all whole words in alice file with characters between 2-20"""
    count=dict()
    words=re.findall(r'\b[a-z]{2,20}\b',x)
    for word in words:
        if word in count:
            count[word] +=1
        else:
            count[word] =1
    return count
#Dictionary countaining words and there frequncy values
words_frequency=(word_count(filelines))

#Dictionary countaining words appearing more than 100 times
frequent_words={k:v for (k,v) in words_frequency.items() if v > 100}
# Plot histogram using matplotlib bar().
plt.bar(range(len(frequent_words)), frequent_words.values())
plt.xticks(range(len(frequent_words)), frequent_words.keys(),rotation=-60)
plt.title('Histogram of Frequency of words')
plt.xlabel('Words')
plt.ylabel('Frequency')

plt.show()
