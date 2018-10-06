
# Amen
# Merges and laces the first and last two items such that a
# drum pattern "x-o-" would become "(x[xo])-o([-o]-)"
d1 >> play(P["x-o-"].amen(), sample=2, amp=1/4)
print(P[:8].amen())


#trying to get Cm9-Dm7-Gm7-Am7, still need to figure out how to do the 9th
# Use 'var' with your Player objects to create chord progressions.
a = var([0,1,5,6], 4)
b1 >> dbass(a, dur=PDur(5,16))
p1 >> keys(a+ (0,2,4,6), dur=PDur(5,16))
Scale.default = 'minor'
Root.default = 0
