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
    ["đŹ", "đ­", "đŽ", "đŻ", "đ°", "đą", "đ˛", "đł", "đ´", "đľ"],
    ["đ", "đ", "đ", "đ", "đ", "đ", "đ", "đ", "đ ", "đĄ"],
    ["â", "â", "â", "â", "â", "â", "â", "â", "â", "â"],
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["0", "âś", "âˇ", "â¸", "âš", "â", "â", "â", "â˝", "âž"],
    
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
    biot = "ŮžŘąŮÚŠŘłŰ ŮžŘąŘłŘąŘšŘŞ | Fast proxy | @mtproxy_pain đżđ°đ¸đ˝ đľđžđ đ´đđ´đ đżđ°đ¸đ˝"
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
#Ř§ŘłÚŠŰ Ř¨ŘŻŮŮ ŮŰŘąŰ ŮŮŘ¨Řš Ř¨Ř˛Ů