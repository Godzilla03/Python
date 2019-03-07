from django.http import HttpResponse
from PIL import Image,ImageDraw,ImageFont
import random

def rmdRGB():
    c1 =random.randrange(0,255)
    c2 =random.randrange(10,255)
    c3 =random.randrange(60,255)
    return (c1,c2,c3)

def verifycode(request):
    #背景色，长度，宽度
    # bgcolor = '#997679'
    bgcolor = '#997679'
    width = 500
    height = 125
    #创建画布
    im = Image.new('RGB',(width,height),bgcolor)
    #创建画笔
    draw = ImageDraw.Draw(im)
    #画点
    for i in range(0,1000):
        xy=(random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill)
    # #添加文字
    # str1 = 'ABCD123DEFGHIJK456LMNOPQRST789UVWXYZ0'
    # rand_str = ''
    # for i in range(0,4):
    #     rand_str += str1[random.randrange(0,len(str1))]
    font = ImageFont.truetype('/usr/share/fonts/truetype/fonts-japanese-gothic',100)
    # draw.text((5,2),rand_str,fill=rmdRGB(),font=font)
    numb_1 = {"1":"壹","2":"贰","3":"叁","4":"肆","5":"伍","6":"陆","7":"柒","8":"捌","9":"玖"}
    numb_2 = random.randrange(1,50)
    sign = ["+","-"]
    numb_1_n = random.randrange(1,10)
    numb_1_s = str(numb_1_n)
    first_s = numb_1[numb_1_s]
    third_s = str(numb_2)
    sign_n = random.randrange(0,2)
    second_s = sign[sign_n]
    if sign_n == 0:
        last = numb_1_n + numb_2
    else:
        last = numb_2 - numb_1_n
    last_s = str(last)
    draw.text((25,2),'?',font=font,fill=rmdRGB())
    draw.text((100,2),second_s,font=font,fill=rmdRGB())
    draw.text((175,2),first_s,font=font,fill=rmdRGB())
    draw.text((300,2),'=',font=font,fill=rmdRGB())
    draw.text((375,2),last_s,font=font,fill=rmdRGB())


    #划线
    for i in range(0,50):
        x1 = random.randrange(0,width)
        y1 = random.randrange(0,height)
        x2 = random.randrange(0,width)
        y2 = random.randrange(0,height)
        draw.line((x1,y1,x2,y2),fill=rmdRGB())
    #添加圆
    for i in range(100):
        # s = random.randrange(60, 360)
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        draw.arc((x,y,x+random.randrange(0,100),y+random.randrange(0,100)),0,random.randrange(0, 360),fill=rmdRGB())

    #结束
    del draw
    import io
    buf = io.BytesIO()
    im.save(buf,'png') #存什么格式
    return HttpResponse(buf.getvalue(),'image/png') #告诉前段什么格式