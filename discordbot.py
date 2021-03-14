from discord.ext import commands
import os
import traceback
import math
import datetime
from PIL import ImageGrab
from PIL import Image
import cv2

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

def mtime(hp,dam):
    mt = 90*(1-hp/dam)+20
    if(mt>=90):
        mt = 90
    else:
        mt = math.ceil(mt)
    return mt

direc_path = os.getcwd()
#direc_path = "C:\\Users\\komin\\Documents\\python\\pricone"
file_name1 = "record.dat"
file_name2 = "character_list.dat"
file_path = direc_path +"\\database\\"+ file_name1
chara_list = direc_path +"\\database\\"+ file_name2
#win_img = direc_path + "\\chara_icon\\win.jpg"
#lose_img = direc_path + "\\chara_icon\\lose.jpg"
file_path2 = "SC.png"
#file_path4 = "dc.jpg"
#file_path5 = "oc.jpg"
#file_path2 = direc_path + "\\temp_files\\SC.jpg"
file_path4 = direc_path + "\\temp_files\\dc.jpg"
file_path5 = direc_path + "\\temp_files\\oc.jpg"

def read_record():
    with open(file_path, mode='r') as f:
        s = f.read()
        x = s.split()
        Num_P = int(len(x)/12)
        Plist = [[0]*12 for i in range(Num_P)]
        for i in range(Num_P):
            Plist[i][0] = x[12*i]
            Plist[i][1] = x[12*i+1]
            Plist[i][2] = x[12*i+2]
            Plist[i][3] = x[12*i+3]
            Plist[i][4] = x[12*i+4]
            Plist[i][5] = x[12*i+5]
            Plist[i][6] = x[12*i+6]
            Plist[i][7] = x[12*i+7]
            Plist[i][8] = x[12*i+8]
            Plist[i][9] = x[12*i+9]
            Plist[i][10] = x[12*i+10]
            Plist[i][11] = x[12*i+11]
        return Plist

#def changename(names):
#    for i in range(len(abbr)):
#        if(abbr[i] in names):


def search(DC1, DC2, DC3, DC4, DC5, flug0=5):
    names = [DC1,DC2,DC3,DC4,DC5]
#    names = changename(names)
    flug = check_charactername(names)
    if(flug != "0"):
        if(DC1 == "少なくとも1勝はしてほしいのー"):
            mes = DC1
        else:
            mes = flug + "なんて知りません。\n"
        return mes
    Plist = read_record()
    Num_P = len(Plist)
    match_num = [0 for i in range(Num_P)]
    counter = 0
    mes = "防衛:"+names[0]+"\t"+names[1]+"\t"+names[2]+"\t"+names[3]+"\t"+names[4]+"\n"
    for i in range(Num_P):
        if(Plist[i][0] in names):
            match_num[i] += 1
        if(Plist[i][1] in names):
            match_num[i] += 1
        if(Plist[i][2] in names):
            match_num[i] += 1
        if(Plist[i][3] in names):
            match_num[i] += 1
        if(Plist[i][4] in names):
            match_num[i] += 1
        if(match_num[i] >= flug0):
            if(Plist[i][11] == "0"):
                if(match_num[i] == 5):
                    mes += str(i)+"〇"+"\t"+Plist[i][5]+"\t"+Plist[i][6]+"\t"+Plist[i][7]+"\t"+Plist[i][8]+"\t"+Plist[i][9]+"\t"+Plist[i][10]+"\n"
                    counter += 1
                else:
                    mes += str(i)+"\t"+Plist[i][5]+"\t"+Plist[i][6]+"\t"+Plist[i][7]+"\t"+Plist[i][8]+"\t"+Plist[i][9]+"\t"+Plist[i][10]+"\n"
                    counter += 1
            else:
                if(match_num[i] == 5):
                    mes += str(i)+"〇"+" 注意\t"+Plist[i][5]+"\t"+Plist[i][6]+"\t"+Plist[i][7]+"\t"+Plist[i][8]+"\t"+Plist[i][9]+"\t"+Plist[i][10]+"\n"
                    counter += 1
                else:
                    mes += str(i)+" 注意\t"+Plist[i][5]+"\t"+Plist[i][6]+"\t"+Plist[i][7]+"\t"+Plist[i][8]+"\t"+Plist[i][9]+"\t"+Plist[i][10]+"\n"
                    counter += 1
    if(counter == 0):
        mes += "🙇　こんな編成知らないよー\n"
    return mes

def check_charactername(name): #chara_listは並び順
    with open(chara_list, mode='r') as f:
        s = f.read()
        characternames = s.split()
    for i in range(len(name)):
        if(name[i] not in characternames):
            return name[i]
    return "0"

def read_charalist():
    with open(chara_list, mode='r') as f:
        s = f.read()
        x = s.split()
        Clist = [[0]*3 for i in range(int(len(x)/3))]
        for i in range(int(len(x)/3)):
            Clist[i][0] = x[3*i]
            if(x[3*i+1] != "NoFile"):
                Clist[i][1] = direc_path +"\\chara_icon\\"+ x[3*i+1]
            else:
                Clist[i][1] = x[3*i+1]
            if(x[3*i+2] != "NoFile"):
                Clist[i][2] = direc_path +"\\chara_icon\\"+ x[3*i+2]
            else:
                Clist[i][2] = x[3*i+2]
    return Clist

"""
def Judge_Matching(num):
    if 0.985 < num:
        return True
    else:
        return False

#余白追加関数
def add_margin(pil_img, top, bottom, left, right):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), (0,0,0))
    result.paste(pil_img, (left, top))
    return result

#画像を2160×1080に調整
def check_size(img):
    w,h = img.size
#    if(w==1282 and h==752):
#        img = img.resize((1972,1156))
#    if (w==2160 and h==1080):
#        return img
    if w<2160:
        diff = (2160 - w)//2
        img = add_margin(img, 0, 0, diff, diff)
    elif w>2160:
        diff = (w - 2160)//2
        img = img.crop((diff, 0, w-diff, h))
    w = img.width
    if h<1080:
        diff = (1080 - h)//2
        img = add_margin(img, diff, diff, 0, 0)
    elif h>1080:
        diff = (h - 1080)//2
        img = img.crop((0, diff, w, h-diff))
    return img

def read_BA_SC():
#    file_path2 = direc_path + "\\SC.jpg"
    file_path3 = direc_path + "\\temp_files\\p1.jpg"
#    file_path3 = "p1.jpg"
#    file_path4 = direc_path + "\\p2.jpg"
    sc = Image.open(file_path2)
    sc = check_size(sc)
    box1 = (1450,320,1950,420)
#    box2 = (890,390,1230,470)
    p1_img = sc.crop(box1)
    p1_resize = p1_img.resize((340, 68))
    p1_resize.save(file_path3)
#    p2_img = sc.crop(box2)
#    p2_img.save(file_path4)
    Clist = read_charalist()
    p1img = cv2.imread(file_path3)
#    p2img = cv2.imread(file_path4)
    p1 = ["","","","",""]
    p1_f = [0,0,0,0,0]
    p1_m = [0.0,0.0,0.0,0.0,0.0]
#    p2 = ["","","","",""]
#    p2_f = [0,0,0,0,0]
    for i in range(len(Clist)):
        if(Clist[i][1] != "NoFile"):
            Cimg = cv2.imread(Clist[i][1])
            result1 = cv2.matchTemplate(p1img, Cimg, cv2.TM_CCORR_NORMED)
            minVal1, maxVal1, minLoc1, maxLoc1 = cv2.minMaxLoc(result1)
            Judg1 = Judge_Matching(maxVal1)
            if(Judg1):
                if(maxLoc1[0] < 40):
                    if(p1_m[4]<maxVal1):
                        p1_m[4] = maxVal1
                        p1[4] = Clist[i][0]
                        p1_f[4] = 1
                elif(maxLoc1[0] < 100):
                    if(p1_m[3]<maxVal1):
                        p1_m[3] = maxVal1
                        p1[3] = Clist[i][0]
                        p1_f[3] = 1
                elif(maxLoc1[0] < 160):
                    if(p1_m[2]<maxVal1):
                        p1_m[2] = maxVal1
                        p1[2] = Clist[i][0]
                        p1_f[2] = 1
                elif(maxLoc1[0] < 220):
                    if(p1_m[1]<maxVal1):
                        p1_m[1] = maxVal1
                        p1[1] = Clist[i][0]
                        p1_f[1] = 1
                else:
                    if(p1_m[0]<maxVal1):
                        p1_m[0] = maxVal1
                        p1[0] = Clist[i][0]
                        p1_f[0] = 1
#    for i in range(len(p1_f)):
#        if(p1_f[i] == 0):
#            p1[i] = "リマ"
#            p1_f[i] = 1
    return p1, p1_f

def search_resultPA():
    Clist = read_charalist()
    sc_img = Image.open(file_path2)
    sc_img = check_size(sc_img)
    dc1 = ["","","","",""]
    dc1_f = [0,0,0,0,0]
    dc_m = [0.0,0.0,0.0,0.0,0.0]
    box2 = (1040,300,1720,450)
    dc_img = sc_img.crop(box2)
    dc_resize = dc_img.resize((442, 98))
    dc_resize.save(file_path4)
    dcimg = cv2.imread(file_path4)
#    print("Battle 1")
#    mes1 = "Battle 1\n"
    for i in range(len(Clist)):
        if(Clist[i][2] != "NoFile"):
            Cimg = cv2.imread(Clist[i][2])
            result2 = cv2.matchTemplate(dcimg, Cimg, cv2.TM_CCORR_NORMED)
            minVal2, maxVal2, minLoc2, maxLoc2 = cv2.minMaxLoc(result2)
            Judg2 = Judge_Matching(maxVal2)
            if(Judg2):
                if(maxLoc2[0] < 50):
                    if(dc_m[4]<maxVal2):
                        dc_m[4] = maxVal2
                        dc1[4] = Clist[i][0]
                        dc1_f[4] = 1
                elif(maxLoc2[0] < 150):
                    if(dc_m[3]<maxVal2):
                        dc_m[3] = maxVal2
                        dc1[3] = Clist[i][0]
                        dc1_f[3] = 1
                elif(maxLoc2[0] < 250):
                    if(dc_m[2]<maxVal2):
                        dc_m[2] = maxVal2
                        dc1[2] = Clist[i][0]
                        dc1_f[2] = 1
                elif(maxLoc2[0] < 350):
                    if(dc_m[1]<maxVal2):
                        dc_m[1] = maxVal2
                        dc1[1] = Clist[i][0]
                        dc1_f[1] = 1
                else:
                    if(dc_m[0]<maxVal2):
                        dc_m[0] = maxVal2
                        dc1[0] = Clist[i][0]
                        dc1_f[0] = 1
#    print(dc1)
#    for i in range(len(dc_f)):
#        if(dc_f[i] == 0):
#            print("dc",i+1,"?")
#            dc1[i] = input()
#    mes1 = mes1 + dc1[0] + "\t" + dc1[1] + "\t" + dc1[2] + "\t" + dc1[3] + "\t" + dc1[4] + "\n"
#2編成目
    dc2 = ["","","","",""]
    dc2_f = [0,0,0,0,0]
    dc_m = [0.0,0.0,0.0,0.0,0.0]
    box2 = (1040,500,1720,650)
    dc_img = sc_img.crop(box2)
    dc_resize = dc_img.resize((442, 98))
    dc_resize.save(file_path4)
    dcimg = cv2.imread(file_path4)
#    print("Battle 2")
#    mes2 = "Battle 2\n"
    for i in range(len(Clist)):
        if(Clist[i][2] != "NoFile"):
            Cimg = cv2.imread(Clist[i][2])
            result2 = cv2.matchTemplate(dcimg, Cimg, cv2.TM_CCORR_NORMED)
            minVal2, maxVal2, minLoc2, maxLoc2 = cv2.minMaxLoc(result2)
            Judg2 = Judge_Matching(maxVal2)
            if(Judg2):
                if(maxLoc2[0] < 50):
                    if(dc_m[4]<maxVal2):
                        dc_m[4] = maxVal2
                        dc2[4] = Clist[i][0]
                        dc2_f[4] = 1
                elif(maxLoc2[0] < 150):
                    if(dc_m[3]<maxVal2):
                        dc_m[3] = maxVal2
                        dc2[3] = Clist[i][0]
                        dc2_f[3] = 1
                elif(maxLoc2[0] < 250):
                    if(dc_m[2]<maxVal2):
                        dc_m[2] = maxVal2
                        dc2[2] = Clist[i][0]
                        dc2_f[2] = 1
                elif(maxLoc2[0] < 350):
                    if(dc_m[1]<maxVal2):
                        dc_m[1] = maxVal2
                        dc2[1] = Clist[i][0]
                        dc2_f[1] = 1
                else:
                    if(dc_m[0]<maxVal2):
                        dc_m[0] = maxVal2
                        dc2[0] = Clist[i][0]
                        dc2_f[0] = 1
#    print(dc2)
#    for i in range(len(dc_f)):
#        if(dc_f[i] == 0):
#            print("dc",i+1,"?")
#            dc2[i] = input()
#    mes2 = mes2 + dc2[0] + "\t" + dc2[1] + "\t" + dc2[2] + "\t" + dc2[3] + "\t" + dc2[4] + "\n"
#3編成目
    dc3 = ["","","","",""]
    dc3_f = [0,0,0,0,0]
    dc_m = [0.0,0.0,0.0,0.0,0.0]
    box2 = (1040,740,1720,900)
    dc_img = sc_img.crop(box2)
    dc_resize = dc_img.resize((442, 98))
    dc_resize.save(file_path4)
    dcimg = cv2.imread(file_path4)
#    print("Battle 2")
#    mes3 = "Battle 3\n"
    for i in range(len(Clist)):
        if(Clist[i][2] != "NoFile"):
            Cimg = cv2.imread(Clist[i][2])
            result2 = cv2.matchTemplate(dcimg, Cimg, cv2.TM_CCORR_NORMED)
            minVal2, maxVal2, minLoc2, maxLoc2 = cv2.minMaxLoc(result2)
            Judg2 = Judge_Matching(maxVal2)
            if(Judg2):
                if(maxLoc2[0] < 50):
                    if(dc_m[4]<maxVal2):
                        dc_m[4] = maxVal2
                        dc3[4] = Clist[i][0]
                        dc3_f[4] = 1
                elif(maxLoc2[0] < 150):
                    if(dc_m[3]<maxVal2):
                        dc_m[3] = maxVal2
                        dc3[3] = Clist[i][0]
                        dc3_f[3] = 1
                elif(maxLoc2[0] < 250):
                    if(dc_m[2]<maxVal2):
                        dc_m[2] = maxVal2
                        dc3[2] = Clist[i][0]
                        dc3_f[2] = 1
                elif(maxLoc2[0] < 350):
                    if(dc_m[1]<maxVal2):
                        dc_m[1] = maxVal2
                        dc3[1] = Clist[i][0]
                        dc3_f[1] = 1
                else:
                    if(dc_m[0]<maxVal2):
                        dc_m[0] = maxVal2
                        dc3[0] = Clist[i][0]
                        dc3_f[0] = 1
#    print(dc3)
#    for i in range(len(dc_f)):
#        if(dc_f[i] == 0):
#            print("dc",i+1,"?")
#            dc3[i] = input()
#    mes3 = mes3 + dc3[0] + "\t" + dc3[1] + "\t" + dc3[2] + "\t" + dc3[3] + "\t" + dc3[4] + "\n"
#search
#    print("result of Battle 1")
#    mes1 = "Battle 1\n" + search(dc1[0],dc1[1],dc1[2],dc1[3],dc1[4])
#    print("result of Battle 2")
#    mes2 = "Battle 2\n" + search(dc2[0],dc2[1],dc2[2],dc2[3],dc2[4])
#    print("result of Battle 3")
#    mes3 = "Battle 3\n" + search(dc3[0],dc3[1],dc3[2],dc3[3],dc3[4])
#    mes = mes1 + mes2 + mes3
#    for i in range(len(dc1_f)):
#        if(dc1_f[i] == 0):
#            dc1[i] = "リマ"
#            dc1_f[i] = 1
#    for i in range(len(dc2_f)):
#        if(dc2_f[i] == 0):
#            dc2[i] = "リマ"
#            dc2_f[i] = 1
#    for i in range(len(dc3_f)):
#        if(dc3_f[i] == 0):
#            dc3[i] = "リマ"
#            dc3_f[i] = 1
    if(dc3_f[0]==0):
        if(dc3_f[1]==0):
            if(dc3_f[2]==0):
                if(dc3_f[3]==0):
                    if(dc3_f[4]==0):
                        dc3 = ["少なくとも1勝はしてほしいのー","リマ","リマ","リマ","リマ"]
                        dc3_f = [1,1,1,1,1]
    return dc1, dc1_f, dc2, dc2_f, dc3, dc3_f

def record(DC1, DC2, DC3, DC4, DC5, OC1, OC2, OC3, OC4, OC5):
    names = [DC1,DC2,DC3,DC4,DC5,OC1,OC2,OC3,OC4,OC5]
    if(None in names):
        mes = "cancelを押さないでください。\n"
        return mes
    flug = check_charactername(names)
    if(flug != "0"):
        mes = flug + "なんて知らないよー\n"
        return mes
    d_today = datetime.date.today()
    day = str(d_today.year)+"-"+str(d_today.month)+"-"+str(d_today.day)
    new_data = "\n"+DC1+"\t"+DC2+"\t"+DC3+"\t"+DC4+"\t"+DC5+"\t"+OC1+"\t"+OC2+"\t"+OC3+"\t"+OC4+"\t"+OC5+"\t"+day+"\t0"
    mes = "防衛:"+names[0]+"\t"+names[1]+"\t"+names[2]+"\t"+names[3]+"\t"+names[4]+"\n攻撃:"+names[5]+"\t"+names[6]+"\t"+names[7]+"\t"+names[8]+"\t"+names[9]+"\n"
#    with open(file_path, mode='a') as f:
#        f.write(new_data)
    mes += "新しい編成を記録したよ\n"
    return mes

"""
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
    if message.content.startswith('/tcal'):
        mes = message.content.split()
        mt = mtime(int(mes[1]),int(mes[2]))
        await message.channel.send(str(mt)+'秒')
    # アリーナ自作データベースの検索
    if message.content.startswith('/ar'):
        party = message.content.split()
        if len(party)==6:
            result = search(party[1],party[2],party[3],party[4],party[5])
            await message.channel.send(result)
"""    # 画像利用検索
    if message.content.startswith('/search'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.url.endswith(("png","jpg","jpeg")):
                    await message.channel.send("画像を保存するよ")
                    await attachment.save("SC.png")
                    DCs, DCs_f = read_BA_SC()
                    for i in range(len(DCs_f)):
                        if(DCs_f[i] == 0):
                            await message.channel.send(str(i+1)+"番目の防衛キャラはだれー?")
                            msg = await client.wait_for('message')
                            DCs[i] = msg.content
                    mes = search(DCs[0],DCs[1],DCs[2],DCs[3],DCs[4])
                    await message.channel.send(mes)
    if message.content.startswith('/pa'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.url.endswith(("png","jpg","jpeg")):
                    await message.channel.send("画像を保存するよ")
                    await attachment.save("SC.png")
                    DCs1, DCs1_f, DCs2, DCs2_f, DCs3, DCs3_f = search_resultPA()
                    for i in range(len(DCs1_f)):
                        if(DCs1_f[i] == 0):
                            await message.channel.send("パーティ1の"+str(i+1)+"番目の防衛キャラはだれー?")
                            msg = await client.wait_for('message')
                            DCs1[i] = msg.content
                    for i in range(len(DCs2_f)):
                        if(DCs2_f[i] == 0):
                            await message.channel.send("パーティ2の"+str(i+1)+"番目の防衛キャラはだれー?")
                            msg = await client.wait_for('message')
                            DCs2[i] = msg.content
                    for i in range(len(DCs3_f)):
                        if(DCs3_f[i] == 0):
                            await message.channel.send("パーティ3の"+str(i+1)+"番目の防衛キャラはだれー?")
                            msg = await client.wait_for('message')
                            DCs3[i] = msg.content
                    await message.channel.send("Battle 1")
                    mes = search(DCs1[0],DCs1[1],DCs1[2],DCs1[3],DCs1[4])
                    await message.channel.send(mes)
                    await message.channel.send("Battle 2")
                    mes = search(DCs2[0],DCs2[1],DCs2[2],DCs2[3],DCs2[4])
                    await message.channel.send(mes)
                    await message.channel.send("Battle 3")
                    mes = search(DCs3[0],DCs3[1],DCs3[2],DCs3[3],DCs3[4])
                    await message.channel.send(mes)
    if message.content.startswith('/rec'):
        party = message.content.split()
        if len(party)==11:
            result = record(party[1],party[2],party[3],party[4],party[5],party[6],party[7],party[8],party[9],party[10])
            await message.channel.send(result)
"""

bot.run(token)
