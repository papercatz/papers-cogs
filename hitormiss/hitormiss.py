from redbot.core import commands

class hitormiss(commands.hitormiss):
    """hitormiss"""

    @commands.command()
    async def mycom(self, ctx):
        """Provides a link to NyanNyanCosplay doing the memiest things."""
        await ctx.send("https://www.youtube.com/watch?v=gVEdQJ7qtJw")
