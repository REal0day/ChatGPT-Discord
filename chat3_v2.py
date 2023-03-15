#!/usr/bin/env python3
from os import environ
import discord, openai
from dotenv import load_dotenv
from discord.ext import commands

# Set up the Discord bot
intents = discord.Intents.all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

# Load the variables
load_dotenv('./.env')

# Set up OpenAI API
openai.api_key = environ["OPENAI_API_KEY"]

# Chat function to interact with OpenAI API
async def chat_with_gpt(message):
    response = openai.ChatCompletion.create(
        #model="gpt-4-0314",
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
        max_tokens=150,
        n=1,
        temperature=0.5,
    )
    assistant_message = response.choices[0]['message']
    
    if assistant_message is not None:
        return assistant_message["content"].strip()
    else:
        return "I'm sorry, I couldn't generate a response."
    

# Command to chat with the bot
@bot.command()
async def chat(ctx, *, message=None):
    # Handle file uploads
    if ctx.message.attachments:
        attachment_urls = []
        for attachment in ctx.message.attachments:
            attachment_urls.append(attachment.url)
        message = f"{message or ''} {' '.join(attachment_urls)}"
    
    response = await chat_with_gpt(message)
    await ctx.send(response)

# Run the bot
bot.run(environ["DISCORD_API_KEY"])