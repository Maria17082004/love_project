from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
import os
from decouple import config

API_ID = config("API_ID")
API_HASH = config("API_HASH")
chat_id = "2492211150"

app = Client(name=config('LOGIN'),
             api_id=config('API_ID'),
             api_hash=config('API_HASH'),
             phone_number=config('PHONE'))

@app.on_chat_member_updated(filters.chat(chat_id))
async def handle_chat_member_update(client, chat_member_updated: ChatMemberUpdated):
    # Получение информации о событии
    user = chat_member_updated.new_chat_member.user
    if chat_member_updated.new_chat_member.status == "member":
        # Сообщение об добавлении участника
      print(f"👤 добавлен в чат.")
    elif chat_member_updated.new_chat_member.status == "left":
              # Сообщение об удалении участника
      print(f"👤 покинул чат.")
    elif chat_member_updated.new_chat_member.status == "administrator":
              # Сообщение о повышении участника до администратора
      print(f"👑 теперь администратор.")
    elif chat_member_updated.new_chat_member.status == "restricted":
              # Сообщение о понижении участника до ограниченного
      print(f"🔒 теперь ограничен в правах.")

app.run()


