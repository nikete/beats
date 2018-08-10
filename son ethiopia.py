son_durs = P[3,3,4,2,4]
son_accent = [1,0.4,0.8,0.8,0.3]
N_hits = len(son_durs)
p2 >> play(P["p"].stretch(N_hits),dur=son_durs,sample=4,pan=(1,-1),amp=son_accent)
p3 >> play(P["t"].stretch(N_hits),dur=son_durs,sample=4,amp=son_accent)
Clock.bpm = 180
Root.default =-2
Scale.default = 'minor'
d1 >> dbass(P[0,1,2,5,4,2,1,0,1,0,-2,-3,-2,-3],tremolo=0,dur=P[6,1,1,3,3,1,1,6,1,1,3,3,1,1],sample=1)
