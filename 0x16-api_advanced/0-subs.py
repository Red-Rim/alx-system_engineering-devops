#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Function to retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the given subreddit, or 0 if the subreddit is invalid.
    """
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "Custom User Agent"}

    # Construct the URL to query subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Make a GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Return the number of subscribers for the subreddit
        return data["data"]["subscribers"]
    else:
        # If the subreddit is invalid or not found, return 0
        return 0

# Test the function
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        print(number_of_subscribers(subreddit_name))

