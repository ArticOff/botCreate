"""
The MIT License (MIT)

Copyright (c) 2022-today Artic#6377

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import os

BOT = 'bot'
CLIENT = 'client'
SHARDED_BOT = 'sharded_bot'

def create(name: str, token: str, prefix: str = '!', type: str = BOT, launch: bool = False):
    """
    ## Create a bot
    
    ## Exemple:
    ```python
    import botCreate

    bot_type = botCreate.BOT

    botCreate.create(
        name='mybot',
        token='12346789MySuperSecretToken',
        prefix='?',
        type=bot_type,
        launch=True
    )
    ```
    ### The launch function is to launch the bot
    """
    if not name:
        name = 'bot'
    name = name.replace(' ', '_').replace("'", '_')
    if os.path.isfile('{}.py'.format(name)):
        import random
        code = random.randint(1, 10000)
        name = '{}_{}'.format(name, code)
    with open('{}.py'.format(name), 'x') as file:
        if type == 'bot':
            file.write("import discord\nfrom discord.ext import commands\n\nTOKEN = '" + token + "'\n\nintents = discord.Intents().all()\nintents.members = True\n\nbot = commands.Bot(command_prefix='" + prefix + "', description='my description', intents=intents)\n\n@bot.event\nasync def on_ready():\n    print('ready!')\n    await bot.change_presence(activity=discord.Game(name='made with botCreate.py'))\n\n@bot.command()\nasync def ping(ctx):\n    await ctx.send('pong! `{}ms`'.format(round(bot.latency * 1000), 2))\n\nbot.run('{}'.format(TOKEN))")
        elif type == 'sharded_bot':
            file.write("import discord\nfrom discord.ext import commands\n\nTOKEN = '" + token + "'\n\nintents = discord.Intents().all()\nintents.members = True\n\nbot = commands.AutoShardedBot(command_prefix='" + prefix + "', description='my description', intents=intents)\n\n@bot.event\nasync def on_ready():\n    print('ready!')\n    await bot.change_presence(activity=discord.Game(name='made with botCreate.py'))\n\n@bot.command()\nasync def ping(ctx):\n    await ctx.send('pong! `{}ms`'.format(round(bot.latency * 1000), 2))\n\nbot.run('{}'.format(TOKEN))")
        elif type == 'client':
            file.write("import discord\n\nTOKEN = '" + token + "'\n\nclient = discord.Client()\n\n@client.event\nasync def on_ready():\n    print('ready!')\n    await client.change_presence(activity=discord.Game(name='made with botCreate.py'))\n\n@client.event\nasync def on_message(message):\n    if message.author == client.user:\n        return\n\n    if message.content.startswith('" + prefix + "ping'):\n        await message.channel.send('pong! `{}ms`'.format(round(client.latency * 1000), 2))\n\nclient.run('{}'.format(TOKEN))")
        else:
            file.write("import discord\nfrom discord.ext import commands\n\nTOKEN = '" + token + "'\n\nintents = discord.Intents().all()\nintents.members = True\n\nbot = commands.Bot(command_prefix='" + prefix + "', description='my description', intents=intents)\n\n@bot.event\nasync def on_ready():\n    print('ready!')\n    await bot.change_presence(activity=discord.Game(name='made with botCreate.py'\n\n@bot.command()\nasync def ping(ctx):\n    await ctx.send('pong! `{}ms`'.format(round(bot.latency * 1000), 2))\n\nbot.run('{}'.format(TOKEN))")
            print('TypeValueError [botCreate]: type must be \'CLIENT\' or \'BOT\' or \'SHARDED_BOT\', not {}.'.format(type))
        file.close()
        if launch:
            os.system('python {}.py'.format(name))