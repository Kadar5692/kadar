import telepot

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    print('Received: %s' % command)
    
    if command == '/start':
        bot.sendMessage(chat_id, 'Hello!')
        
TOKEN = '6143405797:AAGEKmOduaBoAGachMfrs_P-PHm2CV-VTJo'
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('I am legend...')

# Keep the program running.
while True:
    pass
