
from pip import main
TOKEN= "912206126:AAEIdZo_1jyNzfea9smjfWrB-L2o-pYeNHo"
USER= "@Y7yabot"    
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes  

# Commands
async def start_command(update: Update, contex:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello this is my first botttt!!!!!!")

async def help_command(update: Update, contex:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pls type something so I can help")
        
async def custom_command(update: Update, contex:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("custom!")

#Respones
def handle_responses(text: str) ->str:
    proc= text.lower()
    if "khartoum" in proc:
        from requests import get
        from bs4 import BeautifulSoup as soup
        url="https://www.weather-atlas.com/en/sudan/khartoum"
        rq = get(url, proxies={})
        page=soup(rq.content,"html.parser")
        weather= page.find('li', class_='fs-2').text
        return(f"it is {weather} in khartoum")
    else:
        return("hmmm... :(")
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"user({update.message.chat.id}) in {message_type}:{text}")
    if message_type == "group":
        if USER in text:
            new_text: str = text.replace(USER, "").strip()
            response: str = handle_responses(new_text)
        else:
            return    
    else:
        response: str = handle_responses(text)
    print(f'bot: {response}')    
    await update.message.reply_text(response)




#Commands
if __name__ == "__main__":
    print("starting bot...")
    app=Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

#Messages    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("polling")
    app.run_polling(poll_interval=3)