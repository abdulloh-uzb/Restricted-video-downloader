import asyncio
from telethon import TelegramClient

api_id = API_ID
api_hash = API_HASH

client = TelegramClient('session_name', api_id, api_hash)


async def main():

    await client.start()
    video_url = input("url: ")

    message_id = int(video_url.split("/")[-1])
    chat_id = "-100" + video_url.split("/")[-2]
    
    message = await client.get_messages(int(chat_id), ids=message_id)

    def callback(current, total):
        total = total//(1024*1024)
        current = current//(1024*1024)
        print(total, 'dan', current, "yuklandi", 'bytes: {:.2%}'.format(current / total))

    await client.download_media(message, progress_callback=callback)

    await client.disconnect()


asyncio.run(main())