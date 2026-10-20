"""Cinematic logo sting soundtrack — deep swell, riser, soft impact with reverb tail, glass pad, settle.
No bells, no chimes. Deterministic. Usage: python3 audio.py <dur> <out.wav>"""
import numpy as np, sys, wave

SR = 48000
DUR = float(sys.argv[1]) if len(sys.argv) > 1 else 8.0
OUT = sys.argv[2] if len(sys.argv) > 2 else 'sting.wav'
N = int(SR*DUR); t = np.arange(N)/SR
rng = np.random.default_rng(11)
HIT = 1.30                      # logo bloom moment (matches the video)
END = DUR - 0.9                 # settle moment

def lp(x, fc, order=2):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1/SR)
    return np.fft.irfft(X/np.sqrt(1+(f/max(fc,1))**(2*order)), n=len(x))
def hp(x, fc, order=2):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1/SR)
    return np.fft.irfft(X/np.sqrt(1+(max(fc,1)/np.maximum(f,1e-6))**(2*order)), n=len(x))
def bp(x, lo, hi, order=2): return hp(lp(x, hi, order), lo, order)
def adsr(start, a, hold, d):
    tt = t-start; e = np.zeros_like(t); m = tt >= 0; x = tt[m]
    e[m] = np.where(x < a, (x/a)**2, np.where(x < a+hold, 1.0, np.exp(-(x-a-hold)/d))); return e
def reverb(x, rt=2.2, wet=0.35, pre=0.02):
    n = int(SR*rt); ir = rng.standard_normal(n)*np.exp(-np.arange(n)/(SR*rt/6.9))
    ir = lp(ir, 6500, 1); ir[:int(SR*pre)] = 0; ir /= np.sqrt((ir**2).sum())
    y = np.fft.irfft(np.fft.rfft(x, len(x)+n)*np.fft.rfft(ir, len(x)+n))[:len(x)]
    return x*(1-wet) + y*wet*1.6
def stereo(x, width=0.0, pan=0.0):
    """pan in [-1,1]; width adds decorrelated highs"""
    l = x*np.sqrt((1-pan)/2); r = x*np.sqrt((1+pan)/2)
    if width>0:
        d = int(SR*0.011); s = np.zeros_like(x); s[d:] = x[:-d]
        l = l + width*hp(s, 1200)*0.5; r = r - width*hp(s,1200)*0.5
    return np.stack([l,r],1)

mix = np.zeros((N,2))

# 1) sub swell: 38→52 Hz, rises into the hit, then hands over to the boom
f_sub = 38 + 14*np.clip(t/HIT,0,1)
sub = np.sin(2*np.pi*np.cumsum(f_sub)/SR) * np.clip(t/HIT,0,1)**2.2 * (t<HIT)
mix += stereo(sub*0.55)

# 2) riser: filtered noise sweeping up + soft harmonic riser (octave climb), 0 → HIT
wn = rng.standard_normal(N)
seg = (t<HIT)
sweep = np.zeros(N)
# time-varying bandpass via 6 bands crossfaded
bands = [(120,400),(250,800),(500,1600),(900,3000),(1500,5000),(2500,8000)]
for i,(lo,hi) in enumerate(bands):
    w = np.clip(1-np.abs(t/HIT*(len(bands)-1)-i),0,1)
    sweep += bp(wn,lo,hi,2)*w
riser_env = (np.clip(t/HIT,0,1)**3)*seg
sweep = sweep*riser_env
mix += stereo(sweep*0.22, width=0.6)
f0 = 110*2**(np.clip(t/HIT,0,1)*1.0)          # A2 → A3
harm = sum(np.sin(2*np.pi*np.cumsum(f0*m)/SR)/m for m in (1,2,3,4,5))
harm = lp(harm, 2500)*riser_env
mix += stereo(harm*0.10, width=0.3)

# 3) impact at HIT: boom (pitch drop) + body thud + air; goes into reverb
boom_f = 48 + 90*np.exp(-np.maximum(t-HIT,0)*9)
boom = np.sin(2*np.pi*np.cumsum(boom_f)/SR) * adsr(HIT, 0.004, 0.05, 0.9)
thud = bp(rng.standard_normal(N), 90, 500, 2) * adsr(HIT, 0.003, 0.0, 0.11)
air  = bp(rng.standard_normal(N), 2500, 11000, 2) * adsr(HIT, 0.002, 0.0, 0.22)
impact = boom*0.9 + thud*0.7 + air*0.28
impact_wet = reverb(impact, rt=2.4, wet=0.45)
mix += stereo(impact_wet*0.42, width=0.5)

# 4) glass pad after the hit: A2 + E3 + A3 + C#4 (soft major), detuned, filtered, swelling then leaving
def voice(f, det=0.0):
    ph = np.cumsum(np.full(N, f*(1+det)))/SR
    return (np.sin(2*np.pi*ph) + 0.5*np.sin(2*np.pi*2*ph) + 0.25*np.sin(2*np.pi*3*ph) + 0.12*np.sin(2*np.pi*4*ph))
pad = np.zeros(N)
for f in (110.0, 164.81, 220.0, 277.18, 329.63):
    for det in (-0.006, 0.0, 0.007): pad += voice(f, det)
pad = lp(pad, 900 + 1400*np.clip((t-HIT)/3,0,1).mean(), 2)
pad_env = adsr(HIT+0.05, 2.2, 2.6, 0.9)
pad = pad*pad_env
pad = reverb(pad, rt=3.0, wet=0.35)
mix += stereo(pad*0.028, width=0.8)

# 5) turning texture: three very soft airy swells synced with the 3-fold turn (barely there)
turn = bp(rng.standard_normal(N), 1200, 7000, 2)
tenv = 0.5*(1-np.cos(2*np.pi*3*(t-HIT)/(DUR-HIT))) * ((t>HIT)&(t<END))
mix += stereo(turn*tenv*0.045, width=0.9)

# 6) settle at END: soft low thump + short air, then everything fades
settle_f = 42 + 40*np.exp(-np.maximum(t-END,0)*10)
settle = np.sin(2*np.pi*np.cumsum(settle_f)/SR)*adsr(END, 0.004, 0.02, 0.5)*0.55 + bp(rng.standard_normal(N),1800,9000,2)*adsr(END,0.002,0,0.12)*0.14
mix += stereo(reverb(settle, rt=1.6, wet=0.35)*0.5)

# master: gentle tilt, fade-out, soft limiter, normalize
mix = np.stack([lp(mix[:,0], 14000, 1), lp(mix[:,1], 14000, 1)], 1)
mix *= np.clip((DUR-t)/0.6, 0, 1)[:,None]
mix = np.tanh(mix*1.4)/1.4                      # soft clip
peak = np.abs(mix).max(); mix = mix/peak*0.70
pcm = (mix*32767).astype(np.int16)
with wave.open(OUT, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
rms = 20*np.log10(np.sqrt((mix**2).mean())+1e-9)
print('wrote', OUT, 'peak', round(float(peak),3), 'rms dBFS', round(float(rms),1))
