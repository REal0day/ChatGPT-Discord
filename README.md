# ChatGPT-Discord
# Discord ChatGPT Integration 🤖💬

This repository contains a simple Python script that integrates OpenAI's ChatGPT into a Discord bot, allowing users to interact with ChatGPT directly through a Discord server. Follow the step-by-step instructions below to set up and deploy the bot on your own server.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setting up Discord Bot](#setting-up-discord-bot)
- [Installation and Configuration](#installation-and-configuration)
- [Running the Bot](#running-the-bot)

## Prerequisites 📚

- A Discord account
- [Python 3.6 or higher](https://www.python.org/downloads/)
- [openai](https://github.com/openai/openai) Python package
- [discord.py](https://github.com/Rapptz/discord.py) Python package
 - dotenv

## Setting up Discord Bot 🤖

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and sign in with your Discord account.
2. Click on the "New Application" button and provide a name for your bot.
3. Navigate to the "Bot" tab and click on "Add Bot". Confirm the action when prompted.
4. Under the "Token" section, click on "Copy" to copy your bot's token. Keep this token safe and do not share it publicly.
5. Go to the "OAuth2" tab, scroll down to the "Scopes" section, and select the "bot" scope.
6. In the "Bot Permissions" section, select "Send Messages" and "Read Message History".
7. Copy the generated URL from the "Scopes" section and paste it into your browser to invite the bot to your server.

## Installation and Configuration ⚙️

1. Clone the repository or download the source code.
2. Install the required Python packages by running the following command:
`pip3 install openai discord.py dotenv`

3. Create a file named `.env` in the root directory of the project.
4. Open the `.env` file and add the following content, replacing `<YOUR_DISCORD_BOT_TOKEN>` with your bot's token and `<YOUR_OPENAI_API_KEY>` with your OpenAI API key:

`DISCORD_TOKEN=<YOUR_DISCORD_BOT_TOKEN> 
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>`

5. Save and close the `.env` file.

## Running the Bot 🚀

1. Open a terminal or command prompt and navigate to the root directory of the project.
2. Run the following command to start the bot:

python3 chat3_v2.py

3. The bot should now be online in your Discord server. To interact with ChatGPT, type `!chat <your_message>` in a text channel.

**Note**: The bot will only respond to messages starting with `!chat`. To change the command prefix, edit the `bot.py` file and replace `!chat` with your desired prefix.
