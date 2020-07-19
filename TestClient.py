from telethon import TelegramClient

telephone ='xxxx5'
api_id = 'xxxx'
api_hash = 'xxxx'
session = "xxxxx"
client = TelegramClient(session, api_id, api_hash)
client.start()
name = "Litecoin_click_bot"

async def main():
    async for message in client.iter_messages(name):
        print(message.sender.username, message.text)
with client:
    client.loop.run_until_complete(main())


