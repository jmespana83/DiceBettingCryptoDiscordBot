# DiceBettingCryptoDiscordBot
DiceBettingCryptoDiscordBot

This is a discord bot for betting on dice rolls written in Python (front-end) and Java (back-end) with a SQLite database.

Start off first by downloading all the code here, and then proceed with unzipping the file "SqliteConnection.zip"

If you want to use it on your own discord server you will need to have a couple of items in order to config this to run on your discord; please refer to this . . . 

https://realpython.com/how-to-make-a-discord-bot-python/
or
https://medium.com/@moomooptas/how-to-make-a-simple-discord-bot-in-python-40ed991468b4

. . . . for getting setup first with your discord server, in order to encorporate this bot into it.

Next, you will need to undertake these following steps:

Within the "Bot.py" file be sure to update accordingly the fields: fileLocation, TOKEN,
Within the "diceBot-Config.txt" file be sure to update accordingly the fields: database, house_edge, addFaucet,
Within the "DbHandler.java" file be sure to update accordingly the fields: DbLocation,
And within the "addresses-text2.txt" & "addresses-text.txt" file be sure to update accordingly with the crypto deposit addresses for your intended crypto coin to be used, if you plan to use another crypto coin besides Dogecoin then a number of things within all the code would have to be changed, namely the portions dealing with verifying deposits being made on the crypto block chain; this code is hard-written for Dogecoin.

