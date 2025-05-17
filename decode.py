from PIL import Image

im = Image.open("big-chonk.png")
w,h = im.size
bits = []
for x in range(w):
  for y in range(h):
    p = im.getpixel((x,y))
    r, g, b, a = im.getpixel((x, y))     
    bits.append(str(r & 1))         
    bits.append(str(g & 1))          
    bits.append(str(b & 1)) 
    bits.append(str(a & 1)) 
s = "".join(bits)

open("bits.txt","w").write(s)
