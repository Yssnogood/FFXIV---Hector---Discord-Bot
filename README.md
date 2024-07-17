# FFXIV Hector Discord-Bot
## Overview
This Discord bot is designed to assist players of Final Fantasy XIV (FFXIV) by providing various functionalities such as retrieving item prices, crafting recipes, and setting language preferences. The bot uses APIs from Universalis and Saddlebag Exchange to fetch market data.

/!\ **It was my first time coding a discord bot. If you use it on multiples servers, you could get some surprise if someone decide to change some settings with the configs commands. I will probably fix this if I find the time for it.** /!\ 

## Features
- Item Pricing: Fetch the current price of items from different servers.
- Crafting Recipes: Display recipes and sub-recipes for crafting items.
- Language Settings: Change the language for item names.
- Server Listings: Set how many items should be displayed in price queries.
## Requirements
- Python 3.7 or higher
- discord.py library
- requests library
## Installation
1. Clone the repository:
        
        git clone https://github.com/Yssnogood/FFXIV---Hector---Discord-Bot.git
        cd FFXIV---Hector---Discord-Bot
2. Install the required Python librairies:

        pip install discord.py requests
3. Add your discord bot token to the `config.py` file:

        class Config:
        TOKEN = 'YOUR_TOKEN_HERE'
        # other configurations...

## Usage
1. Run the bot: 

        python bot.py

2. Invite the bot to your Discord server using the OAuth2 URL from the Discord Developer Portal.

# Commands
## General Commands
- $Hello: Greets the user.
## Item Pricing Commands
- $CostOf: <item_name> [hq] [home_server]: Show the cost of a specific item. hq should be True, False, or left blank. home_server should be one of the configured servers.
## Crafting Recipe Commands
- $RecipeOf: <item_name> [how_many]: Show the recipe for the specified item.
- $RecipesOf: <item_name> [how_many]: Show the recipe and sub-recipes for the specified item.
## Configuration Commands
- $SetLanguage: <language>: Set the language for item names.
- $CurrentLanguage: Display the currently selected language.
- $ChangeListing <how_many>: Change the number of items displayed in price queries.
- $ApiInfo: Display information about the APIs used by the bot.

# Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgements
- Universalis API: [Universalis Documentation](https://docs.universalis.app)
- Saddlebag Exchange API: [Saddlebag Exchange Documentation](https://github.com/ff14-advanced-market-search/saddlebag-with-pockets/wiki#ffxiv-alert-guides)

Feel free to reach out if you have any questions or need further assistance. Happy crafting and adventuring in Eorzea!