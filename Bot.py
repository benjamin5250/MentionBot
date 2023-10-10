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

@client.on(events.NewMessage(pattern="^/play ?(.*)")) 
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ဝမ်းနည်းပါတယ်ခင်ဗျာ။ ကချင်ပြည်နယ်၊ လိုင်ဇာမြို့တွင်ဖြစ်ပွားခဲ့သော အပြစ်မဲ့ပြည်သူများနှင့် ကလေးသူငယ်များအား စစ်ကောင်စီမှ ဥပဒေမဲ့ သတ်ဖြတ်မှုနှင့်ပတ်သတ်ပြီး Purple Planet မှ ပြည်သူများနှင့်အတူ ရပ်တည်လျှက်ရှိပါတယ်၊ ဝမ်းနည်းမှုအထိမ်းအမှတ်အဖြစ် Group Profile Picture ပြောင်းလဲကာ၊ Music Bot အသုံးပြုခွင့်အား ၂၄နာရီရပ်နားထားမည်ဖြစ်ပါသည်။")
    helptext = "ဝမ်းနည်းပါတယ်ခင်ဗျာ။ ကချင်ပြည်နယ်၊ လိုင်ဇာမြို့တွင်ဖြစ်ပွားခဲ့သော အပြစ်မဲ့ပြည်သူများနှင့် ကလေးသူငယ်များအား စစ်ကောင်စီမှ ဥပဒေမဲ့ သတ်ဖြတ်မှုနှင့်ပတ်သတ်ပြီး Purple Planet မှ ပြည်သူများနှင့်အတူ ရပ်တည်လျှက်ရှိပါတယ်၊ ဝမ်းနည်းမှုအထိမ်းအမှတ်အဖြစ် Group Profile Picture ပြောင်းလဲကာ၊ Music Bot အသုံးပြုခွင့်အား ၂၄နာရီရပ်နားထားမည်ဖြစ်ပါသည်။"
    await event.reply(
        helptext,
        link_preview=False )

print(">> PurplePlanet MENTION IS WORKING <<")
client.run_until_disconnected()


# A Powerful Music And Management Bot
# Property Of Rocks Indian Largest Chatting Group
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali + Harshit Sharma + Abhimanyu Singh + Krishna Ki Diwani
