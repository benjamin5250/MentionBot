# A Powerful Music And Management Bot
# Property Of Rocks Indian Largest Chatting Group
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali + Kattai Massom + Abhimanyu Singh


import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(
    level=logging.INFO, format="%(name)s - [%(levelname)s] - %(message)s"
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", ""))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("TOKEN", "")
client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)
spam_chats = []


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("I'm not dead 😎")

@client.on(events.NewMessage(pattern="^/update ?(.*)")) 
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("မင်္ဂလာပါခင်ဗျာ ... Group Music Bot အား ပြန်လည်အသုံးပြုနိုင်ပြီဖြစ်ပါသည်။")
    helptext = "မင်္ဂလာပါခင်ဗျာ... Group Music Bot အား ပြန်လည်အသုံးပြုနိုင်ပြီဖြစ်ပါသည်။"
    await event.reply(
        helptext,
        link_preview=False )

@client.on(events.NewMessage(pattern="^/nocp ?(.*)")) 
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("Group ထဲတွင် အသက်မပြည့်သေးသော ကလေးသူငယ်များနှင်ပတ်သတ်သည့် ပုံများ၊ စာများ၊ Group/Channel များ၊ link များ မျှဝေဖြန့်ဖြူးခြင်းပြုလုပ်ပါက Group မှထုတ်ပယ်ပါမည်။")
    helptext = "Group ထဲတွင် အသက်မပြည့်သေးသော ကလေးသူငယ်များနှင်ပတ်သတ်သည့် ပုံများ၊ စာများ၊ Group/Channel များ၊ link များ မျှဝေဖြန့်ဖြူးခြင်းပြုလုပ်ပါက Group မှထုတ်ပယ်ပါမည်။"
    await event.reply(
        helptext,
        link_preview=False )

@client.on(events.NewMessage(pattern="^/pppl ?(.*)")) 
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("Group ထဲတွင် အသက်မပြည့်သေးသော ကလေးသူငယ်များနှင်ပတ်သတ်သည့် ပုံများ၊ စာများ၊ Group/Channel များ၊ link များ မျှဝေဖြန့်ဖြူးခြင်းပြုလုပ်ပါက Group မှထုတ်ပယ်ပါမည်။")
    helptext = "Group ထဲတွင် အသက်မပြည့်သေးသော ကလေးသူငယ်များနှင်ပတ်သတ်သည့် ပုံများ၊ စာများ၊ Group/Channel များ၊ link များ မျှဝေဖြန့်ဖြူးခြင်းပြုလုပ်ပါက Group မှထုတ်ပယ်ပါမည်။"
    await event.reply(
        helptext,
        link_preview=False )

print(">> PurplePlanet MENTION IS WORKING <<")
client.run_until_disconnected()


# A Powerful Music And Management Bot
# Property Of Rocks Indian Largest Chatting Group
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali + Harshit Sharma + Abhimanyu Singh + Krishna Ki Diwani
