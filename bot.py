

import discord
import asyncio


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

#-------OPENING THE DATABASE---------------------------------------------------------
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/cezar/discord_bot/gspread_creds/client_secret.json', scope)
client = gspread.authorize(creds)
disc_commands = client.open("discord_database").sheet1
#------------------------------------------------------------------------------------

#-------VARIABLES--------------------------------------------------------------------

MAX_COMMANDS = int(disc_commands.cell(1,1).value)
INDEX_START = 4             #   where does the actual database start
INDEX_ROW = 1               #   row for extracting the index
NAME_ROW = 2                #   row for extracting the name
DESCRIPTION_ROW = 3         #   row for extracting the description
COMMAND_ROW = 4             #   row for extracting the command name
CODE_ROW = 5                #   row for extracting the command code
client = discord.Client(command_prefix = '!')   #   actual client
teststring = ''


#------------------------------------------------------------------------------------

#-------FUNCTIONS--------------------------------------------------------------------

def check_command(MESSAGE):
    com_iterator = 0
    found_command = 0
    while com_iterator < MAX_COMMANDS:
        if MESSAGE == disc_commands.cell(INDEX_START + com_iterator, COMMAND_ROW).value:
            teststring = disc_commands.cell(INDEX_START + com_iterator, CODE_ROW).value
            found_command = 1
            print(teststring)
            break  
        else:
            com_iterator += 1         
    if (found_command == 0):
        teststring = 'Unknown command. Try !help for more help.'
    return teststring


async def nyez(message : discord.message):
    await client.send_message(message.channel, 'nyez')
            
#------------------------------------------------------------------------------------     
    
#-------BODY-------------------------------------------------------------------------
@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('-------------')
    print('')

@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel, 'Help not available yet.')
    elif message.content.startswith('!nyez'):
        await nyez(message)
    elif message.content.startswith('!'):
        # check_command(message.content[1:])
        # com_iterator = 0
        # found_command = False
        # MESSAGE = message.content[1:]
        # while com_iterator < MAX_COMMANDS:
        #     if MESSAGE == disc_commands.cell(INDEX_START + com_iterator, COMMAND_ROW).value:
        #         teststring = disc_commands.cell(INDEX_START + com_iterator, CODE_ROW).value
        #         found_command = True
        #         print(teststring)
        #         break
        #     com_iterator += 1
        # if (found_command == False):
        #     teststring = 'Unknown command. Try !help for more help.'
        await client.send_message(message.channel, check_command(message.content[1:]))

client.run('MzUzNjE3MTc2NzkzNzEwNjEy.DIyULg.7J9_CWDYHr2PGeFJWmnPhRLV8BU')
#--------------------------------------------------------------------------------------





# client = discord.Client()


# @client.event
# async def on_ready():
#     print('Logged in as')
#     print(client.user.name)
#     print(client.user.id)
#     print('------')


# @client.event
# async def on_message(message):
#     if message.content.startswith('!help'):
#         await client.send_message(message.channel, '--help--')
#     elif message.content.startswith('!dick'):
#         dick = message.content[6:]
#         messagedick = ''.join(['http://www.marimea.xyz/', dick])
#         await client.send_message(message.channel, messagedick)
#     elif message.content.startswith('!biblia'):
#         await client.send_message(message.channel, 'https://biblia.resursecrestine.ro/')
#     elif message.content.startswith('!ragaie'):
#         await client.send_message(message.channel, 'Ragai ca un porc. :                                ^)')
#     elif message.content.startswith('!say'):
#         saymessage = message.content[5:]
#         await client.send_message(message.channel, saymessage.upper())
#     elif message.content.startswith('!muie_la_republica'):
#         await client.send_message(message.channel, 'Cei ce doresc rau republicii sug pula pe vecie!')
#     elif message.content.startswith('!'):
#         await client.send_message(message.channel, 'Unknown command. Type !help for help.')

# client.run('MzUzNjE3MTc2NzkzNzEwNjEy.DIyULg.7J9_CWDYHr2PGeFJWmnPhRLV8BU')




    		
# https://discordapp.com/oauth2/authorize?&client_id=%7Bbot-id%7D&scope=%7Bscope%7D&permissions=%7Bpermissions%7D&response_type=code









