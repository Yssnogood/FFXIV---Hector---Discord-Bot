import json
from datetime import datetime

class Config:

    TOKEN = 'YOUR_TOKEN_HERE'

    SERVERLIST =  ["Europe","Chaos","Light",
                    "Cerberus", "Louisoix", "Moogle", "Omega", "Ragnarok", "Spriggan", "Sagittarius","Phantom",
                    "Lich", "Odin", "Phoenix", "Shiva", "Twintania", "Zordiark", "Alpha", "Raiden"]

    LANGAVAILABLE = ["en", "fr", "de", "ja"]
    LANG = "en"

    LISTING = "5"

    @staticmethod
    def set_listing(new_listing):
        Config.LISTING = str(new_listing)

    @staticmethod
    def get_listing():
        return Config.LISTING

    @staticmethod
    def get_lang():
        return Config.LANG

    @staticmethod
    def set_lang(new_lang):
        if new_lang in Config.LANGAVAILABLE:
            Config.LANG = new_lang


with open('Data/items.json', encoding='utf-8')as f:
    DATAID= json.load(f)
with open('Data/recipes.json', encoding='utf-8')as f:
    DATARECIPES= json.load(f)