import httpx, time, modules, os
from dotenv import load_dotenv
from supabase import create_client, Client
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def scraper():
    list = httpx.get("https://suchwow.xyz/api/list").json()
    for item in list:
        try:
            supabase.table("suchmeme").insert(item).execute()
            print(f'Inserted meme {item["id"]} to Supabase DB')
            post(item)
        except Exception:
            continue

def post(item):
    modules.mastodon(item)

while True:
    scraper()
    print("Done")
    time.sleep(60)