import telepot
from decouple import config

#colocar a id do bot nessa parte
bot = telepot.Bot(config('bot_name'))

#comece com a id do seu telegram e depois o conteudo que vc quiser
bot.sendMessage(config('id_telegram'),'testando mandar foto')
bot.sendPhoto(config('id_telegram'),photo=open("link_para_foto","rb"))