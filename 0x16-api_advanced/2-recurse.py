#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[], after=None):
    # Reddit API endpoint URL for getting hot posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)

    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    # Add 'after' parameter if it exists
    if after:
        url += "&after={}".format(after)

    # Make a GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Extract the titles of the hot posts from the JSON response
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        # Get the 'after' parameter for pagination
        after = data['data']['after']

        # Recursively call the function with the 'after' parameter
        if after:
            recurse(subreddit, hot_list, after)
        else:
            # Return the hot_list when no more pages are available
            return hot_list
    else:
        # Return None if the subreddit is invalid or the request fails
        return None


# Example usage
subreddit = "python"
hot_articles = recurse(subreddit)
if hot_articles is not None:
    print("Hot articles in r/{}:".format(subreddit))
    for index, title in enumerate(hot_articles, start=1):
        print("{}. {}".format(index, title))
else:
    print("Invalid subreddit or no results found.")
