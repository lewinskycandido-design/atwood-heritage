#!/usr/bin/env python3
# Generate the 4 "everyday carry" context scenes (trail/school/work/everyday)
# for image #10, conditioned on the real product cut-out for texture fidelity.
import subprocess, threading, os, re, glob, sys
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageOps
CODEX="/Users/wetrade/.codex/plugins/.plugin-appserver/codex"
B="/Users/wetrade/Documents/Brand Image Generation/Atwood_Heritage_Amazon_Images/_references"
PEP="/Users/wetrade/Documents/Brand Image Generation/Atwood_Heritage_Amazon_Images/_research/_resume10/pep_sticks_cut.png"; SL="/Users/wetrade/Documents/Brand Image Generation/Atwood_Heritage_Amazon_Images/_research/_resume10/slices_cut.png"
# context scene templates; {p}=product noun, {carry}=how it's carried
CTX={
"trail":"OUTDOOR TRAIL: a hiker shown from chest-down (NO face) on a sunny mountain trail, one hand holding {p} mid-snack, a daypack strap and trekking pole visible, pine forest and blue sky behind, crisp fresh daylight, product clearly in focus in the foreground.",
"school":"SCHOOL/CAMPUS: a student shown hands-and-torso only (NO face) pulling {p} from an open backpack next to books and a water bottle, bright lockers/hallway softly blurred behind, casual daytime, product clearly in focus.",
"work":"AT WORK: a person shown hands-and-torso only (NO face) at a tidy modern office desk with a laptop and coffee mug, holding {p} on a short work break, soft window daylight, product clearly in focus in the foreground.",
"everyday":"EVERYDAY ON-THE-GO: a person shown hands only (NO face) in an everyday moment — car cupholder / gym-bag / couch — holding {p}, phone and keys nearby, warm casual daily-life light, product clearly in focus.",
}
STICK=dict(ref=PEP,p="a thin smoked snack stick (wrinkled natural casing)",
  tex="The attached PNG is a REAL Atwood smoked meat snack stick — use it as the TEXTURE/SHAPE reference for a thin dry snack stick with a wrinkled natural casing.")
SLICE=dict(ref=SL,p="a small resealable snack pack of round cured salami slices",
  tex="The attached PNG is a REAL Atwood cured-meat SLICE — use it as the TEXTURE/SHAPE reference for round cured salami slices.")
SS=dict(ref=SL,p="a summer-sausage chub with a few slices in a small snack pack",
  tex="The attached PNG is a REAL Atwood cured-meat SLICE — use it as the TEXTURE reference for the cured-meat surface.")
# which product profile per ASIN
PROF={
"B0G4SL5STQ":STICK,"B0G4SHBQSV":STICK,"B0G4SKZLJG":STICK,"B0G4SLCJMX":STICK,"B0G4SJJK1F":STICK,
"B0858JH8R9":STICK,"B0FBSDH627":STICK,"B0FBS9XQWS":STICK,"B0FBSF8K9K":STICK,"B0FBSF8RB3":STICK,"B0G4VRMHXN":STICK,
"B0FBS8TMCQ":SLICE,"B0FBS8HKM5":SLICE,"B0FBSBCHTQ":SLICE,"B0FBSCFKJS":SLICE,"B0FBSCNBHS":SLICE,
"B0856ZDR63":SS,"B0G4SK5FH6":SS,
}
PRE="Premium editorial lifestyle food photography, SQUARE, natural light, shallow depth of field, appetizing, authentic, magazine quality. {tex} No text, no logos, no packaging brands, no readable labels."
lock=threading.Lock()
def run(job):
    asin,ctx,body,prof=job
    outdir=f"{B}/{asin}/everyday"; os.makedirs(outdir,exist_ok=True)
    dst=f"{outdir}/{ctx}.png"
    if os.path.exists(dst):
        with lock: print("SKIP",asin,ctx); return
    prompt=f"{PRE.format(tex=prof['tex'])}  COMPOSITION: {body}  Generate ONE square photorealistic image; just generate it, do not resize."
    try:
        p=subprocess.run([CODEX,"exec","--skip-git-repo-check","-s","workspace-write","-c","model_reasoning_effort=low",prompt,"-i",prof['ref']],
                         stdin=subprocess.DEVNULL,capture_output=True,text=True,timeout=520)
    except Exception:
        with lock: print("TIMEOUT",asin,ctx); return
    out=p.stdout+p.stderr
    if "hit your usage limit" in out:
        with lock: print("USAGE-LIMIT",asin,ctx); return
    m=re.search(r'session id:\s*(\S+)',out)
    if not m:
        with lock: print("NOSID",asin,ctx); return
    imgs=glob.glob(os.path.expanduser(f"~/.codex/generated_images/{m.group(1)}/*.png"))
    if not imgs:
        with lock: print("NOIMG",asin,ctx); return
    ImageOps.fit(Image.open(imgs[0]).convert("RGB"),(2048,2048),Image.LANCZOS).save(dst)
    with lock: print("OK",asin,ctx)
if __name__=="__main__":
    asins=sys.argv[1:] or ["B0G4SL5STQ"]
    jobs=[]
    for a in asins:
        prof=PROF[a]
        for ctx,tpl in CTX.items(): jobs.append((a,ctx,tpl.format(p=prof['p']),prof))
    with ThreadPoolExecutor(max_workers=12) as ex: list(ex.map(run,jobs))
    print("EVERYDAY_GEN_DONE")
