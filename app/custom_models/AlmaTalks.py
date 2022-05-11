from app import line_bot_api

from linebot.models import (
TextSendMessage, Sender
)

from linebot.exceptions import LineBotApiError
from linebot.models.emojis import Emojis


def default_reply(event):
    name = line_bot_api.get_profile(event.source.user_id).display_name
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"Hello {name}!")

        )


def join_reply(event):
    line_bot_api.reply_message(
        event.reply_token,
		TextSendMessage(text=f"歡迎新朋友~👏🎉\n\n1️⃣《盒買+1》是屬於《甜蜜秘境》品牌的團購服務\n針對所有各類包裝盒有微量需求的朋友們，相簿內都有商品資訊，可以先看看 👀\n\n2️⃣ 有需要的商品可以直接詢問，會盡力找優惠，幫您省荷包💰 \n \n3️⃣ 想私訊、更瞭解我們或產品的Q&A，請查看記事本 📖 \n \n4️⃣ 訂購下單只要連結 ⬇ ，商品就會送到家 🌸 \n https://forms.gle/QnhqeETJSVeTUHq18 ",
            sender=Sender(
            name="盒買+1機器人",
            icon_url="https://i.imgur.com/hblrp13.jpg")  #來源圖:https://pin.it/7tfmTJR
        )
    )