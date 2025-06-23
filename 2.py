import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import string

df = pd.read_csv("C:/Users/hp/Downloads/spam.csv", encoding='latin-1')
df = df[['v1', 'v2']]
df.columns = ['label', 'message']
df['message_length'] = df['message'].apply(len)

label_counts = df['label'].value_counts()

plt.bar(label_counts.index, label_counts.values, color=['green', 'red'])
plt.title('Spam vs Ham Count')
plt.xlabel('Label')
plt.ylabel('Count')
plt.show()

ham_lengths = df[df['label'] == 'ham']['message_length']
spam_lengths = df[df['label'] == 'spam']['message_length']

plt.hist(ham_lengths, bins=40, alpha=0.7, label='Ham', color='blue')
plt.hist(spam_lengths, bins=40, alpha=0.7, label='Spam', color='orange')
plt.title("Histogram of Message Lengths")
plt.xlabel("Message Length")
plt.ylabel("Frequency")
plt.legend()
plt.show()

spam_text = " ".join(df[df['label'] == 'spam']['message']).translate(str.maketrans('', '', string.punctuation))
ham_text = " ".join(df[df['label'] == 'ham']['message']).translate(str.maketrans('', '', string.punctuation))

spam_wc = WordCloud(width=600, height=400, background_color='white').generate(spam_text)
ham_wc = WordCloud(width=600, height=400, background_color='white').generate(ham_text)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(spam_wc, interpolation='bilinear')
plt.title("Spam Word Cloud")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(ham_wc, interpolation='bilinear')
plt.title("Ham Word Cloud")
plt.axis('off')
plt.show()

print("\nAverage message length (Ham):", ham_lengths.mean())
print("Average message length (Spam):", spam_lengths.mean())
print("Max message length:", df['message_length'].max())
print("Min message length:", df['message_length'].min())
