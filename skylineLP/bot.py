# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from cl.test import comprova_mis
from skyline import Skyline
from cl.SkylineVisitor import SkylineVisitor
import pickle

#DEFINICIO FUNCIONS COMANDES

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Benvingut al BotSkylinePocho, si funciona algo dona gracies!")
    visitor = SkylineVisitor()
    context.user_data["visitor"] = visitor
    
def text(update, context):
    #print ("s'ha escrit text")
    missatge = update.message.text
    print (missatge)
    s = Skyline()
    s = comprova_mis(missatge, context.user_data["visitor"])
    
    #print ("mostrar altura i alçada:")
    alcada = s.getAlcada()
    area = s.getArea()
    #print (alcada, area)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('imatge.png', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text=("area: "+str(area)+"\nalçada: "+str(alcada)))
    #print ("FINAL")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= \
    "Comandes:\n\
    /start : inicia la conversa amb el Bot.\n\
    /help : mostra la llista de totes les comandes i una petita explicacio.\n\
    /author : escriu el nom de l’autor del projecte i el seu correu electrònic.\n\
    /lst : mostra els identificadors definits i la seva corresponent àrea.\n\
    /clean : esborra tots els identificadors definits.\n\
    /save id : guarda un skyline definit amb el nom id.sky.\n\
    /load id : carrega un skyline de l’arxiu id.sky.")
    
def author(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= \
        "@ Marc Cervilla Rovira, 2020\n marc.cervilla.rovira@est.fib.upc.edu")
    
def lst(update, context):
    resposta = ""
    for n, s in context.user_data["visitor"].ts.items():
        resposta +="%s: alçada: %d, area: %d\n" % (n, s.alcada, s.area)
    context.bot.send_message(chat_id=update.effective_chat.id, text=resposta)
    
def clean(update, context):
    visitor = SkylineVisitor()
    context.user_data["visitor"] = visitor
    context.bot.send_message(chat_id=update.effective_chat.id, text="clean done")
    
def save_id(update, context):
    id = context.args[0]
    usuari = update.effective_chat.id
    nom = str( os.getcwd() ) + "/" + ( usuari ) + "." + id + ".sky"
    f = open (nom, "wb")
    pickle.dump(context.user_data[id], f)
    f.close()
    context.bot.send_message(chat_id=update.effective_chat.id, text="ID guardat")
    #print ("FIN")
    
def load_id(update, context):
    id = context.args[0]
    usuari = update.effective_chat.id
    nom = str( os.getcwd() ) + "/" + ( usuari ) + "." + id + ".sky"
    f = open (nom, "rb")
    context.user_data[id] = pickle.load(f)
    f.close()
    context.bot.send_message(chat_id=update.effective_chat.id, text="ID cargat")
    #print ("FIN")

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# COMANDES
#quan es rebi una comanda s'executara la seva funcio que esta a dalt
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save_id))
dispatcher.add_handler(CommandHandler('load', load_id))

# MISSATGES
#quan es rebi un missatge s'executara la funcio
dispatcher.add_handler(MessageHandler(Filters.text,text))

# engega el bot
updater.start_polling()