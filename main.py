import discord
import os

intents = discord.Intents.default()
intents.members = True

roles_msg_id = []

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    for guild in client.guilds:  #cycling through all guilds
        for channel in guild.text_channels: #cycling through all channels until we find the roles channel.
            if str(channel).strip() == "roles": 
                global roles_msg_id
                roles_channel_id = channel.id #storing the channel id
                roles_channel = client.get_channel(roles_channel_id)
                await roles_channel.send("""
Hello @everyone!
React in this message in order to take the role you need:
1)👍 Member
2)👨‍💻 Programmer
""")
                roles_msg_id.append(channel.last_message_id)
                break

@client.event
async def on_raw_reaction_add(payload):
    found = False
    for i in roles_msg_id:
        if payload.message_id == i:
            found = True
            break

    if not found:
        return

    guild = client.get_guild(payload.guild_id)

    if guild != None:
        if payload.emoji.name == '👍':
            role = discord.utils.get(guild.roles, name="Member")
            await payload.member.add_roles(role)
        if payload.emoji.name == '👨‍💻':
            role = discord.utils.get(guild.roles, name="Programmer")
            await payload.member.add_roles(role)
            

@client.event
async def on_raw_reaction_remove(payload):
    found = False
    for i in roles_msg_id:
        if payload.message_id == i:
            found = True
            break

    if not found:
        return

    guild = client.get_guild(payload.guild_id)
    
    if guild != None:
        if payload.emoji.name == '👍':
            member = guild.get_member(payload.user_id)
            role = discord.utils.get(guild.roles, name="Member")
            await member.remove_roles(role)
        if payload.emoji.name == '👨‍💻':
            member = guild.get_member(payload.user_id)
            role = discord.utils.get(guild.roles, name="Programmer")
            await member.remove_roles(role)

client.run()
