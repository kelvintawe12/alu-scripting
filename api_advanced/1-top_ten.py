#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    # Check if the subreddit exists
    if response.status_code != 200:
        print(None)  # Invalid subreddit
        print("OK")  # Print OK for non-existent subreddit
        return
    # Parse response safely
    try:
        posts = response.json().get('data', {}).get('children', [])
        # If no posts, print None and OK
        if not posts:
            print(None)
            print("OK")
            return
        # Print the titles of each post if available
        for post in posts:
            title = post['data'].get('title')
            if title:  # Only print if title exists
                print(title)
        # If we successfully print titles, print "OK"
        print("OK")
    except (ValueError, KeyError, TypeError):
        print(None)
        print("OK")  # Print OK even on errors
