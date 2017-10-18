

import discord
import asyncio
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#-------OPENING THE DATABASE---------------------------------------------------------
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/cezar/discord_bot/gspread_creds/client_secret.json', scope)
gclient = gspread.authorize(creds)
disc_commands = gclient.open("discord_database").sheet1
#------------------------------------------------------------------------------------

#-------VARIABLES--------------------------------------------------------------------

MAX_COMMANDS = int(disc_commands.cell(1,1).value)
INDEX_START = 4             #   where does the actual database start
INDEX_ROW = 1               #   row for extracting the index
NAME_ROW = 2                #   row for extracting the name
DESCRIPTION_ROW = 3         #   row for extracting the description
COMMAND_ROW = 4             #   row for extracting the command name
CODE_ROW = 5                #   row for extracting the command code
TYPE_ROW = 6                #   row for extracting the type of command
client = discord.Client()   #   actual client


#------------------------------------------------------------------------------------

#-------FUNCTIONS--------------------------------------------------------------------


async def PRINT_HELP(message : discord.message):
    help_message_str = ['The prefix for using this bot is \'!\'', 'For a list of commands, type \'!commands\'', 'https://github.com/cezarmathe/discord_bot is the official github repository for this bot', 'Have fun!']
    await client.send_message(message.channel, help_message_str[0])
    await client.send_message(message.channel, help_message_str[1])
    await client.send_message(message.channel, help_message_str[2])
    await client.send_message(message.channel, help_message_str[3])


async def SEPARATE_ARGS(text):
    return re.compile('\w+').findall(text[1:])


async def print_commands(message : discord.message):
    com_mes = ''
    for i in range(MAX_COMMANDS):
        com_mes = ''.join([str(i + 1), '. ', disc_commands.cell(INDEX_START + i, NAME_ROW).value, ' - !', disc_commands.cell(INDEX_START + i, COMMAND_ROW).value])
        await client.send_message(message.channel, com_mes)


async def CHECK_CUSTOM_COMMAND(message : discord.message):
    com_iterator = 0
    found_command = 0
    MESSAGE = message.content[1:]
    while com_iterator < MAX_COMMANDS:
        if MESSAGE.startswith(disc_commands.cell(INDEX_START + com_iterator, COMMAND_ROW).value):
            com_code = disc_commands.cell(INDEX_START + com_iterator, CODE_ROW).value
            found_command = 1
            command_type = int(disc_commands.cell(INDEX_START + com_iterator, TYPE_ROW).value)
            await DO_CUSTOM_COMMAND(message, com_code, com_iterator, command_type)
            break  
        else:
            com_iterator += 1         
    if (found_command == 0):
        await client.send_message(message.channel, 'Unknown command. Try !help or for more help or !commands for a list of available commands')
  

async def DO_CUSTOM_COMMAND(message : discord.message, command_code, command_number, command_type):
    if command_type == 0:
        await client.send_message(message.channel, command_code)
        return
    else:
        command_args = SEPARATE_ARGS(command_code)
        # to do code interpreting
        return


async def UPDATE_COMMAND_NUMBER(message : discord.message, silent = False):
    MAX_COMMANDS = int(disc_commands.cell(1,1).value)
    if (silent):
        return
    await client.send_message(message.channel, 'Updated commands, there are ' + str(MAX_COMMANDS) + ' commands. Type !commands to see the list.')
        
        
async def CHECK_COMMAND(message : discord.message):
    args = await SEPARATE_ARGS(message.content)
    if (await CHECK_COMMAND_ZERO(args[0], message)):
        return
    else:
        await CHECK_CUSTOM_COMMAND(message)
        return 


async def CHECK_COMMAND_ZERO(arg, message : discord.message):
    if (arg == "help"):
        await PRINT_HELP(message)
        return True
    if (arg == "commands"):
        await print_commands(message)
        return True
    if (arg == "say"):
        await client.send_message(message.channel, message.content[5:].upper())
        return True
    if (arg == "update"):
        await UPDATE_COMMAND_NUMBER(message)
        return True
    if (arg == "spam"):
        spamm = message.content[6:].split()
        for i in range(int(spamm[0])):
            await client.send_message(message.channel, spamm[1])
        return True
    return False

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
    if message.content.startswith('!'):
        await CHECK_COMMAND(message)

client.run('MzUzNjE3MTc2NzkzNzEwNjEy.DIyULg.7J9_CWDYHr2PGeFJWmnPhRLV8BU')
#--------------------------------------------------------------------------------------

# https://discordapp.com/oauth2/authorize?&client_id=%7Bbot-id%7D&scope=%7Bscope%7D&permissions=%7Bpermissions%7D&response_type=code









