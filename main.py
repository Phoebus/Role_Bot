import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    for guild in client.guilds:  #cycling through all guilds
        for channel in guild.text_channels: #cycling through all channels until we find the roles channel.
            if str(channel).strip() == "roles": 
                global roles_channel_id
                roles_channel_id = channel.id #storing the channel id
                roles_channel = client.get_channel(roles_channel_id)
                await roles_channel.send("""
Hello @everyone!
React in this message in order to take the role you need:
1)👍 Member
2)👨‍💻 Programmer
""")
                break
