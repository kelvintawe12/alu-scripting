#!/usr/bin/python3
"""
Module to query the Reddit API and count keyword occurrences in titles.
"""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursively fetch hot posts and count keyword occurrences.

    Args:
        subreddit (str): Subreddit name.
        word_list (list): Keywords to count.
        word_count (dict): Keyword counts.
        after (str): Pagination token.

    Returns:
        None
    """
    # API URL for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'after': after, 'limit': 100}  # Max 100 posts

    # Fetch posts
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return  # Invalid subreddit

        # Parse JSON data
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after', None)

        # Initialize word counts
        if not word_count:
            word_list = [word.lower() for word in word_list]  # Normalize words
            word_count = {word: 0 for word in word_list}

        # Count keywords in titles
        for post in posts:
            title = post.get('data', {}).get('title', "").lower()
            for word in word_list:
                word_count[word] += title.split().count(word)

        # Recursive call if more pages exist
        if after is not None:
            return count_words(subreddit, word_list, word_count, after)
        else:
            # Sort and print results
            sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")
            return

    except requests.RequestException:
        return  # Handle exceptions gracefully


if __name__ == "__main__":
    # Test using the 3-main.py script
    pass
