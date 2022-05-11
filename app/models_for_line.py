from app import handler
from app.custom_models import AlmaTalks

from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage, MemberJoinedEvent, Sender
)

# 個別用戶學說話
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	if event.source.type == 'user':  #判斷是否來自user
   		 AlmaTalks.default_reply(event)

# Join event (觸發)加入事件
@handler.add(MemberJoinedEvent)
def handle_memberJoined(event):
	if event.source.type == 'group':  #判斷是否來自群組
		AlmaTalks.join_reply(event)	      #回覆