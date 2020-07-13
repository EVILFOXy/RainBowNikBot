import discord
from discord.ext import commands, tasks
from itertools import cycle
import os

TOKEN = os.environ.get('TOKEN2')
prefix = '`'
client = commands.Bot(command_prefix=prefix)
colours = cycle([0xFF0000, 0xFF7F00, 0xFFFF00, 0x00FF00, 0x0000FF, 0x8F00FF])


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    _rain.start()


@tasks.loop(seconds=1)
async def _rain():

    server = client.get_guild(690936791083122748)
    channel = client.get_channel(732173473102692412)
    role = discord.utils.get(server.roles, name='rainbow')
    await role.edit(server=server, role=role, colour=discord.Colour(next(colours)))


client.run(str(TOKEN))