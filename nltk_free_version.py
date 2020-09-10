"""
If you have problems with nltk, you should use this script. It repeats logic of the main file (a bit simplified)
(nltk require access to saving datasets on your local machine)
"""

from commits_github import get_commits_messages
import re
from collections import Counter

if __name__ == '__main__':
    messages = get_commits_messages(user='JetBrains', repo='kotlin')
    text = ' '.join(messages)
    text = text.lower()
    tokens = re.split('[^a-zA-Z]', text)
    tokens = list(filter(lambda token: token != '', tokens))
    print(*Counter(tokens).most_common(n=30), sep='\n')
