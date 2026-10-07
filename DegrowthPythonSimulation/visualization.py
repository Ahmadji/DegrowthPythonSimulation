import matplotlib.pyplot as plt
import pandas as pd
from simulation_functions import ComputeDurationsFromTimes, CityLevels


def show_graphs(data,
                showElectricityNeedCityGraphs=True,
                showWaterGraphs=False,
                showSearchGraph=False,
                showGamePhasesGraph=False):
    """Affiche les graphes selon les options passées en paramètre.

    Args:
        data: dict retourné par simulation_functions.run()
        showElectricityNeedCityGraphs: affiche électricité, besoins, niveaux de ville
        showWaterGraphs:   affiche les graphes eau
        showSearchGraph:   affiche le graphe de recherche
        showGamePhasesGraph: affiche les durées des phases de jeu
    """
    SimulationTimes          = data["SimulationTimes"]
    CityLevelsData           = data["CityLevelsData"]
    ElectricityOverTimeData  = data["ElectricityOverTimeData"]
    NeedsOverTimeData        = data["NeedsOverTimeData"]
    SearchOverTime           = data["SearchOverTime"]
    WaterOverTime            = data["WaterOverTime"]
    CityLevelsTimes          = data["CityLevelsTimes"]
    GamePhasesTimes          = data["GamePhasesTimes"]

    # Initialisé ici car il peut être référencé avant le bloc showGamePhasesGraph
    GamePhasesDurations = []

    # Electricity, Needs, City Graphs
    if(showElectricityNeedCityGraphs):
        # Electricity and Needs over time
        plt.plot(ElectricityOverTimeData["Time"], ElectricityOverTimeData["Electricity"], color = "#d1a700", label = "Electricity Production")
        plt.plot(ElectricityOverTimeData["Time"], NeedsOverTimeData["Needs"], color = "#b31500", label = "City Needs")
        plt.xlabel("Time in seconds")
        plt.ylabel("Energy in W")
        plt.title("Electricity Production and City Needs over Time")
        plt.legend()
        #plt.show()


        # City levels over time
        CityLevelsOverTimedf = pd.DataFrame(CityLevelsData)
        CityLevelsOverTimePlot = CityLevelsOverTimedf.plot(x = "Time", y = "Level", color = "#343444")
        CityLevelsOverTimePlot.set_xlabel("Time in seconds")
        CityLevelsOverTimePlot.set_ylabel("City Level")
        CityLevelsOverTimePlot.set_title("City Level Over Time")
        CityLevelsOverTimePlot.set_ylim([1, len(CityLevels) + 1])


        # City levels durations

        # Add final time to City Levels Times
        CityLevelsTimes.append(SimulationTimes[-1])

        # Computes the duration list
        CityLevelsDurations = ComputeDurationsFromTimes(CityLevelsTimes)

        # Parameters and computing
        CityLevelsIndexes = []
        Counter = 0
        for duration in CityLevelsDurations:
            Counter += 1
            CityLevelsIndexes.append(Counter)

        # Plotting
        fig, CityLevelsDurationsPlot = plt.subplots()
        Bar = CityLevelsDurationsPlot.bar(CityLevelsIndexes, CityLevelsDurations, color = "#343444")
        CityLevelsDurationsPlot.set_xlabel("City Level")
        CityLevelsDurationsPlot.set_ylabel("Duration in seconds")
        CityLevelsDurationsPlot.set_title("City Levels Durations")
        CityLevelsDurationsPlot.bar_label(Bar, GamePhasesDurations)

        plt.show()


    # Water Graphs
    if(showWaterGraphs):
    # Water Supply Over Time
        WaterOverTimedf = pd.DataFrame(WaterOverTime)
        WaterSupplyOverTimePlot = WaterOverTimedf.plot(x = "Time", y = "WaterSupply", color = "#28ace4")
        WaterSupplyOverTimePlot.set_xlabel("Time in seconds")
        WaterSupplyOverTimePlot.set_ylabel("Water Supply")
        WaterSupplyOverTimePlot.set_title("Water Supply Over Time")
        #plt.show()

        # Water Balance Over Time - To do next : dynamic coloring
        # WaterBalanceOverTimePlot = WaterOverTimedf.plot(x = "Time", y = "WaterBalance", color = "#28ace4")
        # WaterBalanceOverTimePlot.set_xlabel("Time in seconds")
        # WaterBalanceOverTimePlot.set_ylabel("Water Balance")
        # WaterBalanceOverTimePlot.set_title("Water Balance Over Time")
        #plt.show()

        # Water Consumption Over Time
        WaterConsumptionOverTimePlot = WaterOverTimedf.plot(x = "Time", y = "WaterConsumption", color = "#28ace4")
        WaterConsumptionOverTimePlot.set_xlabel("Time in seconds")
        WaterConsumptionOverTimePlot.set_ylabel("Water Consumption")
        WaterConsumptionOverTimePlot.set_title("Water Consumption Over Time")
        plt.show()


    # Search Graph
    if(showSearchGraph):
        plt.plot(SearchOverTime["Time"], SearchOverTime["Search"], color = "#7300bb", label = "Search")
        plt.plot(SearchOverTime["Time"], SearchOverTime["Speed"], color = "#b31500", label = "Speed")
        plt.xlabel("Time in seconds")
        plt.ylabel("Search")
        plt.title("Search and Speed over Time")
        plt.legend()
        plt.show()


    # Game Phases Durations
    if(showGamePhasesGraph):
        # Add final time to Game Phases Times
        GamePhasesTimes.append(SimulationTimes[-1])
        # Computes the duration list
        GamePhasesDurations = ComputeDurationsFromTimes(GamePhasesTimes)

        # Parameters and computing
        Counter = 0
        GamePhasesDurationPlotColors = []
        GamePhasesDurationPlotLabels = []
        GamePhasesIndexes = []
        for duration in GamePhasesDurations:
            GamePhasesIndexes.append(Counter)
            if(Counter % 2 == 0):
                #Playing : creating a list of colors and labels for bar diagram
                GamePhasesDurationPlotColors.append('tab:blue')
                GamePhasesDurationPlotLabels.append('playing')
            else:
                #Nothing : creating a list of colors and labels for bar diagram
                GamePhasesDurationPlotColors.append('tab:red')
                GamePhasesDurationPlotLabels.append('nothing')

            Counter += 1

        # Plotting
        fig, GamePhasesDurationsPlot = plt.subplots()
        Bar = GamePhasesDurationsPlot.bar(GamePhasesIndexes, GamePhasesDurations, label = GamePhasesDurationPlotLabels, color = GamePhasesDurationPlotColors)
        GamePhasesDurationsPlot.set_xlabel("Game Phases")
        GamePhasesDurationsPlot.set_xticklabels("")
        GamePhasesDurationsPlot.set_ylabel("Duration in seconds")
        GamePhasesDurationsPlot.set_title("Game Phases Durations")
        GamePhasesDurationsPlot.bar_label(Bar, GamePhasesDurations)
        handles, labels = GamePhasesDurationsPlot.get_legend_handles_labels() #Legend
        unique = dict(zip(labels, handles)) 
        a = zip(labels, handles) # dict keeps first occurrence, drops duplicates
        GamePhasesDurationsPlot.legend(unique.values(), unique.keys())
        plt.show()
