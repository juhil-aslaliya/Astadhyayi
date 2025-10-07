# svara
a   = 'a0'
aa  = 'a1'
i   = 'i0'
ii  = 'i1'
u   = 'u0'
uu  = 'u1'
R   = 'R0'
RR  = 'R1'
L   = 'L0'
LL  = 'L1'
e   = 'ee'
ai  = 'AI'
o   = 'oo'
au  = 'AU'

# vyanjana
# k varga
k   = 'k0'
kh  = 'k1'
g   = 'k2'
gh  = 'k3'
ng  = 'n1'
# c varga
c   = 'c0'
ch  = 'c1'
j   = 'c2'
jh  = 'c3'
nj  = 'n2'
# T varga
T   = 'T0'
Th  = 'T1'
D   = 'T2'
Dh  = 'T3'
N   = 'n3'
# t varga
t   = 't0'
th  = 't1'
d   = 't2'
dh  = 't3'
n   = 'n4'
# p varga
p   = 'p0'
ph  = 'p1'
b   = 'p2'
bh  = 'p3'
m   = 'n5'
# antyastha
y   = 'y2'
r   = 'r3'
l   = 'l4'
v   = 'v5'
# ushmakshara
z   = 'z2'
S   = 'S3'
s   = 's4'
h   = 'h1'
# anya vyanjana
lh  = 'l3'

# ayogavaha
# anusvara
M   = '*0'
# visarga
H   = ':0'
# jihvamuliya
X   = '|0'
# upadhmaniya
F   = '=0'

# anya varna
# avagraha
avg = '-0'
# halanta
hal = '_0'

devanagariToTokenMap = {
    'अ'  : a,
    'आ'  : aa,
    'इ'  : i,
    'ई'  : ii,
    'उ'  : u,
    'ऊ'  : uu,
    'ऋ'  : R,
    'ॠ'  : RR,
    'ऌ'  : L,
    'ॡ'  : LL,
    'ए'  : e,
    'ऐ'  : ai,
    'ओ'  : o,
    'औ'  : au,
    'ा'  : aa,
    'ि'  : i,
    'ी'  : ii,
    'ु'  : u,
    'ू'  : uu,
    'ृ'  : R,
    'ॄ'  : RR,
    'ॢ'  : L,
    'ॣ'  : LL,
    'े'  : e,
    'ै'  : ai,
    'ो'  : o,
    'ौ'  : au,
    'क'  : k,
    'ख'  : kh,
    'ग'  : g,
    'घ'  : gh,
    'ङ'  : ng,
    'च'  : c,
    'छ'  : ch,
    'ज'  : j,
    'झ'  : jh,
    'ञ'  : nj,
    'ट'  : T,
    'ठ'  : Th,
    'ड'  : D,
    'ढ'  : Dh,
    'ण'  : N,
    'त'  : t,
    'थ'  : th,
    'द'  : d,
    'ध'  : dh,
    'न'  : n,
    'प'  : p,
    'फ'  : ph,
    'ब'  : b,
    'भ'  : bh,
    'म'  : m,
    'य'  : y,
    'र'  : r,
    'ल'  : l,
    'व'  : v,
    'श'  : z,
    'ष'  : S,
    'स'  : s,
    'ह'  : h,
    'ळ'  : lh,
    '्'  : M,
    'ः'  : H,
    'ᳵ' : X,
    'ᳶ' : F,
    'ऽ' : avg,
    '्' : hal
}

tokenToDevanagariMap = {
    a   : ['अ', ''],
    aa  : ['आ', 'ा'],
    i   : ['इ', 'ि'],
    ii  : ['ई', 'ी'],
    u   : ['उ', 'ु'],
    uu  : ['ऊ', 'ू'],
    R   : ['ऋ', 'ृ'],
    RR  : ['ॠ', 'ॄ'],
    L   : ['ऌ', 'ॢ'],
    LL  : ['ॡ', 'ॣ'],
    e   : ['ए', 'े'],
    ai  : ['ऐ', 'ै'],
    o   : ['ओ', 'ो'],
    au  : ['औ', 'ौ'],
    k   : ['क्'],
    kh  : ['ख्'],
    g   : ['ग्'],
    gh  : ['घ्'],
    ng  : ['ङ्'],
    c   : ['च्'],
    ch  : ['छ्'],
    j   : ['ज्'],
    jh  : ['झ्'],
    nj  : ['ञ्'],
    T   : ['ट्'],
    Th  : ['ठ्'],
    D   : ['ड्'],
    Dh  : ['ढ्'],
    N   : ['ण्'],
    t   : ['त्'],
    th  : ['थ्'],
    d   : ['द्'],
    dh  : ['ध्'],
    n   : ['न्'],
    p   : ['प्'],
    ph  : ['फ्'],
    b   : ['ब्'],
    bh  : ['भ्'],
    m   : ['म्'],
    y   : ['य्'],
    r   : ['र्'],
    l   : ['ल्'],
    v   : ['व्'],
    z   : ['श्'],
    S   : ['ष्'],
    s   : ['स्'],
    h   : ['ह्'],
    lh  : ['ळ्'],
    M   : ['ं'],
    H   : ['ः'],
    X   : ['ᳵ'],
    F   : ['ᳶ'],
    avg : ['ऽ'],
    hal : ['्']
}

svara = [a, aa, 
         i, ii, 
         u, uu, 
         R, RR, 
         L, LL, 
            e, 
            ai, 
            o, 
            au]

vyanjana = [k, kh, g, gh, ng,
            c, ch, j, jh, nj,
            T, Th, D, Dh, N,
            t, th, d, dh, n,
            p, ph, b, bh, m,
            y, r, l, v,
            z, S, s, h,
            lh]

anya = [M, H, X, F, avg]