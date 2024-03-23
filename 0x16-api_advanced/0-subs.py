#!/usr/bin/python3
"""
number of subscribers 'How Many Subs?'
"""


import requests as req
headers = {"User-Agent": "User_Agent_/3.0"}


def number_of_subscribers(subreddit):
    """Method Subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = req.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    return 0
