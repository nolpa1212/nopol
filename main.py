#_________________________Import___________________________________
from datetime import datetime
from random import choice
from aiocron import crontab
from pyrogram import Client, idle
from pytz import timezone
#_________________________api___________________________________
api_id = 19712680
api_hash = "e04fc66fe35fbed6b57c8eeb6fddfb22"

time_zone = timezone("Asia/Tehran")
#_________________________font___________________________________
fonts = [
    ["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
    ["𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", "𝟞", "𝟟", "𝟠", "𝟡"],
    ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["0", "❶", "❷", "❸", "❹", "➄", "➅", "➆", "❽", "❾"],
    
]
#_________________________time___________________________________
app = Client(
    "ALPHATRICK",
    api_id,
    api_hash,
)


@crontab("*/1 * * * *", tz=time_zone, start=False)
async def change_name():
    table = str.maketrans("0123456789", "".join(choice(fonts)))
    time = datetime.now(time_zone).strftime("%H:%M")
    biot = "پروکسی پرسرعت | Fast proxy | @mtproxy_pain 🄿🄰🄸🄽 🄵🄾🅁 🄴🅅🄴🅁 🄿🄰🄸🄽"
    await app.update_profile(last_name=time.translate(table),bio=biot.format(time.translate(table)))
if __name__ == "__main__":
    app.start()
    change_name.start()
    idle()
    change_name.stop()
    app.stop()
#_____________________________________end_________________
#@YehPHP
#@ALPHA_TRICK
#اسکی بدون میری منبع بزن