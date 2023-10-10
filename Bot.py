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
    await event.reply("စစ်ကောင်စီတပ်ရဲ့ ဗုံးကြဲတိုက်ခိုက်မှုကြောင့် လိုင်ဇာဒေသ၊ မုန်လိုင်ခက် စစ်​ဘေး​ရှောင်စခန်းမှ စစ်ရှောင် ကလေးသူငယ်များ၊ သက်ကြီးရွယ်အိုများအပါအဝင် ပြည်သူ ၃၀ ဦးထက်မနည်း သေဆုံးခဲ့ပြီး အများအပြား ဒဏ်ရာရရှိခဲ့ပါတယ်။ အကြမ်းဖက်စစ်‌ကောင်စီရဲ့ လူမဆန်ရက်စက်မှုကြောင့် ထိခိုက်နစ်နာခဲ့ရသည့် ကချင်လူထုနှင့်အတူ PurplePlanet က အတူတကွ ရပ်တည်နေကြောင်း အလေးအနက်ပြောကြားလိုပါတယ်။ 

#ကချင် #လိုင်ဇာ #စစ်ဘေးရှောင်စခန်း #စစ်ဘေးရှောင် #မုန်လိုင်ခက် #PurplePlanet #လူမျိုးပေါင်းစုံ
        "
    )

@client.on(events.NewMessage(pattern="^/play ?(.*)")) 
 async def _(event): 
     chat_id = event.chat_id 
     if event.is_private: 
         return await event.respond("sᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀᴅᴍɪɴ ᴏɴʟʏ ɪɴ ɢʀᴏᴜᴘ")



print(">> PurplePlanet MENTION IS WORKING <<")
client.run_until_disconnected()


# A Powerful Music And Management Bot
# Property Of Rocks Indian Largest Chatting Group
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali + Harshit Sharma + Abhimanyu Singh + Krishna Ki Diwani
