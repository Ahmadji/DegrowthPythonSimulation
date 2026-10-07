import random
import numpy as np
from modules_data import (
    Sections, Type, Tier, Resistance, CityLevel,
    AllModules, Modules
)

# ═══════════════════════════════════════════════════════════════════════════════
#  ÉTAT INTERNE DU JOUEUR
# ═══════════════════════════════════════════════════════════════════════════════

PlayerAction           = ""   # Mis à jour à chaque tick par SelectRandomActions()
PlayerBehaviors        = ["Random", "Yield Optimization", "Electricity Optimization", "Water Optimization"]
DesiredBuyModule       = None
DesiredUpgradeLocation = []
IsPlayerSaving         = False
PlayerChoice           = 0

PlayerBehaviorIndex    = 1
PlayerPriceTolerance   = 1 #If the player possesses PriceTolerance% of the price for a module, they will eco for it. 


# ═══════════════════════════════════════════════════════════════════════════════
#  PARAMÈTRES DU BARRAGE
# ═══════════════════════════════════════════════════════════════════════════════

CurrentElectricity   = 10        # Valeur initiale ; calculée dynamiquement par UpdateDam()
Dam                  = [["CTI//", ""], ["TTI//", ""], ["GTI//", ""]]
InitialSectionLength = 2         # Recalculé automatiquement au lancement de run()
SpotPrices           = [30000, 60000, 150000, 200000, 500000, 1200000, 2000000, 6000000]
SpotCityLevels       = [2, 3, 4, 5, 6, 7, 8, 9]
BoostElectricityOutput = 1       # Multiplicateur de production électrique
BoostWaterConsumption  = 1       # Multiplicateur de consommation en eau


# ═══════════════════════════════════════════════════════════════════════════════
#  PARAMÈTRES DU JEU
# ═══════════════════════════════════════════════════════════════════════════════

IsWaterPoolInfinite           = False
WaterSupply                   = 1_000_000
MaxWaterSupply                = 1_000_000
WaterRegen                    = 5_000
WaterBalance                  = 0    # Bilan eau : WaterRegen - consommation canalisations
AuthorizedDifferenceWithNeeds = 0.2  # L'électricité doit rester > Besoins * (1 - cette valeur)
RequiredCityLevelToWin        = 8


# ═══════════════════════════════════════════════════════════════════════════════
#  PARAMÈTRES DE LA VILLE
# ═══════════════════════════════════════════════════════════════════════════════

CurrentCityLevel = 1
CityLevels = {
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

CityUpdateRate = 1       # Fréquence de mise à jour des besoins (en secondes)
CurrentNeeds   = 0       # Besoins initiaux (0 = départ dynamique)
TargetNeeds    = 30_000_000
TargetTime     = 2_400   # Temps cible en secondes
SpeedCoeffA    = 1.2
SpeedCoeffB    = 0.9

GoldUpdateRate = 1       # Fréquence de mise à jour de l'or (en secondes)
CurrentGold    = 0


# ═══════════════════════════════════════════════════════════════════════════════
#  PARAMÈTRES DE RECHERCHE
# ═══════════════════════════════════════════════════════════════════════════════

progressBar        = 0
distance           = 0
speed              = 1
priceInvest        = 0

searchCounter      = 0
totalSearchCounter = 0
nbSearchProposed   = 3
dropRate           = []     # Probabilités : Px, Px-1, Px-2
speedCityLevel     = []     # Vitesse de recherche par niveau de ville
eachPriceInvest    = []     # Prix selon le nb total de recherches


# ═══════════════════════════════════════════════════════════════════════════════
#  PARAMÈTRES DE SIMULATION
# ═══════════════════════════════════════════════════════════════════════════════

SimulationDuration    = 40    # Durée en minutes
NumberOfPossibilities = 5     # Nombre de possibilités d'action du joueur
GameStates            = ["Running", "Defeat, no water", "Defeat, not enough electricity", "Won"]
CurrentGameState      = "Running"

# Compteurs internes — réinitialisés automatiquement par run()
UpdateNeedsCounter = 0
UpdateGoldCounter  = 0


# ═══════════════════════════════════════════════════════════════════════════════
#  ÉTAT INTERNE — phases de jeu & niveaux ville (géré par run())
# ═══════════════════════════════════════════════════════════════════════════════

# NOTE: AllModules et Modules sont importés depuis modules_data.py.

GamePhases          = ["Nothing", "Playing"]  # Les deux états de jeu possibles
CurrentGamePhase    = GamePhases[1]
GamePhasesTimes     = [0]   # Horodatages des changements de phase
GamePhasesDurations = []

CityLevelsTimes     = [0]   # Horodatages des montées de niveau
CityLevelsDurations = []
NextCityLevel       = 2     # Recalculé au lancement de run()


"""PLAYER BEHAVIOR"""
# Will pick a random possibility -> for each possibility, is linked an action
def SelectRandomActions(Possibilities, BuyableModules, BuyableSpots, UpgradableModules, UnlockableModule, InvestSearch, SoldableModules, CurrentGold : float, PlayerAction):
    #Check possibilities
    PlayerAction = "Nothing"

    #Player random choice
    hasMadeAChoice = False
    while (not hasMadeAChoice):
        if(1 in Possibilities):
            PlayerChoice = random.randint(0, len(Possibilities) - 1)
            if(Possibilities[PlayerChoice] == 1): 
                match PlayerChoice:
                    case 0:
                        CurrentGold = PlaceModule(BuyableModules[random.randint(0, len(BuyableModules) - 1)], CurrentGold)
                        PlayerAction = "Placed a module"
                        hasMadeAChoice = True
                    case 1:
                        CurrentGold = BuySpot(BuyableSpots[random.randint(0, len(BuyableSpots) - 1)], CurrentGold)
                        PlayerAction = "Bought a spot"
                        hasMadeAChoice = True
                    case 2:
                        CurrentGold = UpgradeModule(UpgradableModules[random.randint(0, len(UpgradableModules) - 1)], CurrentGold)
                        PlayerAction = "Upgraded a module"
                        hasMadeAChoice = True
                    case 3:
                        UnlockModule()
                        PlayerAction = "Unlock module"
                        hasMadeAChoice = True
                    case 4:
                        investSearch()
                        PlayerAction = "Invest Search"
                        hasMadeAChoice = True 
                    case 5:
                        #Select a random location
                        Locations = []
                        for location in SoldableModules:
                            Locations.append(location)
                        RandomLocation = random.choice(Locations)

                        # Sell current module and buy better module
                        SellModule(RandomLocation, CurrentGold)

                        # Buy a better module
                        PlaceModule(random.choice(SoldableModules[RandomLocation]),CurrentGold)
                        
                        PlayerAction = "Sold and bought a better module"
                        hasMadeAChoice = True
        else:
            hasMadeAChoice = True


    return CurrentGold, PlayerAction
    
def SelectOptimizedActions(Possibilities, BuyableModules, BuyableSpots, UpgradableModules, UnlockableModule, InvestSearch, SoldableModules, CurrentGold : float, PlayerAction, PlayerChoice, IsPlayerSaving, DesiredBuyModule, DesiredUpgradeLocation):
    #Check possibilities
    PlayerAction = "Nothing"

    #Player random choice
    hasMadeAChoice = False
    while (not hasMadeAChoice):
        if(1 in Possibilities):
            if(not IsPlayerSaving):
                PlayerChoice = random.randint(0, len(Possibilities) - 1)
            if(Possibilities[PlayerChoice] == 1): 
                match PlayerChoice:
                    case 0: #Buy module
                        # Checks if there is a Desired Buy Module
                        if(DesiredBuyModule is None):
                            DesiredBuyModule = BuyableModules[random.randint(0, len(BuyableModules) - 1)]
                            print(DesiredBuyModule)
                        else:
                            if (Modules[DesiredBuyModule]["buyCost"] > CurrentGold):
                                PlayerAction = f"Saved to buy {DesiredBuyModule} | Gold remaining : {Modules[DesiredBuyModule]["buyCost"] - CurrentGold}"
                                IsPlayerSaving = True
                                hasMadeAChoice = True
                            else:
                                CurrentGold = PlaceModule(DesiredBuyModule, CurrentGold)
                                PlayerAction = f"Placed the module {DesiredBuyModule}"
                                IsPlayerSaving = False
                                DesiredBuyModule = None
                                hasMadeAChoice = True
                    case 1: #Buy spot
                        Section = BuyableSpots[random.randint(0, len(BuyableSpots) - 1)]
                        CurrentGold = BuySpot(Section, CurrentGold)
                        PlayerAction = f"Bought a spot in the {Section} section"
                        hasMadeAChoice = True
                    case 2: #Upgrade module
                        # Checks if there is an Upgrade Location
                        if(DesiredUpgradeLocation == []):
                            DesiredUpgradeLocation = UpgradableModules[random.randint(0, len(UpgradableModules) - 1)]
                        else:
                            ModuleToUpgrade = Dam[DesiredUpgradeLocation[0]][DesiredUpgradeLocation[1]]
                            if(ModuleToUpgrade != ""): #This line is just a damage control
                                if(Modules[ModuleToUpgrade]["upgradeCost"] > CurrentGold):
                                    PlayerAction = f"Saved to upgrade {ModuleToUpgrade} at location {DesiredUpgradeLocation}| Gold remaining : {Modules[ModuleToUpgrade]["upgradeCost"] - CurrentGold}"
                                    IsPlayerSaving = True
                                    hasMadeAChoice = True
                                else:
                                    CurrentGold = UpgradeModule(DesiredUpgradeLocation, CurrentGold)
                                    PlayerAction = f"Upgraded {ModuleToUpgrade} at {DesiredUpgradeLocation}"
                                    IsPlayerSaving = False
                                    DesiredUpgradeLocation = []
                                    hasMadeAChoice = True
                    case 3: # Unlock a new module
                        UnlockModule()
                        PlayerAction = "Unlock module"
                        hasMadeAChoice = True
                    case 4: # Invest in search
                        investSearch()
                        PlayerAction = "Invest Search"
                        hasMadeAChoice = True 
                    case 5: # Sell and buy module
                        #Select a random location
                        Locations = []
                        for location in SoldableModules:
                            Locations.append(location)
                        RandomLocation = random.choice(Locations)
                        print(RandomLocation)

                        # Sell current module and buy better module
                        
                        SellModule(RandomLocation, CurrentGold)

                        # Buy a better module
                        NewModule = SoldableModules[RandomLocation]
                        PlaceModule(NewModule,CurrentGold)
                        
                        PlayerAction = f"Sold the module at {RandomLocation} and bought {NewModule}"
                        hasMadeAChoice = True
        else:
            hasMadeAChoice = True


    return CurrentGold, PlayerAction, PlayerChoice, IsPlayerSaving, DesiredBuyModule, DesiredUpgradeLocation



"""POSSIBILITIES"""
# Will check all the possibilities for the player

#Returns what can be bought by the player
def CheckBuyPossibilities():
    #Finds which sections have a free spot
    SectionCounter = 0
    FreeSectionsIndexes = []
    for section in Dam:
        for spot in section:
            if(spot == ""):
                FreeSectionsIndexes.append(SectionCounter)
                break
        SectionCounter += 1
    
    #Reconstructs the free section list name
    FreeSections = []
    for index in FreeSectionsIndexes:
        FreeSections.append(Sections[index])

    #Finds what can be bought by the player function of the free sports
    BuyPossibilities = []

    match PlayerBehaviors[PlayerBehaviorIndex]:
        case "Random":
            for module in Modules:
                if(Modules[module]["section"] in FreeSections):
                    if(Modules[module]["buyCost"] <= CurrentGold):
                        BuyPossibilities.append(module)
        case "Yield Optimization":
            # Keep only the modules that are close to CurrentGold
            for module in Modules:
                if(Modules[module]["section"] in FreeSections):
                    if(Modules[module]["buyCost"] * PlayerPriceTolerance <= CurrentGold):
                        BuyPossibilities.append(module)
            
            # Keep only the Best Yield Module for each section
            BestYieldModules = []
            BestYieldModulesWithoutNones = []
            BestYieldModule = None
            if(BuyPossibilities):
                #print(BuyPossibilities)
                #print(Modules[possibility]["yield"] for possibility in BuyPossibilities)
                #PrintParametersList(BuyPossibilities, "yield")
                #input()
                for section in Sections:
                    BestYieldModule = None
                    for possibility in BuyPossibilities:
                        if (Modules[possibility]["section"] == section):
                            if(BestYieldModule is None):
                                BestYieldModule = possibility
                            else:
                                if(Modules[possibility]["yield"] > Modules[BestYieldModule]["yield"]):
                                    BestYieldModule = possibility
                    BestYieldModules.append(BestYieldModule)
                
                # Clear Nones
                for module in BestYieldModules:
                    if(module is not None):
                        BestYieldModulesWithoutNones.append(module)

                BuyPossibilities = BestYieldModulesWithoutNones
                #print(BuyPossibilities)
                #print(Modules[possibility]["yield"] for possibility in BuyPossibilities)
                #PrintParametersList(BuyPossibilities, "yield")
                #input()
        case "Electricity Optimization":
            # Keep only the modules that are close to CurrentGold
            for module in Modules:
                if(Modules[module]["section"] in FreeSections):
                    if(Modules[module]["buyCost"] * PlayerPriceTolerance <= CurrentGold):
                        BuyPossibilities.append(module)
            
            # Keep only the Best Output Module for each section
            BestOutputModules = []
            BestOutputModulesWithoutNones = []
            BestOutputModule = None
            if(BuyPossibilities):
                for section in Sections:
                    BestOutputModule = None
                    for possibility in BuyPossibilities:
                        if (Modules[possibility]["section"] == section):
                            if(BestOutputModule is None):
                                BestOutputModule = possibility
                            else:
                                if(Modules[possibility]["maximumInput"] * Modules[possibility]["yield"] > 
                                   Modules[BestOutputModule]["maximumInput"] * Modules[BestOutputModule]["yield"]):
                                    BestOutputModule = possibility
                    BestOutputModules.append(BestOutputModule)
                
                # Clear Nones
                for module in BestOutputModules:
                    if(module is not None):
                        BestOutputModulesWithoutNones.append(module)

                BuyPossibilities = BestOutputModulesWithoutNones
           
    return BuyPossibilities
            

#Returns a list of the sections that can be upgraded
def CheckBuySpots():
    BuySpots = []
    for section in Sections:
        #Convert the section name into an index
        SectionTypeCounter = ConvertSectionNameIntoIndex(section)

        #Checks if a new spot can be bought
        SpotTier = len(Dam[SectionTypeCounter]) - InitialSectionLength
        if(len(Dam[SectionTypeCounter]) - InitialSectionLength < len(SpotPrices)):
            if(SpotPrices[SpotTier] <= CurrentGold and CurrentCityLevel >= SpotCityLevels[SpotTier]):
                BuySpots.append(section)

    
    return BuySpots


#Returns a list of modules that can be sold because there is a buyable module with a better tier in Modules
def CheckSellPossibilities():
    # Parameters
    SectionCounter = 0
    ModuleLocations = []
    BetterModules = []
    SellPossibilities = {}
    hasBeenAdded = False
    BetterModulesForThisModule = []
    

    # Associate locations and better modules
    for section in Dam:
        SpotCounter = 0
        for module in section:
            #Check if there is a buyable module with a better yield
            if(module != ""):
                for anyModule in Modules:
                    match PlayerBehaviors[PlayerBehaviorIndex]:
                        case "Random":
                            if(Modules[module]["section"] == Modules[anyModule]["section"] 
                            and Modules[module]["tier"] < Modules[anyModule]["tier"]
                            and CurrentGold + Modules[module]["sellPrice"] > Modules[anyModule]["buyCost"]):
                                # Add sellable module location to a list
                                if(not hasBeenAdded):
                                    ModuleLocations.append((SectionCounter, SpotCounter))
                                    hasBeenAdded = True
                                # Add the better module to a list
                                BetterModulesForThisModule.append(anyModule)                       
                        case "Yield Optimization":
                            if(Modules[module]["section"] == Modules[anyModule]["section"] 
                            and Modules[module]["yield"] < Modules[anyModule]["yield"] #The modules must have a better yield
                            and CurrentGold + Modules[module]["sellPrice"] > Modules[anyModule]["buyCost"]):
                                # Add sellable module location to a list
                                if(not hasBeenAdded):
                                    ModuleLocations.append((SectionCounter, SpotCounter))
                                    hasBeenAdded = True
                                # Add the better module to a list
                                BetterModulesForThisModule.append(anyModule)
                        case "Electricity Optimization":
                            if(Modules[module]["section"] == Modules[anyModule]["section"] 
                            and Modules[module]["maximumInput"] * Modules[module]["yield"] < Modules[anyModule]["maximumInput"] * Modules[anyModule]["yield"] #The modules must have a better yield
                            and CurrentGold + Modules[module]["sellPrice"] > Modules[anyModule]["buyCost"]):
                                # Add sellable module location to a list
                                if(not hasBeenAdded):
                                    ModuleLocations.append((SectionCounter, SpotCounter))
                                    hasBeenAdded = True
                                # Add the better module to a list
                                BetterModulesForThisModule.append(anyModule)

            
            # Add the list of better modules to a bigger list
            if(BetterModulesForThisModule != []):
                BetterModules.append(BetterModulesForThisModule)
                BetterModulesForThisModule = []
            
            # Reset values between modules
            SpotCounter += 1
            hasBeenAdded = False
        SectionCounter += 1

    match PlayerBehaviors[PlayerBehaviorIndex]:
        case "Random":
            SellPossibilities = dict(zip(ModuleLocations, BetterModules))
        case "Yield Optimization":
            BetterYieldModules = []
            if(BetterModules):
                #PrintParametersList(BetterModules, "Yield")
                #input()
                for modules in BetterModules:
                    BestYieldModule = None
                    for module in modules:
                        if(BestYieldModule is None):
                            BestYieldModule = module
                        else:
                            if(Modules[module]["yield"] > Modules[BestYieldModule]["yield"]):
                                BestYieldModule = module
                    BetterYieldModules.append(BestYieldModule)
                #PrintParametersList(BetterYieldModules, "Yield")
                #input()
            SellPossibilities = dict(zip(ModuleLocations, BetterYieldModules))
        case "Electricity Optimization":
            BetterOutputModules = []
            if(BetterModules):
                for modules in BetterModules:
                    BestOutputModule = None
                    for module in modules:
                        if(BestOutputModule is None):
                            BestOutputModule = module
                        else:
                            if(Modules[module]["maximumInput"] * Modules[module]["yield"] > Modules[BestOutputModule]["maximumInput"] * Modules[BestOutputModule]["yield"]):
                                BestOutputModule = module
                    BetterOutputModules.append(BestOutputModule)
            SellPossibilities = dict(zip(ModuleLocations, BetterOutputModules))

    return SellPossibilities
    
#Returns the spot location where a module can be upgraded
def CheckUpgradableModules():
    UpgradableModules = []
    SectionCounter = 0
    SpotCounter = 0

    match PlayerBehaviors[PlayerBehaviorIndex]:
        case "Random":
            for section in Dam:
                for module in section:
                    if(module != ""):
                        # The module must exist in the Modules Dict and the player must have enough gold to upgrade it
                        if(Modules[module]["upgradeName"] != "" and Modules[module]["upgradeName"] in Modules and Modules[module]["upgradeCost"] <= CurrentGold):
                            UpgradableModules.append([SectionCounter, SpotCounter])
                    SpotCounter += 1
                SpotCounter = 0
                SectionCounter += 1
        case "Yield Optimization":
            DebugYieldList = []
            for section in Dam:
                for module in section:
                    if(module != ""):
                        if(Modules[module]["upgradeName"] != "" 
                           and Modules[module]["upgradeName"] in Modules 
                           and Modules[module]["upgradeCost"] * PlayerPriceTolerance <= CurrentGold):
                            UpgradableModules.append([SectionCounter, SpotCounter])
                            DebugYieldList.append(Modules[Dam[SectionCounter][SpotCounter]]["yield"])
                    SpotCounter += 1
                SpotCounter = 0
                SectionCounter += 1

            #print(DebugYieldList)
            # Select the best yield now
            BestYieldUpgrades = []
            BestYieldUpgradesWithoutNones = []
            BestYieldUpgrade = None
            BestYieldUpgradeLocation = []

            if(UpgradableModules):
                for section in Sections:
                    BestYieldUpgrade = None
                    for locations in UpgradableModules:
                        Module = Dam[locations[0]][locations[1]]
                        if(Modules[Module]["section"] == section):
                            if(BestYieldUpgrade is None):
                                BestYieldUpgrade = Modules[Module]["upgradeName"]
                                BestYieldUpgradeLocation = [locations[0], locations[1]]
                            else:
                                Upgrade = Modules[Module]["upgradeName"]
                                if(Upgrade != ""):
                                    if(Modules[Upgrade]["yield"] > Modules[BestYieldUpgrade]["yield"]):
                                        BestYieldUpgrade = Modules[Module]["upgradeName"]
                                        BestYieldUpgradeLocation = [locations[0], locations[1]]
                    BestYieldUpgrades.append(BestYieldUpgradeLocation)
                #print(BestYieldUpgrades) #Debug
            
            if(BestYieldUpgrades):
                for location in BestYieldUpgrades:
                    if(location != []):
                        BestYieldUpgradesWithoutNones.append(location)
                #print(BestYieldUpgradesWithoutNones) #Debug

            # Set the final export variable
            UpgradableModules = BestYieldUpgradesWithoutNones
        case "Electricity Optimization":
            for section in Dam:
                for module in section:
                    if(module != ""):
                        if(Modules[module]["upgradeName"] != "" 
                           and Modules[module]["upgradeName"] in Modules 
                           and Modules[module]["upgradeCost"] * PlayerPriceTolerance <= CurrentGold):
                            UpgradableModules.append([SectionCounter, SpotCounter])
                    SpotCounter += 1
                SpotCounter = 0
                SectionCounter += 1

            # Select the best yield now
            BestOutputUpgrades = []
            BestOutputUpgradesWithoutNones = []
            BestOutputUpgrade = None
            BestOutputUpgradeLocation = []

            if(UpgradableModules):
                for section in Sections:
                    BestOutputUpgrade = None
                    for locations in UpgradableModules:
                        Module = Dam[locations[0]][locations[1]]
                        if(Modules[Module]["section"] == section):
                            if(BestOutputUpgrade is None):
                                BestOutputUpgrade = Modules[Module]["upgradeName"]
                                BestOutputUpgradeLocation = [locations[0], locations[1]]
                            else:
                                Upgrade = Modules[Module]["upgradeName"]
                                if(Upgrade != ""):
                                    if(Modules[Upgrade]["maximumInput"] * Modules[Upgrade]["yield"] > 
                                       Modules[BestOutputUpgrade]["maximumInput"] * Modules[BestOutputUpgrade]["yield"]):
                                        BestOutputUpgrade = Modules[Module]["upgradeName"]
                                        BestOutputUpgradeLocation = [locations[0], locations[1]]
                    BestOutputUpgrades.append(BestOutputUpgradeLocation)
            
            if(BestOutputUpgrades):
                for location in BestOutputUpgrades:
                    if(location != []):
                        BestOutputUpgradesWithoutNones.append(location)

            # Set the final export variable
            UpgradableModules = BestOutputUpgradesWithoutNones

    return UpgradableModules

def checkUnlockModule():
    unlockModule = False

    if searchCounter > 0 and len(AllModules) != 0:
        unlockModule = True
    else:
        unlockModule = False
    
    return unlockModule


def checkInvest():
    investSearch = False

    if CurrentGold >= priceInvest:
        investSearch = True
    else:
        investSearch = False
    
    return investSearch


# Returns the current possibilities for the player
def ReturnPossibilities():
    #Check possibilities
    Possibilities = []
    BuyableModules = CheckBuyPossibilities()
    BuyableSpots = CheckBuySpots()
    UpgradableModules = CheckUpgradableModules()
    UnlockableModule = checkUnlockModule()
    InvestSearch = checkInvest()
    SoldableModules = CheckSellPossibilities()

    if(BuyableModules != []):
        Possibilities.append(1)
    else:
        Possibilities.append(0)

    if(BuyableSpots != []):
        Possibilities.append(1)
    else:
        Possibilities.append(0)

    if(UpgradableModules != []):
        Possibilities.append(1)
    else:
        Possibilities.append(0)
    
    if UnlockableModule != False:
        Possibilities.append(1)
    else:
        Possibilities.append(0)

    if InvestSearch != False: 
        Possibilities.append(1)
    else:
        Possibilities.append(0)

    if(SoldableModules):
        Possibilities.append(1)
    else:
        Possibilities.append(0)

    return Possibilities, BuyableModules, BuyableSpots, UpgradableModules, UnlockableModule, InvestSearch, SoldableModules



"""ACTIONS FUNCTIONS"""

#Conditions : avoir une place libre + avoir assez de gold
def PlaceModule(Module, CurrentGold):
    #Find the section where to put the module
    SectionTypeCounter = ConvertSectionNameIntoIndex(Modules[Module]["section"])
    
    #Reduce current gold function of module price
    ModuleCost = Modules[Module]["buyCost"]
    CurrentGold -= ModuleCost

    #Place module in the dam
    SpotCounter = 0
    for spot in Dam[SectionTypeCounter]:
        if(spot == ""):
            Dam[SectionTypeCounter][SpotCounter] = Module
        else:
            SpotCounter += 1

    return CurrentGold

#Conditions : avoir une section inférieur au tier maximale
def BuySpot(SectionName, CurrentGold):
    #Convert the section name into an index
    SectionTypeCounter = ConvertSectionNameIntoIndex(SectionName)

    #Find the spot tier
    SpotTier = len(Dam[SectionTypeCounter]) - InitialSectionLength

    #Reduce current gold function of section tier
    CurrentGold -= SpotPrices[SpotTier]

    #Increase section length
    Dam[SectionTypeCounter].append("")

    return CurrentGold

#Conditions : avoir des modules
def SellModule(SpotLocation : tuple, CurrentGold):
    #Retrieve the module
    Module = Dam[SpotLocation[0]][SpotLocation[1]]

    #Gold transaction
    CurrentGold += Modules[Module]["sellPrice"]

    #Update the dam
    Dam[SpotLocation[0]][SpotLocation[1]] = ""

    return CurrentGold

#Conditions : Avoir un module ayant un niveau pas maximal
def UpgradeModule(SpotLocation : tuple, CurrentGold):
    #Retrieve the module
    Module = Dam[SpotLocation[0]][SpotLocation[1]]

    #Gold transaction
    CurrentGold -= Modules[Module]["upgradeCost"]

    #Update the dam
    Dam[SpotLocation[0]][SpotLocation[1]] = Modules[Module]["upgradeName"]

    return CurrentGold

#Debloque un nouveau module aléatoire
def UnlockModule():
    availableModule = []
    dropRateModule = []
    for m in AllModules:
        if AllModules[m].get("cityLevel") == CurrentCityLevel:
            availableModule.append(m)
            dropRateModule.append(dropRate[0])
        elif AllModules[m].get("cityLevel") >= CurrentCityLevel-1:
            availableModule.append(m)
            dropRateModule.append(dropRate[1])
        elif AllModules[m].get("cityLevel") >= CurrentCityLevel-2:
            availableModule.append(m)
            dropRateModule.append(dropRate[2])

    print(f"Available Modules : {availableModule}")
    # print(f"Pondération Modules {dropRateModule}")
    if(availableModule):
        minimumToPropose = min(nbSearchProposed, len(availableModule))
        dropRateModuleScaled = np.array(dropRateModule) / sum(np.array(dropRateModule))
        # print(dropRateModuleScaled)
        proposeModule = np.random.choice(availableModule, minimumToPropose, False, dropRateModuleScaled)
        global searchCounter

        print(f"Propose Modules : {proposeModule}")

        newModuleSelect = random.choice(proposeModule)
        match PlayerBehaviors[PlayerBehaviorIndex]:
            case "Random":
                newModuleSelect = random.choice(proposeModule)
            case "Yield Optimization":
                BestYieldModule = None
                for module in proposeModule:
                    if(BestYieldModule is None):
                        BestYieldModule = module
                    else:
                        if(Modules[module]["yield"] > Modules[BestYieldModule]["yield"]):
                            BestYieldModule = module
                newModuleSelect = BestYieldModule
            case "Electricity Optimization":
                BestOutputModule = None
                for module in proposeModule:
                    if(BestOutputModule is None):
                        BestOutputModule = module
                    else:
                        if(Modules[module]["maximumInput"] * Modules[module]["yield"] > 
                           Modules[BestOutputModule]["maximumInput"] * Modules[BestOutputModule]["yield"]):
                            BestOutputModule = module
                newModuleSelect = BestOutputModule                

        print(f"Module Selected : {newModuleSelect}")
        parent = AllModules[newModuleSelect].get("parent")

        for m in parent:
            if AllModules.get(m) != None:
                #if(Modules[m] == None): #Check if the modules already exists in Modules #Not necessary anymore
                Modules[m] = AllModules.get(m) #This line overwrite the values inputed in the dict Modules
                AllModules.pop(m)

        searchCounter -= 1

def investSearch():
    global CurrentGold
    global priceInvest
    global progressBar
    global eachPriceInvest
    global totalSearchCounter

    if totalSearchCounter < len(eachPriceInvest):
        priceInvest = eachPriceInvest[totalSearchCounter]
    else:
        priceInvest = eachPriceInvest[len(eachPriceInvest)-1]

    CurrentGold -= priceInvest
    progressBar += speed

"""UTILS FUNCTIONS"""

def ConvertSectionNameIntoIndex(SectionName):
    SectionTypeCounter = 0
    for section in Sections:
      if(SectionName == section):
          break
      else:
          SectionTypeCounter += 1
    
    return SectionTypeCounter

def mround(number, multiple):
    # round to the closest multiple
    # ex : mround(18,10) = 20
    return multiple * round(number / multiple)

def ComputeDurationsFromTimes(Times : list):
    Counter = 0
    Duration = 0
    Durations = []
    for time in Times:
        if(time != Times[len(Times) - 1]):
            Duration = Times[Counter + 1] - time
            Durations.append(Duration)
            Counter += 1
        else:
            break

    return Durations

def PrintParametersList(List: list, Parameter : str):
    ParameterList = []
    for element in List:
        ParameterList.append(Modules[element][Parameter])
    print(f"{Parameter} : {ParameterList}")


"""CITY FUNCTIONS"""

def UpdatedCityNeeds (Time : float):
    ratio = Time / TargetTime
    result = TargetNeeds * pow(ratio, SpeedCoeffA) * (1 - pow(1 - ratio, SpeedCoeffB))
    return result

def UpdatedCityGold (Gold: float): 
      Gold += CityLevels[CurrentCityLevel]["GoldGeneration"]
      return round(Gold)

def UpdatedCityLevel (Electricity: float, CurrentCityLevel: int):
    if (CityLevels[CurrentCityLevel]["NextLevelElectricity"] != 0): #Checked if the city is not max level
        if (Electricity >= CityLevels[CurrentCityLevel]["NextLevelElectricity"]):
            CurrentCityLevel += 1
    return CurrentCityLevel

            
"""DAM FUNCTIONS"""

def UpdateDam():
    SectionsOutputs = [0,0,0]
    TurbineAmount = 0
    GenerateurAmount = 0

    # Counts modules number
    for turbine in Dam[1]:
        if(turbine != ""):
            TurbineAmount += 1

    for generateur in Dam[2]:
        if(generateur != ""):
            GenerateurAmount += 1

    # Canalisations output
    for canalisation in Dam[0]:
          if(canalisation != ""):
            SectionsOutputs[0] += mround(Modules[canalisation]["maximumInput"] * Modules[canalisation]["yield"], 10)


    # Turbines output
    for turbine in Dam[1]:
          if(turbine != ""):
            if((SectionsOutputs[0] / TurbineAmount) > Modules[turbine]["maximumInput"]):
              input = Modules[turbine]["maximumInput"]
            else:
              input = SectionsOutputs[0] / TurbineAmount
            
            SectionsOutputs[1] += mround(input * Modules[turbine]["yield"], 10)

    # Generateurs output
    for generateur in Dam[2]:
        if(generateur != ""):
          if((SectionsOutputs[1] / GenerateurAmount) > Modules[generateur]["maximumInput"]):
              input = Modules[generateur]["maximumInput"]
          else:
              input = SectionsOutputs[1] / GenerateurAmount

          SectionsOutputs[2] += mround(input * Modules[generateur]["yield"], 10)

    return round(SectionsOutputs[0]) * BoostWaterConsumption, round(SectionsOutputs[2]) * BoostElectricityOutput

def ComputeTotalYield():
    TotalYield = 0
    for section in Dam:
        for module in section:
            if(module != ""):
                TotalYield += Modules[module]["yield"]
    
    return round(TotalYield, 1)

def ComputeTotalWaterConsumption():
    TotalWaterConsumption = 0
    for section in Dam:
        for module in section:
            if(module != ""):
                if(Modules[module]["section"] == "Canalisations"):
                    TotalWaterConsumption += Modules[module]["maximumInput"]
    
    return round(TotalWaterConsumption * BoostWaterConsumption, 1)


"""SEARCH FUNCTION"""

def updateSpeedSearch():
    global speed

    if CurrentCityLevel > len(speedCityLevel):
        speed = speedCityLevel[len(speedCityLevel)-1]
    else:
        speed = speedCityLevel[CurrentCityLevel-1]


"""COMPUTING FUNCTIONS FOR VISUALIZATION"""

def UpdateGamePhases(Time : float, GamePhasesTimes : list, GamePhase):
    #Initialize parameters
    areAllSectionsMaxLength = True
    areAllSectionsFull = True
    areAllModulesMaxed = True

    # Checks if all sections are max length
    for section in Dam:
        if(len(section) < InitialSectionLength + len(SpotPrices)):
            areAllSectionsMaxLength = False
    
    # Checks if all spots are not empty
    if(areAllSectionsMaxLength):
        for section in Dam:
            for module in section:
                if(module == ""):
                    areAllSectionsFull = False
    
    # Checks if all modules are fully upgraded
    #print(areAllSectionsFull)
    if(areAllSectionsFull):
        for section in Dam:
            for module in section:
                if(module != "" and Modules[module]["upgradeName"] != "" and Modules[module]["upgradeName"] in Modules):
                    areAllModulesMaxed = False

    # If the dam is full and we are in the "Playing" game phase -> Switch the game phase to "Nothing" and append time
    if(areAllSectionsMaxLength and areAllSectionsFull and areAllModulesMaxed and GamePhase == "Playing"):
        GamePhase = GamePhases[0] 
        GamePhasesTimes.append(Time)
    # If the dam is not full and we are in the "Nothing" game phase -> Switch the game phase to "Playing" and append time
    if((not areAllSectionsMaxLength or not areAllSectionsFull or not areAllModulesMaxed) and GamePhase == "Nothing"):
        GamePhase = GamePhases[1] 
        GamePhasesTimes.append(Time)
    
    return GamePhase, GamePhasesTimes

def UpdateCityLevelsTimes(Time : float, CityLevelsTimes : list, NextCityLevel : int):
    # Adds the current time if the city level had increased
    if(CurrentCityLevel == NextCityLevel):
        NextCityLevel += 1
        CityLevelsTimes.append(Time)
    
    return CityLevelsTimes, NextCityLevel


"""   ---------------   SIMULATION   ---------------   """

def run():
    """Lance la boucle de simulation. Retourne un dict de données pour la visualisation."""
    global CurrentGold, PlayerAction, CurrentElectricity
    global WaterSupply, WaterBalance
    global UpdateGoldCounter, UpdateNeedsCounter, CurrentNeeds, CurrentCityLevel
    global progressBar, speed, distance, searchCounter, totalSearchCounter, CurrentGameState
    global InitialSectionLength, NextCityLevel, CurrentGamePhase
    global GamePhasesTimes, GamePhasesDurations, CityLevelsTimes, CityLevelsDurations
    global PlayerChoice, IsPlayerSaving, DesiredBuyModule, DesiredUpgradeLocation

    # ── Initialisation ──────────────────────────────────────────────────────
    InitialSectionLength = len(Dam[0])
    NextCityLevel = CurrentCityLevel + 1

    SimulationTimes = []
    CityLevelsData        = {"Level": [], "Time": []}
    ElectricityOverTimeData = {"Electricity": [], "Time": []}
    NeedsOverTimeData     = {"Needs": [], "Time": []}
    SearchOverTime        = {"Search": [], "Speed": [], "Time": []}
    WaterOverTime         = {"WaterSupply": [], "WaterBalance": [], "WaterConsumption": [], "Time": []}

    InitialSectionLength = len(Dam[0])
    NextCityLevel = CurrentCityLevel + 1

    #Data visualization
    SimulationTimes = []
    CityLevelsData = {
        "Level" : [],
        "Time" : []
    }
    ElectricityOverTimeData = {
        "Electricity" : [],
        "Time" : []
    }
    NeedsOverTimeData = {
        "Needs" : [],
        "Time" : []
    }
    SearchOverTime = {
        "Search" : [],
        "Speed" : [],
        "Time" : []
    }
    WaterOverTime = {
        "WaterSupply" : [],
        "WaterBalance" : [],
        "WaterConsumption" : [],
        "Time" : []
    }


    #Utils
    #SimulationDuration * 60

    for time in range(SimulationDuration * 60):

        #-------------- Player actions --------------
        Possibilities, BuyableModules, BuyableSpots, UpgradableModules, UnlockableModule, InvestSearch, SoldableModule = ReturnPossibilities()

        match PlayerBehaviors[PlayerBehaviorIndex]:
            case "Random":
                CurrentGold, PlayerAction = SelectRandomActions(Possibilities, BuyableModules, BuyableSpots, UpgradableModules, UnlockableModule, InvestSearch, SoldableModule, CurrentGold, PlayerAction)
            case "Yield Optimization":
                CurrentGold, PlayerAction, PlayerChoice, IsPlayerSaving, DesiredBuyModule, DesiredUpgradeLocation = SelectOptimizedActions(Possibilities, BuyableModules, 
                                                                        BuyableSpots, UpgradableModules, UnlockableModule, 
                                                                        InvestSearch, SoldableModule, 
                                                                        CurrentGold, PlayerAction, PlayerChoice, IsPlayerSaving, DesiredBuyModule, DesiredUpgradeLocation)
            case "Electricity Optimization":
                CurrentGold, PlayerAction, PlayerChoice, IsPlayerSaving, DesiredBuyModule, DesiredUpgradeLocation = SelectOptimizedActions(Possibilities, BuyableModules, 
                                                                        BuyableSpots, UpgradableModules, UnlockableModule, 
                                                                        InvestSearch, SoldableModule, 
                                                                        CurrentGold, PlayerAction, PlayerChoice, IsPlayerSaving, DesiredBuyModule, DesiredUpgradeLocation)
            case "Water Optimization":
                print("Water Optimized Behavior not done yet")


        #-------------- Dam --------------
        #CurrentElectricity += 1000
        CurrentElectricity = UpdateDam()[1]

        WaterSupply -= ComputeTotalWaterConsumption()

        if(WaterSupply < MaxWaterSupply - WaterRegen):
            WaterSupply += WaterRegen
        else:
            WaterSupply = MaxWaterSupply

        WaterBalance = WaterRegen - ComputeTotalWaterConsumption()


        #-------------- City --------------
        #--- Gold
        UpdateGoldCounter += 1
        if (UpdateGoldCounter % GoldUpdateRate == 0):
            CurrentGold = UpdatedCityGold(CurrentGold)

        #--- Needs
        UpdateNeedsCounter += 1
        if (UpdateNeedsCounter % CityUpdateRate == 0):
            CurrentNeeds = UpdatedCityNeeds(time)

        #--- Levels
        CurrentCityLevel = UpdatedCityLevel(CurrentElectricity, CurrentCityLevel)

        #-------------- Search --------------
        #--- Progress Bar
        updateSpeedSearch()
        progressBar += speed
        if progressBar >= distance:
            progressBar = 0
            searchCounter += 1
            totalSearchCounter += 1
            distance += 10

        #-------------- Lose conditions --------------
        # if(WaterSupply < 0 and not(IsWaterPoolInfinite)):
        #     CurrentGameState = GameStates[1]
        # if (CurrentElectricity < CurrentNeeds - CurrentNeeds * AuthorizedDifferenceWithNeeds):
        #     CurrentGameState = GameStates[2]


        #-------------- Win conditions --------------
        if (CurrentElectricity > CurrentNeeds and CurrentCityLevel >= RequiredCityLevelToWin and WaterBalance > 0):
            CurrentGameState = GameStates[3]


        #-------------- Console Display --------------
        #print(f"Current Game State : {CurrentGameState}")
        # if time > 0 and  time < 127: # Une periode de temps
        # if time % 300 == 0: #Toutes les minutes
        print("\n----------------\n")
        print(f"Time in seconds : {time + 1}")
        # print(f"Time in minutes : {(time + 1)//60} min {(time + 1)%60} seconds")
        # print(f"AllModule : {list(AllModules.keys())}")
        # print(f"Modules : {list(Modules.keys())}")
        print(f"Current Player Behavior: {PlayerBehaviors[PlayerBehaviorIndex]}")
        print(f"Player Action: {PlayerAction}")
        print(f"Dam state: {Dam}")
        print(f"Total Yield = {ComputeTotalYield()}")
        # print(f"Current City Level : {CurrentCityLevel}")
        # print(f"City Next Level Electricity : {CityLevels[CurrentCityLevel]["NextLevelElectricity"]}")
        print(f"Current Electricity : {CurrentElectricity}")
        print(f"Current Gold : {CurrentGold}")
        # print(f"Current Needs : {round(CurrentNeeds)}")
        # print(f"Current Water Balance: {WaterBalance}")
        # print(f"Current Water Supply: {WaterSupply}")
        # print(f"Current Water Consumption : {ComputeTotalWaterConsumption()}")
        # print(f"Search Speed : {speed}")
        # print(f"ProgressBar : {progressBar}/{distance}")
        # print(f"Search Counter : {searchCounter}")
        # print(f"Total Search Counter : {totalSearchCounter}")
        #input()


        #--------------- Data gathering for plotting ---------------
        # Time
        SimulationTimes.append(time)

        # City levels over time
        CityLevelsData["Level"].append(CurrentCityLevel)
        CityLevelsData["Time"].append(time)
        # City Durations
        CityLevelsTimes, NextCityLevel = UpdateCityLevelsTimes(time, CityLevelsTimes, NextCityLevel)

        # Electricity over time
        ElectricityOverTimeData["Electricity"].append(CurrentElectricity)
        ElectricityOverTimeData["Time"].append(time)

        # Needs over time
        NeedsOverTimeData["Needs"].append(CurrentNeeds)
        NeedsOverTimeData["Time"].append(time)

        # Search over time
        SearchOverTime["Search"].append(totalSearchCounter)
        SearchOverTime["Speed"].append(speed)
        SearchOverTime["Time"].append(time)

        # Water over time
        WaterOverTime["WaterBalance"].append(WaterBalance)
        WaterOverTime["WaterConsumption"].append(UpdateDam()[0])
        WaterOverTime["WaterSupply"].append(WaterSupply)
        WaterOverTime["Time"].append(time)

        # Game Phases time
        CurrentGamePhase, GamePhasesTimes = UpdateGamePhases(time, GamePhasesTimes, CurrentGamePhase)



        #-------------- Break --------------
        if(CurrentGameState == GameStates[1] or CurrentGameState == GameStates[2] or CurrentGameState == GameStates[3]):
            print(f"\nFinal Game State : {CurrentGameState}")

            break


    return {
        "SimulationTimes":          SimulationTimes,
        "CityLevelsData":           CityLevelsData,
        "ElectricityOverTimeData":  ElectricityOverTimeData,
        "NeedsOverTimeData":        NeedsOverTimeData,
        "SearchOverTime":           SearchOverTime,
        "WaterOverTime":            WaterOverTime,
        "CityLevelsTimes":          CityLevelsTimes,
        "GamePhasesTimes":          GamePhasesTimes,
    }
