#!/usr/bin/python3

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    # Reddit API endpoint URL for getting hot posts
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    # Add 'after' parameter if it exists
    if after:
        # url += f"&after={after}"
        url += "&after={}".format(after)

    # Make a GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Extract the titles of the hot posts from the JSON response
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if " {} ".format(word.lower()) in " {} ".format(title):
                    if word.lower() in word_count:
                        word_count[word.lower()] += 1
                    else:
                        word_count[word.lower()] = 1

        # Get the 'after' parameter for pagination
        after = data['data']['after']

        # Recursively call the function with the 'after' parameter
        if after:
            count_words(subreddit, word_list, after, word_count)
        else:
            # Print the sorted count of keywords
            sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print("{}: {}".format(word, count))
    else:
        # Print nothing if the subreddit is invalid or the request fails
        return


# Example usage
subreddit = "python"
word_list = ["python", "java", "javascript"]
print("Word count for r/{}".format(subreddit))
count_words(subreddit, word_list)
