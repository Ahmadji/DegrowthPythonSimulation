import simulation_functions as sf
from visualization import show_graphs

import json

# ═══════════════════════════════════════════════════════════════════════════════
#  ÉTAT INTERNE DU JOUEUR
# ═══════════════════════════════════════════════════════════════════════════════

sf.PlayerBehaviorIndex    = 2 # 0 = Random | 1 = Yield Opti | 2 = Electricity Opti | 3 = Water Opti
sf.PlayerPriceTolerance   = 0.9 # If the player possesses PriceTolerance% of the price for a module, they will eco for it. 


# ═══════════════════════════════════════════════════════════════════════════════
#  PARAMÈTRES DU BARRAGE
# ═══════════════════════════════════════════════════════════════════════════════

sf.Dam = [["CTI//", ""],
          ["TTI//", ""],
          ["GTI//", ""]]

sf.CurrentElectricity = 10   # Valeur initiale ; recalculée à chaque tick par UpdateDam()

sf.SpotPrices      = [30000, 60000, 150000, 200000, 500000, 1200000, 2000000, 6000000]
sf.SpotCityLevels  = [2, 3, 4, 5, 6, 7, 8, 9]

sf.BoostElectricityOutput = 1   # Multiplie la production électrique du barrage
sf.BoostWaterConsumption  = 1   # Multiplie la consommation en eau du barrage


# ═══════════════════════════════════════════════════════════════════════════════
#  PARAMÈTRES DU JEU
# ═══════════════════════════════════════════════════════════════════════════════

sf.IsWaterPoolInfinite           = False
sf.WaterSupply                   = 1_000_000
sf.MaxWaterSupply                = 1_000_000
sf.WaterRegen                    = 5_000
sf.WaterBalance                  = 0     # Bilan eau : WaterRegen - consommation canalisations
sf.AuthorizedDifferenceWithNeeds = 0.2   # Tolérance électricité vs besoins
sf.RequiredCityLevelToWin        = 8


# ═══════════════════════════════════════════════════════════════════════════════
#  PARAMÈTRES DE LA VILLE
# ═══════════════════════════════════════════════════════════════════════════════

sf.CurrentCityLevel = 1
sf.CityLevels = {
    1:  {"NextLevelElectricity":     1_350, "GoldGeneration":       750, "ResearchSpeed":  10},
    2:  {"NextLevelElectricity":     2_025, "GoldGeneration":     1_500, "ResearchSpeed":  20},
    3:  {"NextLevelElectricity":    27_000, "GoldGeneration":     3_000, "ResearchSpeed":  30},
    4:  {"NextLevelElectricity":    39_375, "GoldGeneration":     7_500, "ResearchSpeed":  40},
    5:  {"NextLevelElectricity":   405_000, "GoldGeneration":    10_000, "ResearchSpeed":  50},
    6:  {"NextLevelElectricity": 3_307_500, "GoldGeneration":    25_000, "ResearchSpeed":  60},
    7:  {"NextLevelElectricity": 5_400_000, "GoldGeneration":    60_000, "ResearchSpeed":  70},
    8:  {"NextLevelElectricity": 6_075_000, "GoldGeneration":   100_000, "ResearchSpeed":  80},
    9:  {"NextLevelElectricity": 9_000_000, "GoldGeneration":   300_000, "ResearchSpeed": 100},
    10: {"NextLevelElectricity":         0, "GoldGeneration": 15_000_000, "ResearchSpeed": 150},
}

sf.CurrentNeeds     = 0       # Besoins initiaux
sf.TargetNeeds      = 30_000_000
sf.TargetTime       = 2_400   # Temps cible en secondes
sf.SpeedCoeffA      = 1.2
sf.SpeedCoeffB      = 0.9

sf.GoldUpdateRate   = 1       # Fréquence de mise à jour de l'or (en secondes)
sf.CityUpdateRate   = 1       # Fréquence de mise à jour des besoins (en secondes)
sf.CurrentGold      = 0


# ═══════════════════════════════════════════════════════════════════════════════
#  PARAMÈTRES DE RECHERCHE
# ═══════════════════════════════════════════════════════════════════════════════

sf.progressBar       = 0
sf.distance          = 100
sf.speed             = 1
sf.priceInvest       = 1_000_000_000_000

sf.searchCounter      = 0
sf.totalSearchCounter = 0
sf.nbSearchProposed   = 3
sf.dropRate           = [0.8, 0.15, 0.05]   # Probabilités : Px, Px-1, Px-2
sf.speedCityLevel     = [1, 2, 3, 4]         # Vitesse de recherche par niveau de ville
sf.eachPriceInvest    = [1000, 1200, 1600, 2200, 4000, 7600, 13000]


# ═══════════════════════════════════════════════════════════════════════════════
#  PARAMÈTRES DE SIMULATION
# ═══════════════════════════════════════════════════════════════════════════════

sf.SimulationDuration    = 40   # Durée de la simulation en minutes
sf.GameStates            = ["Running", "Defeat, no water", "Defeat, not enough electricity", "Won"]
sf.CurrentGameState      = "Running"


# ═══════════════════════════════════════════════════════════════════════════════
#  PARAMÈTRES DES GRAPHES
# ═══════════════════════════════════════════════════════════════════════════════

show_electricity_need_city = False
show_water                 = False
show_search                = False
show_game_phases           = False


# ═══════════════════════════════════════════════════════════════════════════════
#  LANCEMENT DE LA SIMULATION
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    simulation_data = sf.run()

    with open('data.json', 'w') as f:
        json.dump(simulation_data, f, indent=4)

    show_graphs(
        simulation_data,
        showElectricityNeedCityGraphs = show_electricity_need_city,
        showWaterGraphs               = show_water,
        showSearchGraph               = show_search,
        showGamePhasesGraph           = show_game_phases,
    )