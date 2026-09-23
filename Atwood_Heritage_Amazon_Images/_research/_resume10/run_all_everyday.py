#!/usr/bin/env python3
import glob, os, importlib.util, sys
BASE="/Users/wetrade/Documents/Brand Image Generation/Atwood_Heritage_Amazon_Images/_research/_resume10"
B="/Users/wetrade/Documents/Brand Image Generation/Atwood_Heritage_Amazon_Images"
def load(mod):
    spec=importlib.util.spec_from_file_location(mod,f"{BASE}/{mod}.py"); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
gen=load("gen_everyday"); comp=load("compose_everyday")
# asin -> folder
fmap={}
for d in sorted(glob.glob(f"{B}/B0*_*")):
    if os.path.isdir(d): fmap[os.path.basename(d).split("_")[0]]=os.path.basename(d)
ASINS=list(gen.PROF.keys())
# 1) generate scenes for all (skips existing)
from concurrent.futures import ThreadPoolExecutor
jobs=[]
for a in ASINS:
    prof=gen.PROF[a]
    for ctx,tpl in gen.CTX.items(): jobs.append((a,ctx,tpl.format(p=prof['p']),prof))
with ThreadPoolExecutor(max_workers=12) as ex: list(ex.map(gen.run,jobs))
print("GEN PHASE DONE")
# 2) compose those whose 4 scenes exist
done=0
for a in ASINS:
    ed=f"{B}/_references/{a}/everyday"
    if all(os.path.exists(f"{ed}/{k}.png") for k in ["trail","school","work","everyday"]):
        comp.render(a,fmap[a]); done+=1
    else:
        print("INCOMPLETE",a,[k for k in ["trail","school","work","everyday"] if not os.path.exists(f"{ed}/{k}.png")])
print(f"COMPOSE PHASE DONE {done}/18")
print("ALL_EVERYDAY_DONE")
