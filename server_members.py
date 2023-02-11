import discord
import asyncio
from tkinter import *

client = discord.Client()
root = Tk()
root.title("Discord User List")
root.geometry("400x400")

user_list = []

async def list_users():
    await client.wait_until_ready()
    server = client.get_guild(INSERT_GUILD_ID_HERE)
    for member in server.members:
        user_list.append(member.name)
    return user_list

def show_users():
    users = list_users()
    user_label = Label(root, text="Users:")
    user_label.pack()
    for user in users:
        user_display = Label(root, text=user)
        user_display.pack()

client.loop.create_task(list_users())

show_button = Button(root, text="Show Users", command=show_users)
show_button.pack()

root.mainloop()
