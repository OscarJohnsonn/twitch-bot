from twitchio.ext import commands

f = open("chat.txt", "w")

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='YOUR TWITCH TOKEN', prefix='?', initial_channels=['NAME OF CHANNEL THAT THE BOT WILL JOIN'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return

        print(message.content)
        f = open("chat.txt", "w")
        f.write(message.content)
        
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):

        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()