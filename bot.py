

import discord
import asyncio

# discord.opus.load_opus('libopus.so.0')

client = discord.Client()

# async def joinVoiceChannel(): 
#     channel = client.get_channel('353614499019751427')
#     voice = await client.join_voice_channel(channel)
#     print('Bot joined voice channel')

async def client_disconnect():
    client.voice.disconnect()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Pong!')
    elif message.content.startswith('!check_bot'):
        await client.send_message(message.channel, 'Bot is running.')
    elif message.content.startswith('!help'):
        await client.send_message(message.channel, '--help--')
    # elif message.content.startswith('!voice'):
    #     await joinVoiceChannel()
    #     await client.send_message(message.channel, 'voice activated')
    # elif message.content.startswith('!disconnect'):
    #     await client_disconnect()
    #     await client.send_message(message.channel, 'disconnected')
    elif message.content.startswith('!dick'):
        dick = message.content[6:]
        # dick = "%20".join(dick.split(" "))
        messagedick = ''.join(['http://www.marimea.xyz/', dick])
        await client.send_message(message.channel, messagedick)

    elif message.content.startswith('!biblia'):
        await client.send_message(message.channel, 'https://biblia.resursecrestine.ro/')

    elif message.content.startswith('!'):
        await client.send_message(message.channel, 'Unknown command. Type !help for help.')

client.run('MzUzNjE3MTc2NzkzNzEwNjEy.DIyULg.7J9_CWDYHr2PGeFJWmnPhRLV8BU')




    		
# https://discordapp.com/oauth2/authorize?&client_id=%7Bbot-id%7D&scope=%7Bscope%7D&permissions=%7Bpermissions%7D&response_type=code










