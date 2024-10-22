#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers
for a given subreddit. If the subreddit is invalid, it returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for
    a given subreddit. If the subreddit is invalid, return 0.

    Args:
        subreddit (str): The subreddit to search for

    Returns:
        int: Number of subscribers or 0 if invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            # Return the number of subscribers or 0 if the key is missing
            return data['data'].get('subscribers', 0)
        else:
            # Return 0 if the subreddit is invalid (non-200 response)
            return 0
    except requests.RequestException:
        # Return 0 in case of network-related issues
        return 0


if __name__ == "__main__":
    # Testing can be done using the 0-main.py script
    pass
