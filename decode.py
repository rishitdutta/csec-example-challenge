from PIL import Image

im = Image.open("big-chonk.png")
w,h = im.size
bits = []
for x in range(w):
  for y in range(h):  #row-major order
    p = im.getpixel((x,y))
    r, g, b, a = im.getpixel((x, y))    #this image has the alpha(a) channel too which determines the opacity of the pixel
    bits.append(str(r & 1))       #r is 1 byte, so doing bitwise & with 1 (which is same as 00000001) we can get the LSB of r
    bits.append(str(g & 1))          
    bits.append(str(b & 1)) 
    bits.append(str(a & 1)) 
s = "".join(bits)

open("bits.txt","w").write(s)
