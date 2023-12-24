import itertools
import string
import requests
import json
import time

cookie = ''

def fetch_hashtags(keyword):
    url = f"https://www.linkedin.com/voyager/api/graphql?variables=(keywords:{keyword},query:(),type:HASHTAG)&queryId=voyagerSearchDashReusableTypeahead.23c9f700d1a32edbb7f6646dda5e7480"
    headers = {
        "Csrf-Token": "",
        "Cookie": cookie,
        "Accept": "application/vnd.linkedin.normalized+json+2.1"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data for", keyword, ":", response.status_code)
    except Exception as e:
        print("Error fetching data for", keyword, ":", str(e))
    return None

def extract_hashtags(data):
    hashtags = []
    for element in data["data"]["data"]["searchDashReusableTypeaheadByType"]["elements"]:
        hashtag_text = element["title"]["text"]
        hashtags.append(hashtag_text)
    return hashtags

def save_to_file(hashtags, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        for hashtag in hashtags:
            file.write(hashtag + '\n')

# Generate all two-letter combinations
combinations = itertools.product(string.ascii_lowercase, repeat=2)

for combination in combinations:
    keyword = ''.join(combination)
    print("Fetching hashtags for:", keyword)
    data = fetch_hashtags(keyword)
    if data:
        hashtags = extract_hashtags(data)
        save_to_file(hashtags, "linkedin_hashtags.txt")
    time.sleep(0.5)  # Reduced sleep duration
