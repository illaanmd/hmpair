"""script for filtering pokemon ids held in HMs and printing
the pokemon pairs that can learn 8 different HMs (4 each)"""
pokedex = [None, "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
           "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle",
           "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow",
           "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "NidoranF",
           "Nidorina", "Nidoqueen", "NidoranM", "Nidorino", "Nidoking", "Clefairy", "Clefable",
           "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom",
           "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth",
           "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine",
           "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke",
           "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel",
           "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite",
           "Magneton", "Farfetchd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk",
           "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno",
           "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone",
           "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn",
           "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking",
           "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir",
           "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon",
           "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl",
           "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite",
           "Mewtwo", "Mew", "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava",
           "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot",
           "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn",
           "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy",
           "Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip",
           "Skiploom", "Jumpluff", "Aipom", " Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire",
           "Espeon", "Umbreon", "Murkrow", "Slowking", "Misdreavus", "Unown", "Wobbuffet",
           "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", "Snubbull",
           "Granbull", "Qwilfish", "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa",
           "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid",
           "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Kingdra",
           "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop",
           "Smoochum", "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune",
           "Larvitar", "Pupitar", "Tyranitar", "Lugia", "Ho-Oh", "Celebi", "Treecko", "Grovyle",
           "Sceptile", "Torchic", "Combusken", "Blaziken", "Mudkip", "Marshtomp", "Swampert",
           "Poochyena", "Mightyena", "Zigzagoon", "Linoone", "Wurmple", "Silcoon", "Beautifly",
           "Cascoon", "Dustox", "Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry",
           "Taillow", "Swellow", "Wingull", "Pelipper", "Ralts", "Kirlia", "Gardevoir", "Surskit",
           "Masquerain", "Shroomish", "Breloom", "Slakoth", "Vigoroth", "Slaking", "Nincada",
           "Ninjask", "Shedinja", "Whismur", "Loudred", "Exploud", "Makuhita", "Hariyama",
           "Azurill", "Nosepass", "Skitty", "Delcatty", "Sableye", "Mawile", "Aron", "Lairon",
           "Aggron", "Meditite", "Medicham", "Electrike", "Manectric", "Plusle", "Minun", "Volbeat",
           "Illumise", "Roselia", "Gulpin", "Swalot", "Carvanha", "Sharpedo", "Wailmer", "Wailord",
           "Numel", "Camerupt", "Torkoal", "Spoink", "Grumpig", "Spinda", "Trapinch", "Vibrava",
           "Flygon", "Cacnea", "Cacturne", "Swablu", "Altaria", "Zangoose", "Seviper", "Lunatone",
           "Solrock", "Barboach", "Whiscash", "Corphish", "Crawdaunt", "Baltoy", "Claydol",
           "Lileep", "Cradily", "Anorith", "Armaldo", "Feebas", "Milotic", "Castform", "Kecleon",
           "Shuppet", "Banette", "Duskull", "Dusclops", "Tropius", "Chimecho", "Absol", "Wynaut",
           "Snorunt", "Glalie", "Spheal", "Sealeo", "Walrein", "Clamperl", "Huntail", "Gorebyss",
           "Relicanth", "Luvdisc", "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", "Metagross",
           "Regirock", "Regice", "Registeel", "Latias", "Latios", "Kyogre", "Groudon", "Rayquaza",
           "Jirachi", "Deoxys", "Turtwig", "Grotle", "Torterra", "Chimchar", "Monferno",
           "Infernape", "Piplup", "Prinplup", "Empoleon", "Starly", "Staravia", "Staraptor",
           "Bidoof", "Bibarel", "Kricketot", "Kricketune", "Shinx", "Luxio", "Luxray", "Budew",
           "Roserade", "Cranidos", "Rampardos", "Shieldon", "Bastiodon", "Burmy", "Wormadam",
           "Mothim", "Combee", "Vespiquen", "Pachirisu", "Buizel", "Floatzel", "Cherubi", "Cherrim",
           "Shellos", "Gastrodon", "Ambipom", "Drifloon", "Drifblim", "Buneary", "Lopunny",
           "Mismagius", "Honchkrow", "Glameow", "Purugly", "Chingling", "Stunky", "Skuntank",
           "Bronzor", "Bronzong", "Bonsly", "MimeJr", "Happiny", "Chatot", "Spiritomb", "Gible",
           "Gabite", "Garchomp", "Munchlax", "Riolu", "Lucario", "Hippopotas", "Hippowdon",
           "Skorupi", "Drapion", "Croagunk", "Toxicroak", "Carnivine", "Finneon", "Lumineon",
           "Mantyke", "Snover", "Abomasnow", "Weavile", "Magnezone", "Lickilicky", "Rhyperior",
           "Tangrowth", "Electivire", "Magmortar", "Togekiss", "Yanmega", "Leafeon", "Glaceon",
           "Gliscor", "Mamoswine", "Porygon-Z", "Gallade", "Probopass", "Dusknoir", "Froslass",
           "Rotom", "Uxie", "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", "Regigigas",
           "Giratina", "Cresselia", "Phione", "Manaphy", "Darkrai", "Shaymin", "Arceus"]

move_set = [15, 23, 27, 29, 30, 31, 39, 43, 45, 46, 47, 51, 53, 54, 55, 57, 58, 59, 60, 61, 62,
            63, 71, 75, 77, 78, 79, 83, 85, 86, 87, 89, 90, 91, 92, 93, 94, 95, 99, 101, 102, 103,
            105, 106, 107, 108, 109, 110, 111, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122,
            123, 124, 125, 126, 127, 135, 139, 141, 142, 143, 147, 149, 150, 151, 153, 154, 155,
            156, 157, 158, 159, 163, 165, 166, 167, 169, 170, 171, 172, 173, 174, 175, 177, 178,
            179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 195, 197, 198, 199,
            201, 202, 203, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218,
            219, 220, 221, 222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236,
            237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253,
            254, 255]

cort = [1, 2, 3, 4, 5, 6, 15, 30, 33, 34, 43, 47, 50, 98, 114, 149, 151, 154, 155, 159, 160, 161,
        253, 254, 255, 275, 286, 287, 331, 332, 341, 342, 347, 359, 388, 389, 390, 391, 392, 393,
        394, 395, 399, 400, 402, 406, 407, 409, 416, 417, 424, 426, 427, 428, 431, 432, 434, 435,
        443, 444, 445, 451, 452, 454, 455, 461, 465]

vuel = [6, 16, 17, 18, 21, 22, 25, 26, 41, 42, 83, 84, 85, 142, 144, 145, 146, 149, 151, 163, 164,
        169, 176, 178, 198, 225, 227, 249, 250, 276, 277, 278, 279, 329, 330, 333, 334, 357, 373,
        380, 381, 384, 396, 397, 398, 426, 430, 441, 468, 487, 493]

surf = [7, 8, 9, 25, 26, 31, 34, 54, 55, 60, 61, 62, 72, 73, 79, 80, 86, 87, 90, 91, 98, 99,
        108, 112, 115, 116, 117, 118, 119, 120, 121, 128, 130, 131, 134, 138, 139, 140, 141, 143,
        147, 148, 149, 151, 158, 159, 160, 161, 162, 170, 171, 172, 183, 184, 186, 194, 195, 199,
        211, 215, 222, 223, 224, 226, 230, 241, 245, 248, 249, 258, 259, 260, 263, 264, 270, 271,
        272, 279, 295, 296, 297, 298, 306, 318, 319, 320, 321, 339, 340, 341, 342, 349, 350, 363,
        364, 365, 366, 367, 368, 369, 370, 380, 381, 382, 384, 393, 394, 395, 400, 409, 418, 419,
        422, 423, 445, 446, 456, 457, 458, 461, 463, 464, 484, 489, 490, 493]

fuer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 39,
        40, 54, 55, 56, 57, 58, 59, 61, 62, 66, 67, 68, 74, 75, 76, 77, 78, 79, 80, 88, 89, 94, 95,
        98, 99, 102, 103, 104, 105, 106, 107, 108, 111, 112, 113, 115, 125, 126, 127, 128, 130, 131,
        134, 135, 136, 142, 143, 149, 150, 151, 153, 154, 156, 157, 159, 160, 162, 166, 180, 181,
        183, 184, 185, 186, 190, 195, 199, 203, 204, 205, 206, 207, 208, 209, 210, 212, 213, 214,
        215, 216, 217, 219, 220, 221, 222, 229, 231, 232, 236, 237, 241, 242, 243, 244, 248, 249,
        250, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 264, 271, 272, 274, 275, 286, 287,
        288, 289, 294, 295, 296, 297, 299, 301, 303, 304, 305, 306, 307, 308, 309, 310, 316, 317,
        319, 320, 321, 322, 323, 324, 327, 328, 329, 330, 332, 335, 336, 340, 341, 342, 344, 346,
        348, 352, 356, 357, 359, 363, 364, 365, 371, 372, 373, 375, 376, 377, 378, 379, 382, 383,
        384, 386, 387, 388, 389, 390, 391, 392, 394, 395, 400, 402, 403, 404, 405, 408, 409, 410,
        411, 418, 419, 423, 424, 428, 435, 437, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452,
        453, 454, 460, 461, 463, 464, 465, 466, 467, 470, 471, 472, 473, 475, 476, 477, 483, 484,
        485, 486, 487, 491, 493]

desp = [6, 12, 15, 16, 17, 18, 21, 22, 41, 42, 49, 83, 123, 142, 144, 145, 146, 149, 151, 163, 164,
        166, 169, 176, 178, 193, 198, 207, 212, 225, 226, 227, 249, 250, 255, 256, 257, 267, 269,
        273, 274, 275, 276, 277, 278, 279, 284, 291, 313, 314, 329, 330, 333, 334, 351, 357, 358,
        373, 380, 381, 384, 393, 394, 395, 396, 397, 398, 414, 416, 425, 426, 430, 434, 435, 441,
        455, 456, 457, 468, 469, 472, 479, 487, 493]

golp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 19, 20, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
        46, 47, 50, 51, 54, 55, 56, 57, 58, 59, 61, 62, 66, 67, 68, 74, 75, 76, 80, 89, 94, 95, 98,
        99, 104, 105, 106, 107, 108, 111, 112, 113, 114, 115, 123, 125, 126, 127, 128, 130, 131,
        134, 135, 136, 138, 139, 140, 141, 142, 143, 144, 145, 146, 149, 150, 151, 153, 154, 156,
        157, 159, 160, 162, 166, 175, 176, 180, 181, 183, 184, 185, 186, 190, 194, 195, 199, 203,
        204, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222,
        227, 228, 229, 231, 232, 236, 237, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249,
        250, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 271, 272, 273, 274,
        275, 286, 287, 288, 289, 294, 295, 296, 297, 299, 301, 302, 303, 304, 305, 306, 307, 308,
        316, 317, 319, 320, 321, 322, 323, 324, 327, 328, 329, 330, 334, 335, 336, 340, 341, 342,
        344, 346, 347, 348, 352, 356, 357, 359, 363, 364, 365, 369, 371, 372, 373, 375, 376, 377,
        378, 379, 382, 383, 384, 386, 387, 388, 389, 390, 391, 392, 394, 395, 399, 400, 402, 408,
        409, 410, 411, 418, 419, 423, 424, 427, 428, 434, 435, 437, 443, 444, 445, 446, 447, 448,
        449, 450, 451, 452, 453, 454, 460, 461, 463, 464, 465, 466, 467, 468, 470, 471, 472, 473,
        475, 476, 477, 483, 484, 485, 486, 487, 491, 493]

casc = [7, 8, 9, 54, 55, 60, 61, 62, 72, 73, 86, 87, 116, 117, 118, 119, 120, 121, 130, 131, 134,
        138, 139, 140, 141, 147, 148, 149, 151, 158, 159, 160, 170, 171, 183, 184, 186, 194, 195,
        211, 223, 224, 226, 230, 245, 249, 258, 259, 260, 271, 272, 298, 318, 319, 320, 321, 339,
        340, 341, 342, 349, 350, 363, 364, 365, 366, 367, 368, 369, 370, 380, 381, 382, 384, 393,
        394, 395, 400, 418, 419, 423, 456, 457, 458, 489, 490, 493]

trep = [3, 9, 27, 28, 31, 34, 55, 56, 57, 59, 62, 66, 67, 68, 74, 75, 76, 95, 104, 105, 106, 107,
        108, 111, 112, 113, 115, 125, 126, 127, 128, 139, 141, 143, 150, 151, 154, 157, 160, 181,
        207, 208, 210, 217, 242, 243, 244, 245, 248, 254, 257, 260, 263, 264, 272, 288, 289, 295,
        296, 297, 306, 335, 377, 378, 379, 383, 387, 388, 389, 390, 391, 392, 395, 399, 400, 408,
        409, 443, 444, 445, 446, 448, 452, 453, 454, 460, 463, 464, 466, 467, 472, 473, 485, 486,
        487, 491, 493]

moves = [None]
i = 0

while i <= 493:
    moves.append(0x00)
    if i in cort:
        moves[i] = moves[i] + 0x01
    if i in vuel:
        moves[i] = moves[i] + 0x02
    if i in surf:
        moves[i] = moves[i] + 0x04
    if i in fuer:
        moves[i] = moves[i] + 0x08
    if i in desp:
        moves[i] = moves[i] + 0x10
    if i in golp:
        moves[i] = moves[i] + 0x20
    if i in casc:
        moves[i] = moves[i] + 0x40
    if i in trep:
        moves[i] = moves[i] + 0x80
    if moves[i] not in move_set:
        pass
        #moves[i] = 0x00
    i = i + 1

i = 1
while i <= 493:
    print(str(i) + " " + pokedex[i] + "  " + hex(moves[i]))
    i = i + 1

print(len(pokedex))
print(len(moves))
print(moves.index(255))
