#!/usr/bin/python3

import requests


def top_ten(subreddit):
    # Reddit API endpoint URL for getting hot posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    # Make a GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Extract the titles of the hot posts from the JSON response
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        # Print None if the subreddit is invalid or the request fails
        print(None)


subreddit = "python"
print("Top 10 hot posts in r/{}:".format(subreddit))
top_ten(subreddit)
