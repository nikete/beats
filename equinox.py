durs= P[3]
accent = P[0.75,1,0.5,1]
N_hits = len(durs)
p2 >> play(P["p"].stretch(N_hits),dur=P[3],sample=4,pan=(1,-1),amp=accent)
p3 >> play(P["t"].stretch(N_hits),dur=P[3],sample=4,amp=accent)
Clock.bpm = 350
Root.default =0
Scale.default = 'minor'
d1 >> dbass(P[0,7,6,5.5,4,3.5,3,-0.5,
              0,1,2,3,3.5,5,2,2.5,
              3,4,5,9,10,6.5,6,5,
              0,1,2,3,4,3.5,3,0,
              -2,0,1,2,-3,-0.5,2,0.5,
              0,7,3.5,3,2,1,0,-1
    ],tremolo=0,dur=P[3],amp=accent,sample=0)
