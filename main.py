import requests
import os
import asyncio
import pandas as pd
from TikTokApi import TikTokApi

# ms_tokens=["",
#            "twIoYrgQeZc-N-D2Ltwdzlcd1LM5btYuPAWymr3e3J37MAuReqlb76s6n0A7jjD1loF3m05IA0hD5RLBHk3785yXhIhVuNXxZE19S82gjDVN0r4J6mg0K_WhjVxCECkUIUej_iHdRyv7_ko=&X-Bogus=DFSzswVuSAte-/PStLBEAWRhGwlz"]

ms_token = os.environ.get("dAIQI7YQlAxlPl_zFS9Zf22osbUFeqDvz-2KAqAGN4nv-vjwVTn1648xIknyD5K08uyrZj6z4LyVh-PUVmdjzA86Os_5_UTAvKYMkGx4fyyHLvN3aHZMYpdBM_yT2tiWRXgODbxIDGKEhzw=&X-Bogus=DFSzswVOy8cS4RbotLBquWRhGwUP", None) # get your own ms_token from your cookies on tiktok.com


async def trending_videos():
    result = []
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
        async for video in api.hashtag(name='memes').videos(count=5):
            result.append(video.as_dict)
        df = pd.DataFrame(result)
        print(df["id"][0])
        async for v in df["id"]:
            video_bytes = api.video(id=v).bytes()
            # Saving The Video
            with open('saved_video.mp4', 'wb') as output:
                output.write(video_bytes)

if __name__ == "__main__":
    asyncio.run(trending_videos())


