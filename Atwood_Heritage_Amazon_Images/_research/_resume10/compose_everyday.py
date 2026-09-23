#!/usr/bin/env python3
# Compose image #10 "Take It Anywhere" — titled 2x2 everyday-carry montage.
from PIL import Image, ImageDraw, ImageFont, ImageOps
import sys, os
B="/Users/wetrade/Documents/Brand Image Generation/Atwood_Heritage_Amazon_Images"
REF=f"{B}/_references"
S=2048
CREAM=(245,239,227); INK=(46,36,28); RED=(150,38,32); RED2=(120,30,25); GOLD=(201,162,75); WHITE=(255,255,255)
BASK="/System/Library/Fonts/Supplemental/Baskerville.ttc"; AVENIR="/System/Library/Fonts/Avenir Next.ttc"
def ai(w):
    for i in range(20):
        try:
            if ImageFont.truetype(AVENIR,40,index=i).getname()[1].replace(" ","").lower()==w: return i
        except: break
    return 0
AVB=ai("bold");AVD=ai("demibold") or AVB;AVR=ai("regular");AVM=ai("medium") or AVR
def serif(sz,b=True,it=False): return ImageFont.truetype(BASK,sz,index=(3 if b and it else 1 if b else 2 if it else 0))
def sans(sz,w="demi"): return ImageFont.truetype(AVENIR,sz,index={"bold":AVB,"demi":AVD,"med":AVM,"reg":AVR}[w])
def ct(d,cx,y,t,f,fill=INK,anchor="ma",sp=8): d.text((cx,y),t,font=f,fill=fill,anchor=anchor,align="center",spacing=sp)
def maple(d,cx,cy,s,fill=RED): d.polygon([(cx,cy-s),(cx+s*.3,cy-s*.2),(cx+s,cy-s*.15),(cx+s*.4,cy+s*.2),(cx+s*.6,cy+s),(cx,cy+s*.5),(cx-s*.6,cy+s),(cx-s*.4,cy+s*.2),(cx-s,cy-s*.15),(cx-s*.3,cy-s*.2)],fill=fill)
def divider(d,cx,y,w=440): d.line([(cx-w//2,y),(cx-36,y)],fill=GOLD,width=4);d.line([(cx+36,y),(cx+w//2,y)],fill=GOLD,width=4);maple(d,cx,y,18)
def wordmark(d,cx,y):
    ct(d,cx,y,"ATWOOD HERITAGE",sans(40,"bold"),INK);d.text((cx,y+48),"S I N C E   1 9 6 2",font=sans(20,"med"),fill=RED,anchor="ma")

TOP=250; BOT=1830          # grid vertical bounds
GAP=10
def cell_scrim(cell):
    w,h=cell.size; grad=Image.new("L",(1,h),0)
    for y in range(h): grad.putpixel((0,y),0 if y<h*0.60 else int(200*((y-h*0.60)/(h*0.40))))
    sc=Image.new("RGBA",(w,h),(20,12,8,0)); sc.putalpha(grad.resize((w,h)))
    return Image.alpha_composite(cell.convert("RGBA"),sc).convert("RGB")
LABELS=[("trail","ON THE TRAIL"),("school","AT SCHOOL"),("work","AT WORK"),("everyday","EVERYDAY")]
def render(asin,folder):
    ed=f"{REF}/{asin}/everyday"
    cw=(S-GAP)//2; ch=(BOT-TOP-GAP)//2
    im=Image.new("RGB",(S,S),CREAM); d=ImageDraw.Draw(im)
    for i,(key,lab) in enumerate(LABELS):
        cell=ImageOps.fit(Image.open(f"{ed}/{key}.png").convert("RGB"),(cw,ch),Image.LANCZOS)
        cell=cell_scrim(cell); cd=ImageDraw.Draw(cell)
        f=sans(37,"bold"); tw=cd.textlength(lab,font=f)
        cd.rounded_rectangle([28,ch-84,28+tw+56,ch-24],radius=30,fill=RED)
        cd.text((28+28,ch-84+13),lab,font=f,fill=WHITE)
        r,c=divmod(i,2); x=c*(cw+GAP); y=TOP+r*(ch+GAP); im.paste(cell,(x,y))
    # top title band
    ct(d,S//2,54,"Fuel Every Part of Your Day",serif(88,True),INK)
    ct(d,S//2,176,"Grab-and-go protein for the trail, the classroom, the desk — and everywhere in between.",sans(33,"med"),RED2)
    # bottom wordmark band
    divider(d,S//2,1888)
    wordmark(d,S//2,1930)
    out=f"{B}/{folder}/10_everyday_carry.png"; im.save(out); print("composed",out)
if __name__=="__main__":
    render(sys.argv[1], sys.argv[2])
