# ═══════════════════════════════════════════════════════════════════════════════
#  MODULES PARAMATERS
# ═══════════════════════════════════════════════════════════════════════════════

Sections = ["Canalisations", "Turbines", "Générateurs"]
Type = ["Base", "Support", "Améliorante", ]
Tier = [0 ,1, 2, 3, 4, 5]
Resistance = ["Low", "Mid", "High"]
CityLevel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

AllModules = {
    "CTI++": {
        "name": "Canalisation ++",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 800,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 82500,
        "sellPrice": 140,
        "upgradeCost": 412500,
        "upgradeName": "CTII++",
        "parent": []
    },
    "CTI/+": {
        "name": "Canalisation /+",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 650,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 60000,
        "sellPrice": 140,
        "upgradeCost": 300000,
        "upgradeName": "CTII/+",
        "parent": []
    },
    "CTI+/": {
        "name": "Canalisation +/",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 800,
        "yield": 0.25,
        "resistance": Resistance[0],
        "buyCost": 18750,
        "sellPrice": 140,
        "upgradeCost": 75000,
        "upgradeName": "CTII+/",
        "parent": []
    },
    "CTI-+": {
        "name": "Canalisation -+",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 500,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 22500,
        "sellPrice": 140,
        "upgradeCost": 112500,
        "upgradeName": "CTII-+",
        "parent": []
    },
    "CTI//": {
        "name": "Canalisation //",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 650,
        "yield": 0.25,
        "resistance": Resistance[0],
        "buyCost": 41250,
        "sellPrice": 140,
        "upgradeCost": 165000,
        "upgradeName": "CTII//",
        "parent": []
    },
    "CTI-/": {
        "name": "Canalisation -/",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 500,
        "yield": 0.25,
        "resistance": Resistance[0],
        "buyCost": 33750,
        "sellPrice": 140,
        "upgradeCost": 337500,
        "upgradeName": "CTII-/",
        "parent": []
    },
    "CTI+-": {
        "name": "Canalisation +-",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 800,
        "yield": 0.1,
        "resistance": Resistance[0],
        "buyCost": 52500,
        "sellPrice": 140,
        "upgradeCost": 105000,
        "upgradeName": "CTII+-",
        "parent": []
    },
    "CTI/-": {
        "name": "Canalisation /-",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 650,
        "yield": 0.1,
        "resistance": Resistance[0],
        "buyCost": 18750,
        "sellPrice": 140,
        "upgradeCost": 75000,
        "upgradeName": "CTII/-",
        "parent": []
    },
    "CTI--": {
        "name": "Canalisation --",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 500,
        "yield": 0.1,
        "resistance": Resistance[0],
        "buyCost": 11250,
        "sellPrice": 140,
        "upgradeCost": 45000,
        "upgradeName": "CTII--",
        "parent": []
    },
    "CTII++": {
        "name": "Canalisation ++",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 1050,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 412500,
        "sellPrice": 140,
        "upgradeCost": 1375000,
        "upgradeName": "CTIII++",
        "parent": ["CTI++", "CTII++"]
    },
    "CTII/+": {
        "name": "Canalisation /+",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 825,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 300000,
        "sellPrice": 140,
        "upgradeCost": 1000000,
        "upgradeName": "CTIII/+",
        "parent": ["CTI/+", "CTII/+"]
    },
    "CTII+/": {
        "name": "Canalisation +/",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 1050,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 75000,
        "sellPrice": 140,
        "upgradeCost": 250000,
        "upgradeName": "CTIII+/",
        "parent": ["CTI+/", "CTII+/"]
    },
    "CTII-+": {
        "name": "Canalisation -+",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 600,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 112500,
        "sellPrice": 140,
        "upgradeCost": 1375000,
        "upgradeName": "CTIII-+",
        "parent": ["CTI-+", "CTII-+"]
    },
    "CTII//": {
        "name": "Canalisation //",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 825,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 165000,
        "sellPrice": 140,
        "upgradeCost": 150000,
        "upgradeName": "CTIII//",
        "parent": ["CTI//", "CTII//"]
    },
    "CTII-/": {
        "name": "Canalisation -/",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 600,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 337500,
        "sellPrice": 140,
        "upgradeCost": 875000,
        "upgradeName": "CTIII-/",
        "parent": ["CTI-/", "CTII-/"]
    },
    "CTII+-": {
        "name": "Canalisation +-",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 1050,
        "yield": 0.2,
        "resistance": Resistance[0],
        "buyCost": 105000,
        "sellPrice": 140,
        "upgradeCost": 450000,
        "upgradeName": "CTIII+-",
        "parent": ["CTI+-", "CTII+-"]
    },
    "CTII/-": {
        "name": "Canalisation /-",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 825,
        "yield": 0.2,
        "resistance": Resistance[0],
        "buyCost": 75000,
        "sellPrice": 140,
        "upgradeCost": 250000,
        "upgradeName": "CTIII/-",
        "parent": ["CTI/-", "CTII/-"]
    },
    "CTII--": {
        "name": "Canalisation --",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 600,
        "yield": 0.2,
        "resistance": Resistance[0],
        "buyCost": 45000,
        "sellPrice": 140,
        "upgradeCost": 150000,
        "upgradeName": "CTIII--",
        "parent": ["CTI--", "CTII--"]
    },
    "CTIII++": {
        "name": "Canalisation ++",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1200,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 1375000,
        "sellPrice": 140,
        "upgradeCost": 3300000,
        "upgradeName": "CTIV++",
        "parent": ["CTI++", "CTII++", "CTIII++"]
    },
    "CTIII/+": {
        "name": "Canalisation /+",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 950,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 1000000,
        "sellPrice": 140,
        "upgradeCost": 1500000,
        "upgradeName": "CTIV/+",
        "parent": ["CTI/+", "CTII/+", "CTIII/+"]
    },
    "CTIII+/": {
        "name": "Canalisation +/",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 1200,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 250000,
        "sellPrice": 140,
        "upgradeCost": 1000000,
        "upgradeName": "CTIV+/",
        "parent": ["CTI+/", "CTII+/", "CTIII+/"]
    },
    "CTIII-+": {
        "name": "Canalisation -+",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 700,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 1375000,
        "sellPrice": 140,
        "upgradeCost": 2700000,
        "upgradeName": "CTIV-+",
        "parent": ["CTI-+", "CTII-+", "CTIII-+"]
    },
    "CTIII//": {
        "name": "Canalisation //",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 950,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 150000,
        "sellPrice": 140,
        "upgradeCost": 375000,
        "upgradeName": "CTIV//",
        "parent": ["CTI//", "CTII//", "CTIII//"]
    },
    "CTIII-/": {
        "name": "Canalisation -/",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 700,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 875000,
        "sellPrice": 140,
        "upgradeCost": 1500000,
        "upgradeName": "CTIV-/",
        "parent": ["CTI-/", "CTII-/", "CTIII-/"]
    },
    "CTIII+-": {
        "name": "Canalisation +-",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 1200,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 450000,
        "sellPrice": 140,
        "upgradeCost": 1375000,
        "upgradeName": "CTIV+-",
        "parent": ["CTI+-", "CTII+-", "CTIII+-"]
    },
    "CTIII/-": {
        "name": "Canalisation /-",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 950,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 250000,
        "sellPrice": 140,
        "upgradeCost": 625000,
        "upgradeName": "CTIV/-",
        "parent": ["CTI/-", "CTII/-", "CTIII/-"]
    },
    "CTIII--": {
        "name": "Canalisation --",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 700,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 150000,
        "sellPrice": 140,
        "upgradeCost": 375000,
        "upgradeName": "CTIV--",
        "parent": ["CTI--", "CTII--", "CTIII--"]
    },
    "CTIV++": {
        "name": "Canalisation ++",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 1400,
        "yield": 1,
        "resistance": Resistance[0],
        "buyCost": 3300000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI++", "CTII++", "CTIII++", "CTIV++"]
    },
    "CTIV/+": {
        "name": "Canalisation /+",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 900,
        "yield": 1,
        "resistance": Resistance[0],
        "buyCost": 1500000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI/+", "CTII/+", "CTIII/+", "CTIV/+"]
    },
    "CTIV+/": {
        "name": "Canalisation +/",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1400,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 1000000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI+/", "CTII+/", "CTIII+/", "CTIV+/"]
    },
    "CTIV-+": {
        "name": "Canalisation -+",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 400,
        "yield": 1,
        "resistance": Resistance[0],
        "buyCost": 2700000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI-+", "CTII-+", "CTIII-+", "CTIV-+"]
    },
    "CTIV//": {
        "name": "Canalisation //",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 900,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 375000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI//", "CTII//", "CTIII//", "CTIV//"]
    },
    "CTIV-/": {
        "name": "Canalisation -/",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 400,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 1500000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI-/", "CTII-/", "CTIII-/", "CTIV-/"]
    },
    "CTIV+-": {
        "name": "Canalisation +-",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 1400,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 1375000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI+-", "CTII+-", "CTIII+-", "CTIV+-"]
    },
    "CTIV/-": {
        "name": "Canalisation /-",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 900,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 875000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI/-", "CTII/-", "CTIII/-", "CTIV/-"]
    },
    "CTIV--": {
        "name": "Canalisation --",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 400,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 375000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI--", "CTII--", "CTIII--", "CTIV--"]
    },
    "TTI-+": {
        "name": "Turbine -+",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 62.5,
        "yield": 19.2,
        "resistance": Resistance[0],
        "buyCost": 61500,
        "sellPrice": 140,
        "upgradeCost": 307500,
        "upgradeName": "TTII-+",
        "parent": []
    },
    "TTI/+": {
        "name": "Turbine /+",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 231.25,
        "yield": 5.2,
        "resistance": Resistance[0],
        "buyCost": 60000,
        "sellPrice": 140,
        "upgradeCost": 300000,
        "upgradeName": "TTII/+",
        "parent": []
    },
    "TTI++": {
        "name": "Turbine ++",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 400,
        "yield": 3.0,
        "resistance": Resistance[0],
        "buyCost": 58500,
        "sellPrice": 140,
        "upgradeCost": 292500,
        "upgradeName": "TTII++",
        "parent": []
    },
    "TTI-/": {
        "name": "Turbine -/",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 62.5,
        "yield": 13.6,
        "resistance": Resistance[0],
        "buyCost": 37500,
        "sellPrice": 140,
        "upgradeCost": 187500,
        "upgradeName": "TTII-/",
        "parent": []
    },
    "TTI//": {
        "name": "Turbine //",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 231.25,
        "yield": 3.7,
        "resistance": Resistance[0],
        "buyCost": 37500,
        "sellPrice": 140,
        "upgradeCost": 150000,
        "upgradeName": "TTII//",
        "parent": []
    },
    "TTI+/": {
        "name": "Turbine +/",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 400,
        "yield": 2.1,
        "resistance": Resistance[0],
        "buyCost": 33750,
        "sellPrice": 140,
        "upgradeCost": 135000,
        "upgradeName": "TTII+/",
        "parent": []
    },
    "TTI--": {
        "name": "Turbine --",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 62.5,
        "yield": 8.0,
        "resistance": Resistance[0],
        "buyCost": 30000,
        "sellPrice": 140,
        "upgradeCost": 120000,
        "upgradeName": "TTII--",
        "parent": []
    },
    "TTI/-": {
        "name": "Turbine /-",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 231.25,
        "yield": 2.2,
        "resistance": Resistance[0],
        "buyCost": 18750,
        "sellPrice": 140,
        "upgradeCost": 75000,
        "upgradeName": "TTII/-",
        "parent": []
    },
    "TTI+-": {
        "name": "Turbine +-",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 400,
        "yield": 1.3,
        "resistance": Resistance[0],
        "buyCost": 11250,
        "sellPrice": 140,
        "upgradeCost": 45000,
        "upgradeName": "TTII+-",
        "parent": []
    },
    "TTII-+": {
        "name": "Turbine -+",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 150,
        "yield": 80.0,
        "resistance": Resistance[0],
        "buyCost": 307500,
        "sellPrice": 140,
        "upgradeCost": 1025000,
        "upgradeName": "TTIII-+",
        "parent": ["TTI-+", "TTII-+"]
    },
    "TTII/+": {
        "name": "Turbine /+",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 468.75,
        "yield": 25.6,
        "resistance": Resistance[0],
        "buyCost": 300000,
        "sellPrice": 140,
        "upgradeCost": 1000000,
        "upgradeName": "TTIII/+",
        "parent": ["TTI/+", "TTII/+"]
    },
    "TTII++": {
        "name": "Turbine ++",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 787.5,
        "yield": 15.2,
        "resistance": Resistance[0],
        "buyCost": 292500,
        "sellPrice": 140,
        "upgradeCost": 975000,
        "upgradeName": "TTIII++",
        "parent": ["TTI++", "TTII++"]
    },
    "TTII-/": {
        "name": "Turbine -/",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 150,
        "yield": 56.7,
        "resistance": Resistance[0],
        "buyCost": 187500,
        "sellPrice": 140,
        "upgradeCost": 625000,
        "upgradeName": "TTIII-/",
        "parent": ["TTI-/", "TTII-/"]
    },
    "TTII//": {
        "name": "Turbine //",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 468.75,
        "yield": 18.1,
        "resistance": Resistance[0],
        "buyCost": 150000,
        "sellPrice": 140,
        "upgradeCost": 500000,
        "upgradeName": "TTIII//",
        "parent": ["TTI//", "TTII//"]
    },
    "TTII+/": {
        "name": "Turbine +/",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 787.5,
        "yield": 10.8,
        "resistance": Resistance[0],
        "buyCost": 135000,
        "sellPrice": 140,
        "upgradeCost": 450000,
        "upgradeName": "TTIII+/",
        "parent": ["TTI+/", "TTII+/"]
    },
    "TTII--": {
        "name": "Turbine --",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 150,
        "yield": 33.3,
        "resistance": Resistance[0],
        "buyCost": 120000,
        "sellPrice": 140,
        "upgradeCost": 400000,
        "upgradeName": "TTIII--",
        "parent": ["TTI--", "TTII--"]
    },
    "TTII/-": {
        "name": "Turbine /-",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 468.75,
        "yield": 10.7,
        "resistance": Resistance[0],
        "buyCost": 75000,
        "sellPrice": 140,
        "upgradeCost": 250000,
        "upgradeName": "TTIII/-",
        "parent": ["TTI/-", "TTII/-"]
    },
    "TTII+-": {
        "name": "Turbine +-",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 787.5,
        "yield": 6.3,
        "resistance": Resistance[0],
        "buyCost": 45000,
        "sellPrice": 140,
        "upgradeCost": 150000,
        "upgradeName": "TTIII+-",
        "parent": ["TTI+-", "TTII+-"]
    },
    "TTIII-+": {
        "name": "Turbine -+",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 350,
        "yield": 342.9,
        "resistance": Resistance[0],
        "buyCost": 1025000,
        "sellPrice": 140,
        "upgradeCost": 2460000,
        "upgradeName": "TTIV-+",
        "parent": ["TTI-+", "TTII-+", "TTIII-+"]
    },
    "TTIII/+": {
        "name": "Turbine /+",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 775,
        "yield": 154.8,
        "resistance": Resistance[0],
        "buyCost": 1000000,
        "sellPrice": 140,
        "upgradeCost": 2400000,
        "upgradeName": "TTIV/+",
        "parent": ["TTI/+", "TTII/+", "TTIII/+"]
    },
    "TTIII++": {
        "name": "Turbine ++",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1200,
        "yield": 100.0,
        "resistance": Resistance[0],
        "buyCost": 975000,
        "sellPrice": 140,
        "upgradeCost": 2340000,
        "upgradeName": "TTIV++",
        "parent": ["TTI++", "TTII++", "TTIII++"]
    },
    "TTIII-/": {
        "name": "Turbine -/",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 350,
        "yield": 242.9,
        "resistance": Resistance[0],
        "buyCost": 625000,
        "sellPrice": 140,
        "upgradeCost": 1500000,
        "upgradeName": "TTIV-/",
        "parent": ["TTI-/", "TTII-/", "TTIII-/"]
    },
    "TTIII//": {
        "name": "Turbine //",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 775,
        "yield": 109.7,
        "resistance": Resistance[0],
        "buyCost": 500000,
        "sellPrice": 140,
        "upgradeCost": 1250000,
        "upgradeName": "TTIV//",
        "parent": ["TTI//", "TTII//", "TTIII//"]
    },
    "TTIII+/": {
        "name": "Turbine +/",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 1200,
        "yield": 70.8,
        "resistance": Resistance[0],
        "buyCost": 450000,
        "sellPrice": 140,
        "upgradeCost": 1125000,
        "upgradeName": "TTIV+/",
        "parent": ["TTI+/", "TTII+/", "TTIII+/"]
    },
    "TTIII--": {
        "name": "Turbine --",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 350,
        "yield": 142.9,
        "resistance": Resistance[0],
        "buyCost": 400000,
        "sellPrice": 140,
        "upgradeCost": 1000000,
        "upgradeName": "TTIV--",
        "parent": ["TTI--", "TTII--", "TTIII--"]
    },
    "TTIII/-": {
        "name": "Turbine /-",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 775,
        "yield": 64.5,
        "resistance": Resistance[0],
        "buyCost": 250000,
        "sellPrice": 140,
        "upgradeCost": 625000,
        "upgradeName": "TTIV/-",
        "parent": ["TTI/-", "TTII/-", "TTIII/-"]
    },
    "TTIII+-": {
        "name": "Turbine +-",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 1200,
        "yield": 41.7,
        "resistance": Resistance[0],
        "buyCost": 150000,
        "sellPrice": 140,
        "upgradeCost": 375000,
        "upgradeName": "TTIV+-",
        "parent": ["TTI+-", "TTII+-", "TTIII+-"]
    },
    "TTIV-+": {
        "name": "Turbine -+",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 300,
        "yield": 4000.0,
        "resistance": Resistance[0],
        "buyCost": 2460000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI-+", "TTII-+", "TTIII-+", "TTIV-+"]
    },
    "TTIV/+": {
        "name": "Turbine /+",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 1025,
        "yield": 1170.7,
        "resistance": Resistance[0],
        "buyCost": 2400000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI/+", "TTII/+", "TTIII/+", "TTIV/+"]
    },
    "TTIV++": {
        "name": "Turbine ++",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 1750,
        "yield": 685.7,
        "resistance": Resistance[0],
        "buyCost": 2340000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI++", "TTII++", "TTIII++", "TTIV++"]
    },
    "TTIV-/": {
        "name": "Turbine -/",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 300,
        "yield": 2833.3,
        "resistance": Resistance[0],
        "buyCost": 1500000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI-/", "TTII-/", "TTIII-/", "TTIV-/"]
    },
    "TTIV//": {
        "name": "Turbine //",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1025,
        "yield": 829.3,
        "resistance": Resistance[0],
        "buyCost": 1250000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI//", "TTII//", "TTIII//", "TTIV//"]
    },
    "TTIV+/": {
        "name": "Turbine +/",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1750,
        "yield": 485.7,
        "resistance": Resistance[0],
        "buyCost": 1125000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI+/", "TTII+/", "TTIII+/", "TTIV+/"]
    },
    "TTIV--": {
        "name": "Turbine --",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 300,
        "yield": 1666.7,
        "resistance": Resistance[0],
        "buyCost": 1000000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI--", "TTII--", "TTIII--", "TTIV--"]
    },
    "TTIV/-": {
        "name": "Turbine /-",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1025,
        "yield": 487.8,
        "resistance": Resistance[0],
        "buyCost": 625000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI/-", "TTII/-", "TTIII/-", "TTIV/-"]
    },
    "TTIV+-": {
        "name": "Turbine +-",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1750,
        "yield": 285.7,
        "resistance": Resistance[0],
        "buyCost": 375000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI+-", "TTII+-", "TTIII+-", "TTIV+-"]
    },
    "GTI++": {
        "name": "Générateur ++",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 1200,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 61500,
        "sellPrice": 140,
        "upgradeCost": 307500,
        "upgradeName": "GTII++",
        "parent": []
    },
    "GTI/+": {
        "name": "Générateur /+",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 850,
        "yield": 1.2,
        "resistance": Resistance[0],
        "buyCost": 60000,
        "sellPrice": 140,
        "upgradeCost": 300000,
        "upgradeName": "GTII/+",
        "parent": []
    },
    "GTI-+": {
        "name": "Générateur -+",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 500,
        "yield": 2.0,
        "resistance": Resistance[0],
        "buyCost": 58500,
        "sellPrice": 140,
        "upgradeCost": 292500,
        "upgradeName": "GTII-+",
        "parent": []
    },
    "GTI+/": {
        "name": "Générateur +/",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 1200,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 37500,
        "sellPrice": 140,
        "upgradeCost": 187500,
        "upgradeName": "GTII+/",
        "parent": []
    },
    "GTI//": {
        "name": "Générateur //",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 850,
        "yield": 0.9,
        "resistance": Resistance[0],
        "buyCost": 37500,
        "sellPrice": 140,
        "upgradeCost": 150000,
        "upgradeName": "GTII//",
        "parent": []
    },
    "GTI-/": {
        "name": "Générateur -/",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 500,
        "yield": 1.5,
        "resistance": Resistance[0],
        "buyCost": 33750,
        "sellPrice": 140,
        "upgradeCost": 135000,
        "upgradeName": "GTII-/",
        "parent": []
    },
    "GTI--": {
        "name": "Générateur --",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 500,
        "yield": 1.0,
        "resistance": Resistance[0],
        "buyCost": 30000,
        "sellPrice": 140,
        "upgradeCost": 120000,
        "upgradeName": "GTII--",
        "parent": []
    },
    "GTI/-": {
        "name": "Générateur /-",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 850,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 18750,
        "sellPrice": 140,
        "upgradeCost": 75000,
        "upgradeName": "GTII/-",
        "parent": []
    },
    "GTI+-": {
        "name": "Générateur +-",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 1200,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 11250,
        "sellPrice": 140,
        "upgradeCost": 45000,
        "upgradeName": "GTII+-",
        "parent": []
    },
    "GTII++": {
        "name": "Générateur ++",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 12000,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 307500,
        "sellPrice": 140,
        "upgradeCost": 1025000,
        "upgradeName": "GTIII++",
        "parent": ["GTI++", "GTII++"]
    },
    "GTII/+": {
        "name": "Générateur /+",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 8500,
        "yield": 1.2,
        "resistance": Resistance[0],
        "buyCost": 300000,
        "sellPrice": 140,
        "upgradeCost": 1000000,
        "upgradeName": "GTIII/+",
        "parent": ["GTI/+", "GTII/+"]
    },
    "GTII-+": {
        "name": "Générateur -+",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 5000,
        "yield": 2.0,
        "resistance": Resistance[0],
        "buyCost": 292500,
        "sellPrice": 140,
        "upgradeCost": 975000,
        "upgradeName": "GTIII-+",
        "parent": ["GTI-+", "GTII-+"]
    },
    "GTII+/": {
        "name": "Générateur +/",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 12000,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 187500,
        "sellPrice": 140,
        "upgradeCost": 625000,
        "upgradeName": "GTIII+/",
        "parent": ["GTI+/", "GTII+/"]
    },
    "GTII//": {
        "name": "Générateur //",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 8500,
        "yield": 0.9,
        "resistance": Resistance[0],
        "buyCost": 150000,
        "sellPrice": 140,
        "upgradeCost": 500000,
        "upgradeName": "GTIII//",
        "parent": ["GTI//", "GTII//"]
    },
    "GTII-/": {
        "name": "Générateur -/",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 5000,
        "yield": 1.5,
        "resistance": Resistance[0],
        "buyCost": 135000,
        "sellPrice": 140,
        "upgradeCost": 450000,
        "upgradeName": "GTIII-/",
        "parent": ["GTI-/", "GTII-/"]
    },
    "GTII--": {
        "name": "Générateur --",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 5000,
        "yield": 1.0,
        "resistance": Resistance[0],
        "buyCost": 120000,
        "sellPrice": 140,
        "upgradeCost": 400000,
        "upgradeName": "GTIII--",
        "parent": ["GTI--", "GTII--"]
    },
    "GTII/-": {
        "name": "Générateur /-",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 8500,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 75000,
        "sellPrice": 140,
        "upgradeCost": 250000,
        "upgradeName": "GTIII/-",
        "parent": ["GTI/-", "GTII/-"]
    },
    "GTII+-": {
        "name": "Générateur +-",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 12000,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 45000,
        "sellPrice": 140,
        "upgradeCost": 150000,
        "upgradeName": "GTIII+-",
        "parent": ["GTI+-", "GTII+-"]
    },
    "GTIII++": {
        "name": "Générateur ++",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 120000,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 1025000,
        "sellPrice": 140,
        "upgradeCost": 2460000,
        "upgradeName": "GTIV++",
        "parent": ["GTI++", "GTII++", "GTIII++"]
    },
    "GTIII/+": {
        "name": "Générateur /+",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 85000,
        "yield": 1.2,
        "resistance": Resistance[0],
        "buyCost": 1000000,
        "sellPrice": 140,
        "upgradeCost": 2400000,
        "upgradeName": "GTIV/+",
        "parent": ["GTI/+", "GTII/+", "GTIII/+"]
    },
    "GTIII-+": {
        "name": "Générateur -+",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 50000,
        "yield": 2.0,
        "resistance": Resistance[0],
        "buyCost": 975000,
        "sellPrice": 140,
        "upgradeCost": 2340000,
        "upgradeName": "GTIV-+",
        "parent": ["GTI-+", "GTII-+", "GTIII-+"]
    },
    "GTIII+/": {
        "name": "Générateur +/",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 120000,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 625000,
        "sellPrice": 140,
        "upgradeCost": 1500000,
        "upgradeName": "GTIV+/",
        "parent": ["GTI+/", "GTII+/", "GTIII+/"]
    },
    "GTIII//": {
        "name": "Générateur //",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 85000,
        "yield": 0.9,
        "resistance": Resistance[0],
        "buyCost": 500000,
        "sellPrice": 140,
        "upgradeCost": 1250000,
        "upgradeName": "GTIV//",
        "parent": ["GTI//", "GTII//", "GTIII//"]
    },
    "GTIII-/": {
        "name": "Générateur -/",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 50000,
        "yield": 1.5,
        "resistance": Resistance[0],
        "buyCost": 450000,
        "sellPrice": 140,
        "upgradeCost": 1125000,
        "upgradeName": "GTIV-/",
        "parent": ["GTI-/", "GTII-/", "GTIII-/"]
    },
    "GTIII--": {
        "name": "Générateur --",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 50000,
        "yield": 1.0,
        "resistance": Resistance[0],
        "buyCost": 400000,
        "sellPrice": 140,
        "upgradeCost": 1000000,
        "upgradeName": "GTIV--",
        "parent": ["GTI--", "GTII--", "GTIII--"]
    },
    "GTIII/-": {
        "name": "Générateur /-",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 85000,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 250000,
        "sellPrice": 140,
        "upgradeCost": 625000,
        "upgradeName": "GTIV/-",
        "parent": ["GTI/-", "GTII/-", "GTIII/-"]
    },
    "GTIII+-": {
        "name": "Générateur +-",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 120000,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 150000,
        "sellPrice": 140,
        "upgradeCost": 375000,
        "upgradeName": "GTIV+-",
        "parent": ["GTI+-", "GTII+-", "GTIII+-"]
    },
    "GTIV++": {
        "name": "Générateur ++",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 1200000,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 2460000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI++", "GTII++", "GTIII++", "GTIV++"]
    },
    "GTIV/+": {
        "name": "Générateur /+",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 850000,
        "yield": 1.2,
        "resistance": Resistance[0],
        "buyCost": 2400000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI/+", "GTII/+", "GTIII/+", "GTIV/+"]
    },
    "GTIV-+": {
        "name": "Générateur -+",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 500000,
        "yield": 2.0,
        "resistance": Resistance[0],
        "buyCost": 2340000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI-+", "GTII-+", "GTIII-+", "GTIV-+"]
    },
    "GTIV+/": {
        "name": "Générateur +/",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 1200000,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 1500000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI+/", "GTII+/", "GTIII+/", "GTIV+/"]
    },
    "GTIV//": {
        "name": "Générateur //",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 850000,
        "yield": 0.9,
        "resistance": Resistance[0],
        "buyCost": 1250000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI//", "GTII//", "GTIII//", "GTIV//"]
    },
    "GTIV-/": {
        "name": "Générateur -/",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 500000,
        "yield": 1.5,
        "resistance": Resistance[0],
        "buyCost": 1125000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI-/", "GTII-/", "GTIII-/", "GTIV-/"]
    },
    "GTIV--": {
        "name": "Générateur --",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 500000,
        "yield": 1.0,
        "resistance": Resistance[0],
        "buyCost": 1000000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI--", "GTII--", "GTIII--", "GTIV--"]
    },
    "GTIV/-": {
        "name": "Générateur /-",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 850000,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 625000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI/-", "GTII/-", "GTIII/-", "GTIV/-"]
    },
    "GTIV+-": {
        "name": "Générateur +-",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1200000,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 375000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI+-", "GTII+-", "GTIII+-", "GTIV+-"]
    },     
  }

Modules = {
    "CTI++": {
        "name": "Canalisation ++",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 800,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "CTII++",
        "parent": []
    },
    "CTI/+": {
        "name": "Canalisation /+",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 650,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "CTII/+",
        "parent": []
    },
    "CTI+/": {
        "name": "Canalisation +/",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 800,
        "yield": 0.25,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "CTII+/",
        "parent": []
    },
    "CTI-+": {
        "name": "Canalisation -+",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 500,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "CTII-+",
        "parent": []
    },
    "CTI//": {
        "name": "Canalisation //",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 650,
        "yield": 0.25,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "CTII//",
        "parent": []
    },
    "CTI-/": {
        "name": "Canalisation -/",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 500,
        "yield": 0.25,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "CTII-/",
        "parent": []
    },
    "CTI+-": {
        "name": "Canalisation +-",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 800,
        "yield": 0.1,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "CTII+-",
        "parent": []
    },
    "CTI/-": {
        "name": "Canalisation /-",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 650,
        "yield": 0.1,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "CTII/-",
        "parent": []
    },
    "CTI--": {
        "name": "Canalisation --",
        "section": Sections[0],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 500,
        "yield": 0.1,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "CTII--",
        "parent": []
    },
    "CTII++": {
        "name": "Canalisation ++",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 1050,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "CTIII++",
        "parent": ["CTI++", "CTII++"]
    },
    "CTII/+": {
        "name": "Canalisation /+",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 825,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "CTIII/+",
        "parent": ["CTI/+", "CTII/+"]
    },
    "CTII+/": {
        "name": "Canalisation +/",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 1050,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "CTIII+/",
        "parent": ["CTI+/", "CTII+/"]
    },
    "CTII-+": {
        "name": "Canalisation -+",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 600,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "CTIII-+",
        "parent": ["CTI-+", "CTII-+"]
    },
    "CTII//": {
        "name": "Canalisation //",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 825,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "CTIII//",
        "parent": ["CTI//", "CTII//"]
    },
    "CTII-/": {
        "name": "Canalisation -/",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 600,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "CTIII-/",
        "parent": ["CTI-/", "CTII-/"]
    },
    "CTII+-": {
        "name": "Canalisation +-",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 1050,
        "yield": 0.2,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "CTIII+-",
        "parent": ["CTI+-", "CTII+-"]
    },
    "CTII/-": {
        "name": "Canalisation /-",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 825,
        "yield": 0.2,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "CTIII/-",
        "parent": ["CTI/-", "CTII/-"]
    },
    "CTII--": {
        "name": "Canalisation --",
        "section": Sections[0],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 600,
        "yield": 0.2,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "CTIII--",
        "parent": ["CTI--", "CTII--"]
    },
    "CTIII++": {
        "name": "Canalisation ++",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1200,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "CTIV++",
        "parent": ["CTI++", "CTII++", "CTIII++"]
    },
    "CTIII/+": {
        "name": "Canalisation /+",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 950,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "CTIV/+",
        "parent": ["CTI/+", "CTII/+", "CTIII/+"]
    },
    "CTIII+/": {
        "name": "Canalisation +/",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 1200,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "CTIV+/",
        "parent": ["CTI+/", "CTII+/", "CTIII+/"]
    },
    "CTIII-+": {
        "name": "Canalisation -+",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 700,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "CTIV-+",
        "parent": ["CTI-+", "CTII-+", "CTIII-+"]
    },
    "CTIII//": {
        "name": "Canalisation //",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 950,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "CTIV//",
        "parent": ["CTI//", "CTII//", "CTIII//"]
    },
    "CTIII-/": {
        "name": "Canalisation -/",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 700,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "CTIV-/",
        "parent": ["CTI-/", "CTII-/", "CTIII-/"]
    },
    "CTIII+-": {
        "name": "Canalisation +-",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 1200,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "CTIV+-",
        "parent": ["CTI+-", "CTII+-", "CTIII+-"]
    },
    "CTIII/-": {
        "name": "Canalisation /-",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 950,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "CTIV/-",
        "parent": ["CTI/-", "CTII/-", "CTIII/-"]
    },
    "CTIII--": {
        "name": "Canalisation --",
        "section": Sections[0],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 700,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "CTIV--",
        "parent": ["CTI--", "CTII--", "CTIII--"]
    },
    "CTIV++": {
        "name": "Canalisation ++",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 1400,
        "yield": 1,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI++", "CTII++", "CTIII++", "CTIV++"]
    },
    "CTIV/+": {
        "name": "Canalisation /+",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 900,
        "yield": 1,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI/+", "CTII/+", "CTIII/+", "CTIV/+"]
    },
    "CTIV+/": {
        "name": "Canalisation +/",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1400,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI+/", "CTII+/", "CTIII+/", "CTIV+/"]
    },
    "CTIV-+": {
        "name": "Canalisation -+",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 400,
        "yield": 1,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI-+", "CTII-+", "CTIII-+", "CTIV-+"]
    },
    "CTIV//": {
        "name": "Canalisation //",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 900,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI//", "CTII//", "CTIII//", "CTIV//"]
    },
    "CTIV-/": {
        "name": "Canalisation -/",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 400,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI-/", "CTII-/", "CTIII-/", "CTIV-/"]
    },
    "CTIV+-": {
        "name": "Canalisation +-",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 1400,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI+-", "CTII+-", "CTIII+-", "CTIV+-"]
    },
    "CTIV/-": {
        "name": "Canalisation /-",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 900,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI/-", "CTII/-", "CTIII/-", "CTIV/-"]
    },
    "CTIV--": {
        "name": "Canalisation --",
        "section": Sections[0],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 400,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["CTI--", "CTII--", "CTIII--", "CTIV--"]
    },
    "TTI-+": {
        "name": "Turbine -+",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 62.5,
        "yield": 19.2,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "TTII-+",
        "parent": []
    },
    "TTI/+": {
        "name": "Turbine /+",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 231.25,
        "yield": 5.2,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "TTII/+",
        "parent": []
    },
    "TTI++": {
        "name": "Turbine ++",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 400,
        "yield": 3.0,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "TTII++",
        "parent": []
    },
    "TTI-/": {
        "name": "Turbine -/",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 62.5,
        "yield": 13.6,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "TTII-/",
        "parent": []
    },
    "TTI//": {
        "name": "Turbine //",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 231.25,
        "yield": 3.7,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "TTII//",
        "parent": []
    },
    "TTI+/": {
        "name": "Turbine +/",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 400,
        "yield": 2.1,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "TTII+/",
        "parent": []
    },
    "TTI--": {
        "name": "Turbine --",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 62.5,
        "yield": 8.0,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "TTII--",
        "parent": []
    },
    "TTI/-": {
        "name": "Turbine /-",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 231.25,
        "yield": 2.2,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "TTII/-",
        "parent": []
    },
    "TTI+-": {
        "name": "Turbine +-",
        "section": Sections[1],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 400,
        "yield": 1.3,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "TTII+-",
        "parent": []
    },
    "TTII-+": {
        "name": "Turbine -+",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 150,
        "yield": 80.0,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "TTIII-+",
        "parent": ["TTI-+", "TTII-+"]
    },
    "TTII/+": {
        "name": "Turbine /+",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 468.75,
        "yield": 25.6,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "TTIII/+",
        "parent": ["TTI/+", "TTII/+"]
    },
    "TTII++": {
        "name": "Turbine ++",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 787.5,
        "yield": 15.2,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "TTIII++",
        "parent": ["TTI++", "TTII++"]
    },
    "TTII-/": {
        "name": "Turbine -/",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 150,
        "yield": 56.7,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "TTIII-/",
        "parent": ["TTI-/", "TTII-/"]
    },
    "TTII//": {
        "name": "Turbine //",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 468.75,
        "yield": 18.1,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "TTIII//",
        "parent": ["TTI//", "TTII//"]
    },
    "TTII+/": {
        "name": "Turbine +/",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 787.5,
        "yield": 10.8,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "TTIII+/",
        "parent": ["TTI+/", "TTII+/"]
    },
    "TTII--": {
        "name": "Turbine --",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 150,
        "yield": 33.3,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "TTIII--",
        "parent": ["TTI--", "TTII--"]
    },
    "TTII/-": {
        "name": "Turbine /-",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 468.75,
        "yield": 10.7,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "TTIII/-",
        "parent": ["TTI/-", "TTII/-"]
    },
    "TTII+-": {
        "name": "Turbine +-",
        "section": Sections[1],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 787.5,
        "yield": 6.3,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "TTIII+-",
        "parent": ["TTI+-", "TTII+-"]
    },
    "TTIII-+": {
        "name": "Turbine -+",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 350,
        "yield": 342.9,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "TTIV-+",
        "parent": ["TTI-+", "TTII-+", "TTIII-+"]
    },
    "TTIII/+": {
        "name": "Turbine /+",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 775,
        "yield": 154.8,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "TTIV/+",
        "parent": ["TTI/+", "TTII/+", "TTIII/+"]
    },
    "TTIII++": {
        "name": "Turbine ++",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1200,
        "yield": 100.0,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "TTIV++",
        "parent": ["TTI++", "TTII++", "TTIII++"]
    },
    "TTIII-/": {
        "name": "Turbine -/",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 350,
        "yield": 242.9,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "TTIV-/",
        "parent": ["TTI-/", "TTII-/", "TTIII-/"]
    },
    "TTIII//": {
        "name": "Turbine //",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 775,
        "yield": 109.7,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "TTIV//",
        "parent": ["TTI//", "TTII//", "TTIII//"]
    },
    "TTIII+/": {
        "name": "Turbine +/",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 1200,
        "yield": 70.8,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "TTIV+/",
        "parent": ["TTI+/", "TTII+/", "TTIII+/"]
    },
    "TTIII--": {
        "name": "Turbine --",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 350,
        "yield": 142.9,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "TTIV--",
        "parent": ["TTI--", "TTII--", "TTIII--"]
    },
    "TTIII/-": {
        "name": "Turbine /-",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 775,
        "yield": 64.5,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "TTIV/-",
        "parent": ["TTI/-", "TTII/-", "TTIII/-"]
    },
    "TTIII+-": {
        "name": "Turbine +-",
        "section": Sections[1],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 1200,
        "yield": 41.7,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "TTIV+-",
        "parent": ["TTI+-", "TTII+-", "TTIII+-"]
    },
    "TTIV-+": {
        "name": "Turbine -+",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 300,
        "yield": 4000.0,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI-+", "TTII-+", "TTIII-+", "TTIV-+"]
    },
    "TTIV/+": {
        "name": "Turbine /+",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 1025,
        "yield": 1170.7,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI/+", "TTII/+", "TTIII/+", "TTIV/+"]
    },
    "TTIV++": {
        "name": "Turbine ++",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 1750,
        "yield": 685.7,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI++", "TTII++", "TTIII++", "TTIV++"]
    },
    "TTIV-/": {
        "name": "Turbine -/",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 300,
        "yield": 2833.3,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI-/", "TTII-/", "TTIII-/", "TTIV-/"]
    },
    "TTIV//": {
        "name": "Turbine //",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1025,
        "yield": 829.3,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI//", "TTII//", "TTIII//", "TTIV//"]
    },
    "TTIV+/": {
        "name": "Turbine +/",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1750,
        "yield": 485.7,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI+/", "TTII+/", "TTIII+/", "TTIV+/"]
    },
    "TTIV--": {
        "name": "Turbine --",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 300,
        "yield": 1666.7,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI--", "TTII--", "TTIII--", "TTIV--"]
    },
    "TTIV/-": {
        "name": "Turbine /-",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1025,
        "yield": 487.8,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI/-", "TTII/-", "TTIII/-", "TTIV/-"]
    },
    "TTIV+-": {
        "name": "Turbine +-",
        "section": Sections[1],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1750,
        "yield": 285.7,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["TTI+-", "TTII+-", "TTIII+-", "TTIV+-"]
    },
    "GTI++": {
        "name": "Générateur ++",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 1200,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "GTII++",
        "parent": []
    },
    "GTI/+": {
        "name": "Générateur /+",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 850,
        "yield": 1.2,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "GTII/+",
        "parent": []
    },
    "GTI-+": {
        "name": "Générateur -+",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 500,
        "yield": 2.0,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "GTII-+",
        "parent": []
    },
    "GTI+/": {
        "name": "Générateur +/",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[2],
        #Passive
        "maximumInput": 1200,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "GTII+/",
        "parent": []
    },
    "GTI//": {
        "name": "Générateur //",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 850,
        "yield": 0.9,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "GTII//",
        "parent": []
    },
    "GTI-/": {
        "name": "Générateur -/",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 500,
        "yield": 1.5,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "GTII-/",
        "parent": []
    },
    "GTI--": {
        "name": "Générateur --",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 500,
        "yield": 1.0,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "GTII--",
        "parent": []
    },
    "GTI/-": {
        "name": "Générateur /-",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 850,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "GTII/-",
        "parent": []
    },
    "GTI+-": {
        "name": "Générateur +-",
        "section": Sections[2],
        "tier": Tier[0],
        "cityLevel": CityLevel[1],
        #Passive
        "maximumInput": 1200,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 38000,
        "sellPrice": 140,
        "upgradeCost": 180000,
        "upgradeName": "GTII+-",
        "parent": []
    },
    "GTII++": {
        "name": "Générateur ++",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 12000,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "GTIII++",
        "parent": ["GTI++", "GTII++"]
    },
    "GTII/+": {
        "name": "Générateur /+",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 8500,
        "yield": 1.2,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "GTIII/+",
        "parent": ["GTI/+", "GTII/+"]
    },
    "GTII-+": {
        "name": "Générateur -+",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 5000,
        "yield": 2.0,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "GTIII-+",
        "parent": ["GTI-+", "GTII-+"]
    },
    "GTII+/": {
        "name": "Générateur +/",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[4],
        #Passive
        "maximumInput": 12000,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "GTIII+/",
        "parent": ["GTI+/", "GTII+/"]
    },
    "GTII//": {
        "name": "Générateur //",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 8500,
        "yield": 0.9,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "GTIII//",
        "parent": ["GTI//", "GTII//"]
    },
    "GTII-/": {
        "name": "Générateur -/",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 5000,
        "yield": 1.5,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "GTIII-/",
        "parent": ["GTI-/", "GTII-/"]
    },
    "GTII--": {
        "name": "Générateur --",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 5000,
        "yield": 1.0,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "GTIII--",
        "parent": ["GTI--", "GTII--"]
    },
    "GTII/-": {
        "name": "Générateur /-",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 8500,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "GTIII/-",
        "parent": ["GTI/-", "GTII/-"]
    },
    "GTII+-": {
        "name": "Générateur +-",
        "section": Sections[2],
        "tier": Tier[1],
        "cityLevel": CityLevel[3],
        #Passive
        "maximumInput": 12000,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 180000,
        "sellPrice": 140,
        "upgradeCost": 652000,
        "upgradeName": "GTIII+-",
        "parent": ["GTI+-", "GTII+-"]
    },
    "GTIII++": {
        "name": "Générateur ++",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 120000,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "GTIV++",
        "parent": ["GTI++", "GTII++", "GTIII++"]
    },
    "GTIII/+": {
        "name": "Générateur /+",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 85000,
        "yield": 1.2,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "GTIV/+",
        "parent": ["GTI/+", "GTII/+", "GTIII/+"]
    },
    "GTIII-+": {
        "name": "Générateur -+",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 50000,
        "yield": 2.0,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "GTIV-+",
        "parent": ["GTI-+", "GTII-+", "GTIII-+"]
    },
    "GTIII+/": {
        "name": "Générateur +/",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 120000,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "GTIV+/",
        "parent": ["GTI+/", "GTII+/", "GTIII+/"]
    },
    "GTIII//": {
        "name": "Générateur //",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 85000,
        "yield": 0.9,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "GTIV//",
        "parent": ["GTI//", "GTII//", "GTIII//"]
    },
    "GTIII-/": {
        "name": "Générateur -/",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 50000,
        "yield": 1.5,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "GTIV-/",
        "parent": ["GTI-/", "GTII-/", "GTIII-/"]
    },
    "GTIII--": {
        "name": "Générateur --",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 50000,
        "yield": 1.0,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "GTIV--",
        "parent": ["GTI--", "GTII--", "GTIII--"]
    },
    "GTIII/-": {
        "name": "Générateur /-",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 85000,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "GTIV/-",
        "parent": ["GTI/-", "GTII/-", "GTIII/-"]
    },
    "GTIII+-": {
        "name": "Générateur +-",
        "section": Sections[2],
        "tier": Tier[2],
        "cityLevel": CityLevel[5],
        #Passive
        "maximumInput": 120000,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 652000,
        "sellPrice": 140,
        "upgradeCost": 1440000,
        "upgradeName": "GTIV+-",
        "parent": ["GTI+-", "GTII+-", "GTIII+-"]
    },
    "GTIV++": {
        "name": "Générateur ++",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 1200000,
        "yield": 0.8,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI++", "GTII++", "GTIII++", "GTIV++"]
    },
    "GTIV/+": {
        "name": "Générateur /+",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 850000,
        "yield": 1.2,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI/+", "GTII/+", "GTIII/+", "GTIV/+"]
    },
    "GTIV-+": {
        "name": "Générateur -+",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 500000,
        "yield": 2.0,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI-+", "GTII-+", "GTIII-+", "GTIV-+"]
    },
    "GTIV+/": {
        "name": "Générateur +/",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[7],
        #Passive
        "maximumInput": 1200000,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI+/", "GTII+/", "GTIII+/", "GTIV+/"]
    },
    "GTIV//": {
        "name": "Générateur //",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 850000,
        "yield": 0.9,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI//", "GTII//", "GTIII//", "GTIV//"]
    },
    "GTIV-/": {
        "name": "Générateur -/",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 500000,
        "yield": 1.5,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI-/", "GTII-/", "GTIII-/", "GTIV-/"]
    },
    "GTIV--": {
        "name": "Générateur --",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 500000,
        "yield": 1.0,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI--", "GTII--", "GTIII--", "GTIV--"]
    },
    "GTIV/-": {
        "name": "Générateur /-",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 850000,
        "yield": 0.6,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI/-", "GTII/-", "GTIII/-", "GTIV/-"]
    },
    "GTIV+-": {
        "name": "Générateur +-",
        "section": Sections[2],
        "tier": Tier[3],
        "cityLevel": CityLevel[6],
        #Passive
        "maximumInput": 1200000,
        "yield": 0.4,
        "resistance": Resistance[0],
        "buyCost": 1440000,
        "sellPrice": 140,
        "upgradeCost": 0,
        "upgradeName": "",
        "parent": ["GTI+-", "GTII+-", "GTIII+-", "GTIV+-"]
    },
    }
