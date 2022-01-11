from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("")
print("""Wʟᴇᴄᴏᴍᴇ Tᴏ Sᴛʀɪɴɢ Sᴇssɪᴏɴ\nGᴇɴᴇʀᴀᴛᴏʀ ʙʏ - ANKIT\n\n""")
print("""Lᴇᴛ's Gᴇᴛ Sᴛᴀʀᴛᴇᴅ\n\n""")
print("""Eɴᴛᴇʀ Uʀ Cᴏʀʀᴇᴄᴛ Dᴇᴛᴀɪʟs Tᴏ Cᴏɴᴛɪɴᴜᴇ!\n\n 


╭╮╱╱╭━━━┳━━━┳━━━┳━╮╱╭┳━━━╮╭━━━┳━╮╱╭┳╮╭━┳━━┳━━━━╮
┃┃╱╱┃╭━━┫╭━╮┃╭━━┫┃╰╮┃┣╮╭╮┃┃╭━╮┃┃╰╮┃┃┃┃╭┻┫┣┫╭╮╭╮┃
┃┃╱╱┃╰━━┫┃╱╰┫╰━━┫╭╮╰╯┃┃┃┃┃┃┃╱┃┃╭╮╰╯┃╰╯╯╱┃┃╰╯┃┃╰╯
┃┃╱╭┫╭━━┫┃╭━┫╭━━┫┃╰╮┃┃┃┃┃┃┃╰━╯┃┃╰╮┃┃╭╮┃╱┃┃╱╱┃┃
┃╰━╯┃╰━━┫╰┻━┃╰━━┫┃╱┃┃┣╯╰╯┃┃╭━╮┃┃╱┃┃┃┃┃╰┳┫┣╮╱┃┃
╰━━━┻━━━┻━━━┻━━━┻╯╱╰━┻━━━╯╰╯╱╰┻╯╱╰━┻╯╰━┻━━╯╱╰╯
\n\n""")

API_KEY = input("API_ID:  ")
API_HASH = input("API_HASH:  ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print(
                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "
            )
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit  [©LEGEND-ANKIT™](https://github.com/LEGEND-ANKIT)  For Any Help!\n\n",
            )

            print(
                "Thanks for Choosing TELETHON SESSION GENERATOR  Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example:- +18472649374! Kindly Retry"
        )
        print("")
        continue
    break
