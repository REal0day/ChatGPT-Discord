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
async def chat_with_gpt(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        #engine="davinci-codex",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=["User:", "\n"],
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Command to chat with the bot
@bot.command()
async def chat(ctx, *, message):
    prompt = f"User: {message}\nAssistant:"
    response = await chat_with_gpt(prompt)
    print(f"{response}")
    await ctx.send(response)

# Run the bot
bot.run(environ["DISCORD_API_KEY"])
