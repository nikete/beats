
Clock.bpm=100
Root.default = 3
Scale.default="minor"
p1 >> keys([0,-1,-2,-3], dur=8, lpf=480, lpr=0.1, crush=8) + (0,2,4,const(6))
p3 >> donk(p1.pitch, dur=8, sus=4, room=1, oct=5, amp=0.9) + [0,0,0,P*(2,4,3,-1)]
p2 >> blip(P[:5][:9][:16], dur=4, oct=var([3,4],[12,4])).penta()
d1 >> play("(x )( x)o{ vx[xx]}", crush=16, rate=.8).every([24,5,3], "stutter", 4, dur=3)
d2 >> play("<-s>< ~*~>").every(30.5, "jump", cycle=32)
