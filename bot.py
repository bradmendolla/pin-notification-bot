import discord
import time
from discord.ext import commands
from discord.utils import get
from config import token




bot = commands.Bot(command_prefix="?", case_insensitive = True)

# Verifies bot is running
@bot.event
async def on_ready():
    print(f"{bot.user.name} is slowly realizing it's alive! And ready!")

@bot.event
async def on_member_join(ctx):
    user = ctx.user
    role = get(ctx.guild.roles, name="Test Subjects")
    await user.create_dm
    await user.dm_channel.send(f"Welcome to the Bot Factory valued Test Subject. Whether you arrived here voluntarily or otherwise, just know that you won't be paid for your time.")
    await user.add_roles(role)



bot.run(token)