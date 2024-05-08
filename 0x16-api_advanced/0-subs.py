#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    # Reddit API endpoint URL for getting subreddit information
    # url = f"https://www.reddit.com/r/{subreddit}/about.json
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    # Make a GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Extract the number of subscribers from the JSON response
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Return 0 if the subreddit is invalid or the request failed
        return 0


subreddit = "python"
print("Sub in r/{}: {}".format(subreddit, number_of_subscribers(subreddit)))
