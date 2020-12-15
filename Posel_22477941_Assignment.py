import math
import sys

def trackFlow(fin,fout,r,H,h,tmax,topen):
    if r<0 or H<0 or h<0 or tmax<0 or topen<0 or fin<0 or fout<0:
        print("Negative input entered, please enter postitive inputs")
        sys.exit()
    Vtotal = (math.pi)*(H)*(r**2)
    t = 0
    Vn = 0
    hn = 0
    Heights = []
    Times = []
    Volume = []
    while t<=tmax and h<H and h>=0:
        if t == 0:
            Tc = 0
        else: Tc = 0.1
        if t <= topen:
            V = round(Vn + (fin)*(Tc),10)
            h = round(hn + (fin*(Tc)/math.pi*(r**2)),10)
            Volume.append(round(V,2))
            Heights.append(round(h,2))
            Times.append(round(t,2))
            t = round(t+0.1,10)
            Vn = V
            hn = h
           
            
        else:
            V = round(Vn + (fin-fout)*(Tc),10)
            h = round(hn + ((fin-fout)*(Tc)/math.pi*(r**2)),10)
            if t>0 and h<0:
                break            
            Volume.append(round(V,2))
            Heights.append(round(h,2))
            Times.append(round(t,2))
            t = round(t+0.1,10)
            Vn = round(V,10)
            hn = round(h,10)
  
    return(Volume, Heights, Times)

