hertz = 16393442

unit=[
    ("hertz", "Hz"), 
    ("kilohertz", "kHz"),
    ("megahertz", "MHz"), 
    ("gigahertz", "GHz"), 
    ("terahertz", "THz"), 
    ("petahertz", "PHz"), 
    ("exahertz", "EHz"), 
    ("zettahertz", "ZHz"), 
    ("yottahertz", "YHz")
]

i = 0
while hertz >= 1000:
    i+=1
    hertz/=1000

print(str(hertz) + unit[i][1])