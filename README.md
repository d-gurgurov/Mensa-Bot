# Mensa Bot

## Overview

This project is a Python script that utilizes web scraping and the Telegram Bot API to provide translated cafeteria menus. It uses BeautifulSoup for web scraping, the googletrans library for translation, and telegram.ext for creating a Telegram bot.

## Project Structure

    ├── LICENSE
    ├── README.md
    ├── code
    │   └── TelBot.py
    └── requirements.txt

## Configuration

To use this script, you need to obtain a Telegram API key and replace the placeholder in the code:

`API_KEY = "YOUR_TELEGRAM_API_KEY"`

## Usage 

To run the script, execute the following command:

`python script_name.py`


## Acknowledgements

- Thanks to [Mensa](https://mensaar.de/) Saarland University for providing the cafeteria menu.
- This project uses the [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) library for web scraping.
- The translation service is powered by [googletrans](https://pypi.org/project/googletrans/) library.
- Special thanks to [python-telegram-bot](https://python-telegram-bot.org/) for simplifying the Telegram bot creation process.


## Dependencies
- Python 3.x
- Required Python packages (install using pip install -r requirements.txt)