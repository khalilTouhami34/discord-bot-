import discord
from discord.ext import commands
import os

# تفعيل البوت باستخدام البرفكس !
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True  # للسماح بإرسال رسائل خاصة
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

# أمر تجربة
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! البوت شغال ✅")

# إرسال رسالة في الخاص
@bot.command()
async def dm(ctx, member: discord.Member, *, message):
    try:
        await member.send(f"📩 **رسالة من {ctx.author}:**\n{message}")
        await ctx.send("✅ تم إرسال الرسالة بنجاح!")
    except:
        await ctx.send("❌ لا يمكن إرسال رسالة لهذا العضو!")

# تشغيل البوت باستخدام التوكن
bot.run(os.getenv("TOKEN"))
