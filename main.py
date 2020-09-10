from collections import Counter
import nltk
from commits_github import get_commits_messages

if __name__ == '__main__':
    nltk.download('stopwords')
    nltk.download('punctuation')

    messages = get_commits_messages(user='JetBrains', repo='kotlin')

    text = ' '.join(messages)
    text = text.lower()  # Not specified by task, but usually frequency is shown for lowered text

    tokens = nltk.word_tokenize(text)

    remove_stopwords = True
    remove_non_letters = True

    if remove_stopwords:
        set_stopwords = set(nltk.corpus.stopwords.words('english'))
        tokens = list(filter(lambda word: word not in set_stopwords, tokens))
    if remove_non_letters:
        tokens = list(filter(lambda word: word.isalpha(), tokens))

    print(*Counter(tokens).most_common(n=30), sep='\n')
