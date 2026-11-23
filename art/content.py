"""Every word on the page. Facts and sources: research/sources-2026-11-22.md."""

TOP_LEFT = "THE WORLD IN ONE DAY · THE WHOLE DAY, 00:00 TO 24:00 UTC"
TOP_RIGHT = "27 stories · 7 regions · 11 fields · all from Sunday 22 Nov"
DATE = "Sunday 22 November 2026"
SUBLINE = "COP31 ends without a pact · Russia fires 186 drones at Ukraine · Democrats reach 258 US House seats"

NUMBERS = [
    ("186", "drones fired at Ukraine"),
    ("32+", "nations rejected COP31 text"),
    ("258", "House seats for Democrats"),
    ("11,000+", "Ebola cases in DR Congo"),
    ("−1.95%", "Saudi stocks, Sunday trade"),
    ("720/9", "India's record Test in NZ"),
]

UTC = [
    ("00:00", "Drone raids on Sudan"),
    ("06:00", "Kyiv: 161 of 186 downed"),
    ("11:00", "Pope's Angelus for peace"),
    ("12:00", "Saudi index shuts −1.95%"),
    ("12:23", "SpaceX NROL-136 lifts off"),
    ("18:07", "AP: Democrats reach 258"),
]

LEADS = [
    dict(icon="summit", badge="NO DEAL", place="Antalya, Türkiye", tag="CONFIRMED",
         head="COP31 climate summit ends without a pact",
         dek="After two days of overtime, at least 32 nations rejected a text silent on fossil fuels. President Kurum: \"these decisions have not been adopted.\"",
         src="UN News · CNN · Carbon Brief"),
    dict(icon="drones", badge="186", place="Kyiv region, Ukraine", tag="OFFICIAL",
         head="Russia fires 186 drones; block in Dymer collapses",
         dek="Ukraine's air force says 161 were downed or suppressed. Part of a five-storey block near Kyiv fell; Zelensky: 14 residents unreachable.",
         src="Ukrinform · ISW · Euronews"),
    dict(icon="ballot", badge="258", place="Washington", tag="CONFIRMED",
         head="Democrats reach 258 House seats, AP says",
         dek="A recount win in North Carolina's 5th district, ousting Virginia Foxx, gives the largest House majority since 1992.",
         src="AP · CBS · Al Jazeera"),
]

TILES = [
    dict(icon="radar", badge=None, place="Manama, Bahrain", tag="CLAIM",
         head="Iran says it hit US radars; Bahrain denies",
         dek="Bahrain: a civilian plant in Sitra was hit, 2 hurt."),
    dict(icon="ruins", badge=None, place="Khartoum, Sudan", tag="CONFIRMED",
         head="Drones hit Khartoum and a UN building",
         dek="4 killed; the army blames the RSF."),
    dict(icon="ship", badge=None, place="Benghazi, Libya", tag="CONFIRMED",
         head="Russian warship sunk in Libyan port",
         dek="Corvette Merkury capsized after a dawn sea-drone strike."),
    dict(icon="chart_down", badge=None, place="Riyadh", tag="CONFIRMED",
         head="Gulf stocks fall in Sunday trade",
         dek="Saudi index −1.95% to 9,960; Egypt −2.9%."),
    dict(icon="missile", badge=None, place="Washington", tag="OFFICIAL",
         head="Trump \"inclined\" to resume Iran strikes",
         dek="After New Year if no deal, he tells Fox News."),
    dict(icon="virus", badge=None, place="Ituri, DR Congo", tag="OFFICIAL",
         head="Ebola: fighting traps WHO staff in Ituri",
         dek="Outbreak passes 11,000 cases, Reuters says."),
    dict(icon="chart", badge=None, place="Shanghai", tag="OFFICIAL",
         head="China eases margin rules to stem rout",
         dek="Margin requirement cut to 80% from 30 Nov."),
    dict(icon="cricket", badge="720/9", place="Wellington, NZ", tag="CONFIRMED",
         head="India declare on a record 720/9",
         dek="Rahul 136, Pant 128; NZ 119/2 at stumps."),
    dict(icon="tennis", badge=None, place="Turin, Italy", tag="CONFIRMED",
         head="Alcaraz beats Zverev to win ATP Finals",
         dek="6-2, 7-6; a record $5.17m prize."),
    dict(icon="rocket", badge=None, place="Vandenberg, US", tag="CONFIRMED",
         head="SpaceX launches US spy satellites",
         dek="NROL-136 lifts off from Vandenberg, 12:23 UTC."),
]

ALSO_TITLE = "Also on Sunday 22 November"
ALSO = [
    (14, "Middle East", "Houthis claim hit on Saudi refinery"),
    (15, "Middle East", "Tanker in military incident off Iran"),
    (16, "Middle East", "Settlers torch cars in West Bank"),
    (17, "Middle East", "Israel: Likud-Eisenkot talks fail"),
    (18, "Europe", "Liverpool 4-0 Man United"),
    (19, "Europe", "Burning Russian ship leaves Finland"),
    (20, "Europe", "Márquez wins eighth MotoGP crown"),
    (21, "Africa", "Kenya, DR Congo agree to restore ties"),
    (22, "Asia", "South Korea readies stock fund"),
    (23, "Asia", "Drone strikes hurt 10 in Bannu, Pakistan"),
    (24, "Oceania", "Australia rejects US AUKUS warning"),
    (25, "Oceania", "1956 Olympians reunite at the MCG"),
    (26, "Americas", "Bolsonaro stable in intensive care"),
    (27, "World", "OpenAI urges industry-wide AI limits"),
]

PINS = [
    (1, 30.7, 36.9, "Europe"), (2, 30.3, 50.8, "Europe"), (3, -77.0, 38.9, "Americas"),
    (4, 50.6, 26.1, "Middle East"), (5, 32.5, 15.6, "Africa"), (6, 20.1, 32.1, "Africa"),
    (7, 46.7, 24.7, "Middle East"), (9, 30.0, 1.5, "Africa"), (10, 121.5, 31.2, "Asia"),
    (11, 174.8, -41.3, "Oceania"), (12, 7.7, 45.1, "Europe"), (13, -120.6, 34.7, "Americas"),
]

REGION_COUNTS = [("Europe", 6), ("Middle East", 6), ("Americas", 4), ("Africa", 4),
                 ("Asia", 3), ("Oceania", 3), ("World", 1)]

DATECHECK_OUT = ("Not shown, broke before Sunday: Iran's strikes on Bahrain (Sat 21) · the 400-drone barrage "
                 "(19-20 Nov) · BepiColombo at Mercury (Sat 21)")
DATECHECK_NOT_YET = ("Not shown, came after Sunday: Kyiv claims the Benghazi strike (Mon 23) · Dymer toll of 11 (Mon 23) "
                     "· Belgian strike (Mon 23)")
LEGEND = ("CONFIRMED = 2+ outlets · OFFICIAL = on the record · CLAIM = one side's account, attributed · "
          "outlets named under each lead. Pictures are drawn, not photographs.")
