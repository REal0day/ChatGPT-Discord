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
### THIS NEXT PART CAN BE KINDY TRICKY. IF YOU HAVE ISSUES, SCROLL DOWN TO PART II OF THIS.
#### Part I
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and sign in with your Discord account.
2. Click on the "New Application" button and provide a name for your bot.
3. Navigate to the "Bot" tab and click on "Add Bot". Confirm the action when prompted.
4. Under the "Token" section, click on "Copy" to copy your bot's token. Keep this token safe and do not share it publicly.
5. Go to the "OAuth2" tab, scroll down to the "Scopes" section, and select the "bot" scope.
6. In the "Bot Permissions" section, select "Send Messages" and "Read Message History".
7. Copy the generated URL from the "Scopes" section and paste it into your browser to invite the bot to your server.

#### Part II
If you had difficulties with step 5, this is what I did.
1. Get the client-id by going to OAuth2 Settings. It will be in the field: Client information
2. Select the Application > Bot and scroll down to Bot Permissions.
3. Here select all the permissions you want to add. I'm adding everything that let the bot interact with us, but won't let it control the server. Everything with "Send" and "Create", I will let it do. And "Read Message History". I even let it change it's own nickname if it wants to. 
4. Now go to the bottom and you'll see a number. That number represents the permissions the bot has. In my case, it's 3270722313792.
5. You must be logged into Discord in your browser for this next step. Given the URL: `https://discord.com/api/oauth2/authorize?client_id=<INSERT-CLIENT-ID>&permissions=<INSERT-PERMISSION-NUMBER>&scope=bot`
replace the client-id with your bots client-id, and the permissions with the permission number.
Then go to the link, and approve the bot into your server.
`https://discord.com/api/oauth2/authorize?client_id=<INSERT-CLIENT-ID>&permissions=<INSERT-PERMISSION-NUMBER>&scope=bot`
6. You bot should be on your server now. 
 
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

`python3 chat3_v2.py`

3. The bot should now be online in your Discord server. To interact with ChatGPT, type `!chat <your_message>` in a text channel.

**Note**: The bot will only respond to messages starting with `!chat`. To change the command prefix, edit the `bot.py` file and replace `!chat` with your desired prefix.
