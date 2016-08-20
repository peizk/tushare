

def Turntonum(t):
    t=t.split(':');
    nine_half=9*60*60+30*60;
    eleven_half=11*60*60+30*60;
    twelve=12*60*60;
    thirtheen=13*60*60;
    fifteen=15*60*60;
    hour=int(t[0]);
    minute=int(t[1]);
    second=int(t[2]);
    i=0;

    time=hour*60*60+minute*60+second;
    if(time<nine_half):
        i=1;
    elif(time<eleven_half):
        i=time-nine_half+1;
    elif(time<thirtheen):
        i=eleven_half-nine_half+1;
    elif(time<fifteen):
        i=time-thirtheen+1+eleven_half-nine_half+1;
    else:
        i=fifteen-thirtheen+1+eleven_half-nine_half+1;

    return i;
