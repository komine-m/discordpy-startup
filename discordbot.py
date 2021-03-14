from discord.ext import commands
import os
import traceback
import math

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

bossHP = [[6, 8, 10, 12, 15],[6, 8, 10, 12, 15],[7, 9, 13, 15, 20],[17, 18, 20, 21, 23],[85, 90, 95, 100, 110]]
scorerate = [[12, 12, 13, 14, 15],[16, 16, 18, 19, 20],[20, 20, 24, 24, 26],[35, 35, 37, 38, 40],[35, 35, 37, 38, 40]]

def Calcround(score):
    temp = score
    for i in range(180):
        if(i<3):
            for j in range(5):
                temp -= bossHP[0][j]*scorerate[0][j]*100000
                if(temp<0):
                    roundnow = i+1
                    bossnow = j+1
                    remainingscore = -1 * temp
                    HPnow = int(10*remainingscore/scorerate[0][j])
                    break
            else:
                continue
            break
        elif(i<10):
            for j in range(5):
                temp -= bossHP[1][j]*scorerate[1][j]*100000
                if(temp<0):
                    roundnow = i+1
                    bossnow = j+1
                    remainingscore = -1 * temp
                    HPnow = int(10*remainingscore/scorerate[1][j])
                    break
            else:
                continue
            break
        elif(i<34):
            for j in range(5):
                temp -= bossHP[2][j]*scorerate[2][j]*100000
                if(temp<0):
                    roundnow = i+1
                    bossnow = j+1
                    remainingscore = -1 * temp
                    HPnow = int(10*remainingscore/scorerate[2][j])
                    break
            else:
                continue
            break
        elif(i<44):
            for j in range(5):
                temp -= bossHP[3][j]*scorerate[3][j]*100000
                if(temp<0):
                    roundnow = i+1
                    bossnow = j+1
                    remainingscore = -1 * temp
                    HPnow = int(10*remainingscore/scorerate[3][j])
                    break
            else:
                continue
            break
        else:
            for j in range(5):
                temp -= bossHP[4][j]*scorerate[4][j]*100000
                if(temp<0):
                    roundnow = i+1
                    bossnow = j+1
                    remainingscore = -1 * temp
                    HPnow = int(10*remainingscore/scorerate[4][j])
                    break
            else:
                continue
            break
    text = str(roundnow)+"週目"+str(bossnow)+"ボス 残りHP:"+str(HPnow)
    return text

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 指定した発言に対する応答
    # クラバトスコアから現在地点の計算
    if message.content.startswith('/score'):
        score = message.content.split()
        if score[-1].isdecimal():
            ans = Calcround(int(score[-1]))
            await message.channel.send(ans)

    
    
bot.run(token)
