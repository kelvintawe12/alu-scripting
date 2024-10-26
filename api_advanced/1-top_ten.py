#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)  # Print None for non-existent subreddit
        return
    try:
        posts = response.json().get('data', {}).get('children', [])
        if not posts:
            print(None)
            return
        for post in posts[:10]:  # Limit to first 10 posts
            title = post['data'].get('title')
            if title:  # Only print if title exists
                print(title)
    except (ValueError, KeyError, TypeError):
        print(None)
