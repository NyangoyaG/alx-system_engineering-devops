import requests

def fetch_hot_articles(subreddit):
    try:
        response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json", headers={"User-Agent": "Reddit Keyword Counter"})
        response.raise_for_status()
        return [article['data']['title'] for article in response.json()['data']['children']]
    except requests.RequestException as e:
        print(f"Error fetching hot articles for subreddit {subreddit}: {e}")
        return []

def count_words_in_titles(titles, word_list, word_counts):
    if not titles:
        sorted_words = sorted(
            [word for word in word_counts.keys() if word_counts[word] > 0],
            key=lambda word: (-word_counts[word], word)
        )
        for word in sorted_words:
            print(f"{word}: {word_counts[word]}")
        return

    title = titles.pop(0)
    words = [word.lower() for word in title.split() if word.isalpha()]

    for word in words:
        if word in word_list:
            word_counts[word] = word_counts.get(word, 0) + 1

    count_words_in_titles(titles, word_list, word_counts)

def count_words(subreddit, word_list):
    lower_cased_word_list = [word.lower() for word in word_list]
    word_counts = {}
    
    titles = fetch_hot_articles(subreddit)
    count_words_in_titles(titles, lower_cased_word_list, word_counts)

# Example usage:
count_words('programming', ['javascript', 'java', 'python'])
