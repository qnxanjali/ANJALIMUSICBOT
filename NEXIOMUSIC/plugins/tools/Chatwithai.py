import requests
from pyrogram import Client, filters
from pyrogram.enums import ChatAction, ParseMode
from AnonxMusic import app

@app.on_message(filters.command("ask"))
async def fetch_med_info(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("Please provide a query to ask.")
        return

    await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)


    api_url = f"https://chatwithai.codesearch.workers.dev/?chat={query}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            reply = data.get("data", "Sorry, I couldn't fetch the data.")
        else:
            reply = "Failed to fetch data from the API."
    except Exception as e:
        reply = f"An error occurred: {e}"

    await message.reply_text(reply)

@app.on_message(filters.mentioned & filters.group)
async def fetch_med_info(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("Please provide a medical query to ask.")
        return

    await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    api_url = f"https://chatwithai.codesearch.workers.dev/?chat={query}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            reply = data.get("data", "Sorry, I couldn't fetch the data.")
        else:
            reply = "Failed to fetch data from the API."
    except Exception as e:
        reply = f"An error occurred: {e}"

    await message.reply_text(reply)
