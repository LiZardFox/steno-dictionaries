LONGEST_KEY = 2

# binary list of modifiers for first stroke, ctrl = 1, alt = 2, shift = 4, super = 8

fancytext = "#TPA"

retro = [
    "#TPAR",  # retro 1 word
    "#TPAB",  # retro 2 word
    "#TPAG",  # retro 3 word
    "#TPAFR",  # retro 4 word
    "#TPAPB",  # retro 5 word
    "#TPALG",  # retro 6 word
    "#TPAF",  # retro 7 word
    "#TPAP",  # retro 8 word
    "#TPAL",  # retro 9 word
]

figlet = [
    "#TPEUR",
    "#TPEUB",
    "#TPEUG",
    "#TPEUFR",
    "#TPEUPB",
    "#TPEULG",
    "#TPEUF",
    "#TPEUP",
    "#TPEUL",
    ]

fig_fonts = {
   "PWEUG": "big",
   "PWHROBG": "block",
   "KAT": "catwalk",
   "TKO": "doh",
   "SPHAL": "eftifont",
   "PHET": "isometric1",
   "#-GD": "larry3d",
   "HRAOEPB": "lean",
   "ROEPL": "roman",
   "AOUPB": "univers"
}



modes = {
    "PWUB": "bubble",
    "PHORS": "morse",
    "KRAOEU": "crytyping",
    "SRAEUP": "fullwidth",
    "PHED": "medieval",
    "SARBG": "sarcasm",
    "UP": "upsidedown",
    "SPHAL": "smallcaps",
    "SKREUPT": "script",
    "PWHRABG": "blackboardbold",
    "PHOPB": "monospace",
    "AOU": "uwu",
    "AO*U": "UwU",
    "STKPWAL": "zalgo",
    "STKPWAEL": "zalgo:10:15",
    "STKPWAUL": "zalgo:20:30",
    "STKPWAEUL": "zalgo:30:50",
}

def first_stroke_valid(stroke):
    isfancytext = stroke == fancytext
    isRetro = stroke in retro
    isFiglet = stroke in figlet
    return isfancytext or isRetro or isFiglet

def do_figlet(stroke1, stroke2):
    n = figlet.index(stroke1) + 1
    if stroke2 not in fig_fonts:
        raise KeyError
    return "{" + f":fancytext_retro:{n}:figlet:{fig_fonts[stroke2]}" + "}"

def lookup(outline):
    assert len(outline) <= LONGEST_KEY
    str1 = outline[0]
    # KeyError if first stroke is not valid
    if not first_stroke_valid(str1):
        raise KeyError
    if len(outline) == 1:
        if str1 == fancytext:
            return "{:fancytext_set:off}"
        else: 
            raise KeyError

    # length should be 2
    assert len(outline) == 2
    str2 = outline[1]
    
    if str1 in figlet:
        return do_figlet(str1, str2)
    # do nothing if second stroke is a valid mode
    if str2 not in modes:
        raise KeyError
    assert str2 in modes
    # get key to press from second stroke
    mode = modes.get(str2)

    if fancytext == str1:
        trans = "fancytext_set"
    else:
        n = retro.index(str1) + 1
        trans = "fancytext_retro:" + str(n)

    return "{:" + trans + ":" + mode + "}" 
