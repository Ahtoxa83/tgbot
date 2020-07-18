from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest


telephone ='60164364325'
api_id = '1475882'
api_hash = '6af5146321b40a9789698ef41a5b91e3'
session = "anon1"
client = TelegramClient(session, api_id, api_hash)
client.start()
name = "Litecoin_click_bot"

async def main():
    async for message in client.iter_messages(name):
        print(message.sender.username, message.text)
with client:
    client.loop.run_until_complete(main())


