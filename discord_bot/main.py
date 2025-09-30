import discord
import tokens
import stock

class MYBot(discord.Client):
    async def on_ready(self):
        print("Logged in as {0}".format(self.user))

    async def on_message(self, message):
        #Ignore messages from bot
        if message.author == self.user:
            return

        if message.content.startswith('$value'):
            stockName = message.content.replace('$value', '').strip()
            currentVal = stock.getCurrentStockValue(stockName)
            await message.channel.send((f'The current share price of {stockName} is ${currentVal}'))


intents = discord.Intents.default()
intents.message_content = True
bot = MYBot(intents=intents)

#stock.getCurrentStockValue("AAPL")
bot.run(tokens.botToken)