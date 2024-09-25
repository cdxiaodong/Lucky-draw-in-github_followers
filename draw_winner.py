import requests
from bs4 import BeautifulSoup
import random

username = "cdxiaodong"
page = 1
followers = []

while True:
    followers_url = f"https://github.com/{username}?page={page}&tab=followers"
    print(f"Fetching page {page} from {followers_url}")
    response = requests.get(followers_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        current_followers = soup.find_all('span', class_='Link--secondary')
        
        if not current_followers:
            print(f"No more followers found on page {page}")
            break
        
        followers.extend([follower.text.strip() for follower in current_followers])
        print(f"Found {len(current_followers)} followers on page {page}")
        
        next_page_link = soup.find('a', {'class': 'next_page'})
        if not next_page_link:
            print("No next page link found")
            break
        
        page += 1
    else:
        print(f"Failed to retrieve followers. Status code: {response.status_code}")
        break

print("All followers:")
for follower in followers:
    print(follower)

target_name = "AnneLau"
filtered_followers = []

for follower in followers:
    if follower == target_name:
        break
    filtered_followers.append(follower)

print(f"\nFiltered followers before '{target_name}':")
for follower in filtered_followers:
    print(follower)

if filtered_followers:
    winner = random.choice(filtered_followers)
    print(f"\nThe winner is: {winner}")
else:
    print("\nNo followers found before the target name.")
