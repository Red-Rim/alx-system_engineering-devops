#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    try:
        url = ("https://www.reddit.com/r/{}/"
               "about.json").format(subreddit)
        headers = {
            "User-Agent": "Linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-200 status codes
        data = response.json().get("data")
        return data.get("subscribers")
    except requests.exceptions.RequestException as e:
        if isinstance(e, requests.exceptions.HTTPError) and \
                e.response.status_code == 404:
            print(f"Error: Subreddit '{subreddit}' not found.")
        else:
            print("Error connecting to Reddit's API:", e)
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(f"Number of subscribers for '{subreddit}': {subscribers}")
