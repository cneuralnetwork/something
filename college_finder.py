import requests
import json
import csv

rated_users_url = "https://codeforces.com/api/user.ratedList?activeOnly=false&includeRetired=true"

rated_users_response = requests.get(rated_users_url)
rated_users_data = json.loads(rated_users_response.text)
rs = rated_users_data["result"]

users = []
tags=[] //fill tags here

for it in rs:
    if (('organization' in it) and
        (it['organization'] in tags) and
        (it['maxRating'] >= 0)):
        users.append(it)
        print("chk")

csv_filename = 'iiest_cf_users.csv'

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = [
        'firstName',
        'lastName',
        'handle',
        'organization',
        'rating',
        'maxRating',
        'rank',
        'maxRank'
    ]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for user in users:
        user_data = {
            'firstName': user.get('firstName', ''),
            'lastName': user.get('lastName', ''),
            'handle': user.get('handle', ''),
            'organization': user.get('organization', ''),
            'rating': user.get('rating', ''),
            'maxRating': user.get('maxRating', ''),
            'rank': user.get('rank', ''),
            'maxRank': user.get('maxRank', '')
        }
        writer.writerow(user_data)

print(f"Saved {len(iiest_users)} users to {csv_filename}")
