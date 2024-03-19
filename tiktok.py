import requests
import os
import asyncio
import pandas as pd
from TikTokApi import TikTokApi

# ms_tokens=["",
#            "twIoYrgQeZc-N-D2Ltwdzlcd1LM5btYuPAWymr3e3J37MAuReqlb76s6n0A7jjD1loF3m05IA0hD5RLBHk3785yXhIhVuNXxZE19S82gjDVN0r4J6mg0K_WhjVxCECkUIUej_iHdRyv7_ko=&X-Bogus=DFSzswVuSAte-/PStLBEAWRhGwlz"]

ms_token = os.environ.get("dAIQI7YQlAxlPl_zFS9Zf22osbUFeqDvz-2KAqAGN4nv-vjwVTn1648xIknyD5K08uyrZj6z4LyVh-PUVmdjzA86Os_5_UTAvKYMkGx4fyyHLvN3aHZMYpdBM_yT2tiWRXgODbxIDGKEhzw=&X-Bogus=DFSzswVOy8cS4RbotLBquWRhGwUP", None) # get your own ms_token from your cookies on tiktok.com

'''

GOT A NOT IMPLEMENTED ERROR
BRRUUUUUUUUUUUUUUUUUUH

'''

async def trending_videos():
    result = []
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
        async for x in api.hashtag(name='memes').videos(count=1):
            result.append(x.as_dict)
            print(type(x))
            video_bytes = await x.bytes()

            print(type(video_bytes))
            with open("output/saved_video.mp4", 'wb') as file:
                file.write(video_bytes)


        df = pd.DataFrame(result)
        df.to_csv("output/output.csv")

        
          
        

if __name__ == "__main__":
    asyncio.run(trending_videos())
    


