from mastodon import Mastodon
import mimetypes, httpx, os
from dotenv import load_dotenv
load_dotenv()

def mastodon(post):
     mastodon = Mastodon(
     access_token = os.environ.get("MAST_TOKEN"),
     api_base_url = 'https://mastodon.social'
     )
     try:
          i = httpx.get(post["image"]).content
          mime = mimetypes.guess_type(post["image"], strict=True)[0]
          media_ids = mastodon.media_post(i, mime, description=f'{post["title"]}')["id"]
          media_ids = [media_ids]
          content = f'New meme by {post["submitter"]}!\n{post["title"]} - {post["text"]}\n{post["href"]}'
          mastodon.status_post(content, media_ids=media_ids)
          print(f'Posted {post["id"]} to Mastodon @wownero')
     except Exception as e:
          print(e)