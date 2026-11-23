"""Every word on the page. Facts and sources: research/sources-2026-11-22.md."""

TOP_LEFT = "THE WORLD IN ONE DAY · THE WHOLE DAY, 00:00 TO 24:00 UTC"
TOP_RIGHT = "31 stories · 7 regions · 12 fields · every one from Sunday 22 Nov"
DATE = "Sunday 22 November 2026"
SUBLINE = "COP31 collapses without a deal · Russia fires 186 drones at Ukraine · Democrats reach 258 US House seats"

NUMBERS = [
    ("186", "drones fired at Ukraine"),
    ("32+", "nations rejected COP31 text"),
    ("258", "House seats for Democrats"),
    ("11,000+", "Ebola cases in DR Congo"),
    ("−1.95%", "Saudi stocks, Sunday trade"),
    ("720/9", "India's record Test in NZ"),
]

UTC = [
    ("00:00", "Drones over Khartoum"),
    ("06:00", "Kyiv: 161 of 186 downed"),
    ("11:00", "Pope's Angelus for peace"),
    ("12:00", "Saudi index shuts −1.95%"),
    ("12:23", "SpaceX NROL-136 lifts off"),
    ("18:07", "AP: Democrats reach 258"),
]

LEADS = [
    dict(icon="summit", badge="NO DEAL", place="Antalya, Türkiye", tag="CONFIRMED",
         head="COP31 climate talks collapse without a deal",
         dek="After two days of overtime, at least 32 nations rejected a text silent on fossil fuels. UN chief: \"no ambiguity in the science.\"",
         src="UN News · CNN · Carbon Brief"),
    dict(icon="drones", badge="186", place="Kyiv region, Ukraine", tag="OFFICIAL",
         head="Russia fires 186 drones; block in Dymer collapses",
         dek="Ukraine's air force says 161 were downed or suppressed. Part of a five-storey block near Kyiv fell; Zelensky: 14 residents unreachable.",
         src="Ukrinform · ISW · Euronews"),
    dict(icon="ballot", badge="258", place="Washington", tag="CONFIRMED",
         head="Democrats reach 258 House seats, most since 1992",
         dek="A recount win in North Carolina's 5th district, ousting Virginia Foxx, gives the largest House majority in 34 years.",
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
         dek="Corvette Merkury capsized after a dawn drone strike."),
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
    (14, "Middle East", "Houthis claim hit on Saudi Rabigh refinery"),
    (15, "Middle East", "tanker in military incident near Hormuz"),
    (16, "Middle East", "settlers torch cars in West Bank villages"),
    (17, "Middle East", "Likud and Eisenkot end talks, no deal"),
    (18, "Europe", "Liverpool 4-0 Man United, Pochettino's debut"),
    (19, "Europe", "burning Russian ship leaves Finnish waters"),
    (20, "Europe", "Berlin hospital fire injures 15"),
    (21, "Europe", "Márquez clinches 8th MotoGP title"),
    (22, "Africa", "Kenya and DR Congo to restore ambassadors"),
    (23, "Asia", "South Korea readies stock rescue fund"),
    (24, "Asia", "China vows to hit back at US phone ban"),
    (25, "Asia", "drone strikes hurt 10 at Bannu, Pakistan"),
    (26, "Oceania", "Marles: US budget office \"wrong\" on AUKUS"),
    (27, "Oceania", "1956 Olympians reunite at the MCG at 70"),
    (28, "Americas", "Bolsonaro stable in intensive care"),
    (29, "Americas", "Thitikul wins CME title, third in a row"),
    (30, "World", "OpenAI proposes limits on AI capability"),
    (31, "World", "bitcoin back above $60,000"),
]

PINS = [
    (1, 30.7, 36.9, "Europe"), (2, 30.3, 50.8, "Europe"), (3, -77.0, 38.9, "Americas"),
    (4, 50.6, 26.1, "Middle East"), (5, 32.5, 15.6, "Africa"), (6, 20.1, 32.1, "Africa"),
    (7, 46.7, 24.7, "Middle East"), (9, 30.0, 1.5, "Africa"), (10, 121.5, 31.2, "Asia"),
    (11, 174.8, -41.3, "Oceania"), (12, 7.7, 45.1, "Europe"), (13, -120.6, 34.7, "Americas"),
]

REGION_COUNTS = [("Europe", 7), ("Middle East", 6), ("Americas", 5), ("Africa", 4),
                 ("Asia", 4), ("Oceania", 3), ("World", 2)]

DATECHECK_OUT = ("Left out, before Sunday: Iran's strikes on Bahrain (Sat 21) · the 400-drone barrage (19-20 Nov) "
                 "· Sparta II hit (Sat 21) · BepiColombo at Mercury (Sat 21)")
DATECHECK_NOT_YET = ("Not yet: Ukraine claims the Merkury (Mon 23) · Dymer toll rises to 11 (Mon 23) "
                     "· Belgian strike (Mon 23) · Davis Cup Finals (24 Nov)")
LEGEND = ("CONFIRMED = 2+ outlets · OFFICIAL = on the record · CLAIM = one side's account, attributed. "
          "Pictures are drawn in code, not photographs. Sources: research/sources-2026-11-22.md")
