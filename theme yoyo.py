theme_durs = P[2,2,1,2,4,1,1/2,1/2,1,1,1]
son_accent = []
N_hits = len(son_durs)
p2 >> play(P["p"].stretch(N_hits),dur=son_durs,sample=4,pan=(1,-1),amp=son_accent)
p3 >> play(P["t"].stretch(N_hits),dur=son_durs,sample=4,amp=son_accent)
Clock.bpm = 240
Root.default =0
Scale.default = 'minor'
d1 >> dbass(P[0,0,-1,0,2,0,3,2,0,-1,0,0,0,-1,0,3,0,3,2,0,-1,0,],tremolo=0,dur=theme_durs,sample=1)
