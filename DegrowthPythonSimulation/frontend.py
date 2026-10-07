from nicegui import ui

import subprocess, json, ast

import defaultParameters as m
from simulation_functions import ComputeDurationsFromTimes

# ═══════════════════════════════════════════════════════════════════════════════
#  STYLES
# ═══════════════════════════════════════════════════════════════════════════════

ui.add_head_html('''
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg:    #EEEAE0;  --surf:  #EEEAE0;  --card: #D6CFC4;
    --inp:   #D6CFC4;  --bdr:   #B0A49B;  --bdr2: #696969;
    --blue:  #696969;  --green: #94C276;
    --t1:    #696969;  --t2:    #B0A49B;  --t3:   #B0A49B;
  }
  html, body { background: var(--bg) !important; }

  /* ── NiceGUI/Quasar layout ── */
  .q-drawer { background: var(--surf) !important; border-right: 1px solid var(--bdr) !important; }
  .q-header { background: var(--surf) !important; border-bottom: 1px solid var(--bdr) !important; box-shadow: none !important; }

  /*
   * Make the page a flex column so tabs + tab-panels can fill the
   * remaining height without any manual calc().
   */
  .q-page {
    display: flex !important;
    flex-direction: column !important;
    overflow: hidden !important;
    padding: 0 !important;
  }

  /* ── Tabs bar ── */
  .q-tabs {
    flex-shrink: 0 !important;
    background: var(--surf) !important;
    border-bottom: 1px solid var(--bdr) !important;
  }
  .q-tab        { color: var(--t3) !important; font-family: 'DM Sans', sans-serif !important; }
  .q-tab__label { text-transform: none !important; font-size: 0.82rem !important; font-weight: 600 !important; }
  .q-tab--active     { color: var(--blue) !important; }
  .q-tab__indicator  { background: var(--blue) !important; height: 2px !important; }

  /* ── Tab panels fill remaining page height ── */
  .q-tab-panels {
    flex: 1 !important;
    min-height: 0 !important;
    background: transparent !important;
    overflow: hidden !important;
  }
  .q-tab-panel {
    height: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    padding: 10px 14px !important;
    overflow: hidden !important;
  }

  /* ── Chart grid: distributes cards equally ── */
  .chart-grid {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 100%;
  }
  .chart-card {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
    background: var(--card);
    border: 1px solid var(--bdr);
    border-radius: 10px;
    padding: 12px 14px 8px;
    overflow: hidden;
  }
  .chart-title {
    flex-shrink: 0;
    font-size: 0.6rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--t3);
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 6px;
  }
  /* EChart element fills the card */
  nicegui-echart { flex: 1 !important; min-height: 0 !important; }

  /* ── Inputs ── */
  .q-field--outlined .q-field__control          { background: var(--inp) !important; border-radius: 6px !important; }
  .q-field--outlined .q-field__control:before   { border-color: var(--bdr) !important; }
  .q-field--outlined.q-field--focused .q-field__control:before { border-color: var(--blue) !important; border-width: 1px !important; }
  .q-field__label  { color: var(--t3) !important;  font-family: 'JetBrains Mono', monospace !important; font-size: 0.7rem !important; }
  .q-field__native { color: var(--t1) !important;  font-family: 'JetBrains Mono', monospace !important; font-size: 0.8rem !important; }
  .q-select__dropdown-icon { color: var(--t3) !important; }

  /* ── Sidebar section labels ── */
  .sct {
    font-size: 0.58rem; font-weight: 600; letter-spacing: 0.14em;
    text-transform: uppercase; color: var(--blue);
    font-family: 'JetBrains Mono', monospace;
    border-top: 1px solid var(--bdr);
    padding-top: 14px; margin-top: 8px;
    display: flex; align-items: center; gap: 5px;
  }
  .sct:first-child { border-top: none; margin-top: 0; padding-top: 0; }
  .sct .material-icons { font-size: 12px; }

  /* ── Status dot ── */
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:.4} }
  .dot { width: 7px; height: 7px; border-radius: 50%; background: var(--green); box-shadow: 0 0 6px var(--green); animation: blink 2.4s infinite; }

  /* ── Buttons ── */
  .btn-launch { background: var(--blue) !important; color: #696969 !important; font-weight: 700 !important; border-radius: 7px !important; font-size: 0.78rem !important; }
  .btn-save   { border: 1px solid var(--bdr) !important; color: var(--t2) !important; border-radius: 7px !important; font-size: 0.78rem !important; }
</style>
''')

ui.dark_mode().enable()


# ═══════════════════════════════════════════════════════════════════════════════
#  ECHART HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

_MONO = 'JetBrains Mono'
_G    = '#B0A49B'   # grid colour
_T    = '#696969'   # label colour

def _axes(x_label, y_label):
    return {
        'xAxis': {
            'type': 'category', 'name': x_label, 'data': None,
            'nameTextStyle': {'color': _T, 'fontSize': 9},
            'axisLine': {'lineStyle': {'color': _G}}, 'axisTick': {'show': False},
            'axisLabel': {'color': _T, 'fontFamily': _MONO, 'fontSize': 9},
            'splitLine': {'show': False},
        },
        'yAxis': {
            'type': 'value', 'name': y_label,
            'nameTextStyle': {'color': _T, 'fontSize': 9},
            'axisLine': {'show': False}, 'axisTick': {'show': False},
            'axisLabel': {'color': _T, 'fontFamily': _MONO, 'fontSize': 9},
            'splitLine': {'lineStyle': {'color': _G, 'type': 'dashed'}},
        },
    }

def mk_line(x_label, y_label, series):
    cfg = {
        'backgroundColor': 'transparent',
        'textStyle': {'fontFamily': _MONO, 'color': _T},
        'tooltip': {'trigger': 'axis', 'backgroundColor': '#B0A49B', 'borderColor': _G,
                    'textStyle': {'color': '#696969', 'fontFamily': _MONO, 'fontSize': 11}},
        'legend': {'data': [s['name'] for s in series],
                   'textStyle': {'color': _T, 'fontFamily': _MONO, 'fontSize': 10},
                   'top': 0, 'right': 4},
        'grid': {'top': 28, 'right': 16, 'bottom': 24, 'left': 50},
        'series': [{
            'name': s['name'], 'type': 'line', 'data': None,
            'smooth': True, 'symbol': 'none',
            'itemStyle': {'color': s['color']}, 'lineStyle': {'color': s['color'], 'width': 2},
            'areaStyle': {'color': {'type': 'linear', 'x': 0, 'y': 0, 'x2': 0, 'y2': 1,
                'colorStops': [{'offset': 0, 'color': s['color'] + '28'}, {'offset': 1, 'color': s['color'] + '00'}]}},
        } for s in series],
    }
    cfg.update(_axes(x_label, y_label))
    return cfg

def mk_bar(x_label, y_label, series):
    cfg = {
        'backgroundColor': 'transparent',
        'textStyle': {'fontFamily': _MONO, 'color': _T},
        'tooltip': {'trigger': 'axis', 'backgroundColor': '#B0A49B', 'borderColor': _G,
                    'textStyle': {'color': '#696969', 'fontFamily': _MONO, 'fontSize': 11}},
        'legend': {'data': [s['name'] for s in series],
                   'textStyle': {'color': _T, 'fontFamily': _MONO, 'fontSize': 10},
                   'top': 0, 'right': 4},
        'grid': {'top': 28, 'right': 16, 'bottom': 24, 'left': 50},
        'series': [{
            'name': s['name'], 'type': 'bar', 'data': None, 'barMaxWidth': 36,
            'itemStyle': {'color': {'type': 'linear', 'x': 0, 'y': 0, 'x2': 0, 'y2': 1,
                'colorStops': [{'offset': 0, 'color': s['color']}, {'offset': 1, 'color': s['color'] + '55'}]},
                'borderRadius': [4, 4, 0, 0]},
        } for s in series],
    }
    cfg.update(_axes(x_label, y_label))
    return cfg


# ═══════════════════════════════════════════════════════════════════════════════
#  HEADER
# ═══════════════════════════════════════════════════════════════════════════════

with ui.header().classes('items-center justify-between').style('padding: 0 20px; height: 50px;'):
    with ui.row().classes('items-center gap-2'):
        ui.icon('water_drop').style('color: #B0A49B; font-size: 20px;')
        ui.label('Dam Simulation FrontEnd').style(
            'font-family: DM Sans; font-weight: 700; font-size: 1.1rem; color: #B0A49B;')

    with ui.row().classes('items-center gap-2'):
        ui.button('Save Parameters', icon='save_alt', on_click=lambda: saveParameters()) \
            .classes('btn-save').props('flat no-caps')
        ui.button('Launch', icon='play_arrow', on_click=lambda: launch_simulation()) \
            .classes('btn-launch').props('no-caps')


# ═══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR  — ui.left_drawer() handles its own height & scroll natively
# ═══════════════════════════════════════════════════════════════════════════════

def _sec(icon, label):
    ui.html(f'<div class="sct"><span class="material-icons">{icon}</span>{label}</div>')

def _inp(label, value):
    return ui.input(label, value=str(value)).props('outlined dense').classes('w-full')

with ui.left_drawer(value=True, fixed=True, bordered=False).style(
    'width: 268px; padding: 14px 12px; overflow-y: auto;'
):
    _sec('tune', 'Simulation')
    pBehaviorSelector   = ui.select(['Random', 'Yield Optimization', 'Electricity Optimization'], value='Random').props('outlined dense label="Behavior Selector"').classes('w-full').tooltip('[Int] - 0 : Random | 1 : Yield Maximization | 2 : Electricity Maximization')
    pSimulationDuration = _inp('Simulation Duration', m.sf.SimulationDuration).tooltip('[Int] - Duration of the simulation in minutes')
    pPlayerPriceTolerance = _inp('Price Tolerance', m.sf.PlayerPriceTolerance).tooltip('[Int] [0, 1] - If the player possesses PriceTolerance% of the price for a module, they will eco for it.')

    _sec('water', 'Lac')
    pWaterSupply    = _inp('Water Supply',     m.sf.WaterSupply).tooltip('[Float] - The initial water quantity in the lake')
    pMaxWaterSupply = _inp('Water Supply Cap', m.sf.MaxWaterSupply).tooltip('[Float] - The maximum water quantity in the lake')
    pWaterRegen     = _inp('Water Replenishing Rate',      m.sf.WaterRegen).tooltip('[Float] - The quantity of water replinishing each second')

    _sec('bolt', 'Barrage')
    pCurrentElectricity     = _inp('Current Electricity',  m.sf.CurrentElectricity).tooltip('[Float] - Defines the start value of electricity')
    pInitialSectionLength   = _inp('Initial Section Length',       m.sf.InitialSectionLength).tooltip('[Int] - Initial size of a section')
    pSpotPrices             = _inp('Spot Prices',          m.sf.SpotPrices).tooltip('[List Int] - Defines the price of each new spot')
    pSpotCityLevels         = _inp('Spot City Levels',     m.sf.SpotCityLevels).tooltip('[List Int] - Defines the city level required to unlock a spot')
    pBoostElectricityOutput = _inp('Boost Electricity Output',   m.sf.BoostElectricityOutput).tooltip('[Float] - Multiply the electricity production')
    pBoostWaterConsumption  = _inp('Boost Water Consumption',    m.sf.BoostWaterConsumption).tooltip('[Float] - Multiply the water consumption')

    _sec('location_city', 'Ville')
    pCurrentNeeds = _inp('Current Needs', m.sf.CurrentNeeds).tooltip('[Float] - Defines the start value of the needs')
    pTargetNeeds  = _inp('Target Needs',  m.sf.TargetNeeds).tooltip('[Float] - Defines the target value for the needs at Target Time')
    pTargetTime   = _inp('Target Time',   m.sf.TargetTime).tooltip('[Float] - Defines the Target Time')
    pSpeedCoeffA  = _inp('Speed Coeff A', m.sf.SpeedCoeffA).tooltip('[Float] - Defines the slope at the beginning')
    pSpeedCoeffB  = _inp('Speed Coeff B', m.sf.SpeedCoeffB).tooltip('[Float] - Defines the slope at the end')

    _sec('biotech', 'Recherche')
    pDistance        = _inp('Time To Complete Research',  m.sf.distance).tooltip('[Float] - Time to complete a Research')
    pDropRate        = _inp('Drop Rate', m.sf.dropRate).tooltip('[List Float] - Drop rate for each of module per city level [Px, Px-1, Px-2]')
    pSpeedCityLevel  = _inp('Speed',     m.sf.speedCityLevel).tooltip('[List Float] - Research speed per city level')
    pEachPriceInvest = _inp('Invest',    m.sf.eachPriceInvest).tooltip('[List Float] - Price for each research')


# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE CONTENT  — tabs + charts fill the page height automatically
# ═══════════════════════════════════════════════════════════════════════════════

with ui.tabs().props('align=left active-color=696969 indicator-color=696969').classes('w-full') as tabs:
    tab_elec   = ui.tab('elec',   label='Électricité & Ville', icon='bolt')
    tab_water  = ui.tab('water',  label='Barrage & Eau',        icon='water_drop')
    tab_search = ui.tab('search', label='Recherche',            icon='biotech')
    tab_game   = ui.tab('game',   label='Phases de Jeu',        icon='sports_esports')

with ui.tab_panels(tabs, value=tab_elec).classes('w-full'):

    # ── Tab 1 ────────────────────────────────────────────────────────────────
    with ui.tab_panel(tab_elec):
        with ui.element('div').classes('chart-grid'):
            with ui.element('div').classes('chart-card'):
                ui.html('<div class="chart-title">Électricité & Besoins</div>')
                gElec = ui.echart(mk_line('Temps (s)', 'Énergie (W)', [
                    {'name': 'Électricité', 'color': '#d6da14'},
                    {'name': 'Besoins',     'color': '#e03030'},
                ])).classes('w-full')

            with ui.element('div').classes('chart-card'):
                ui.html('<div class="chart-title">Niveau de Ville</div>')
                gCityLevelTime = ui.echart(mk_line('Temps (s)', 'Niveau', [
                    {'name': 'Niveau', 'color': '#8b5cf6'},
                ])).classes('w-full')

            with ui.element('div').classes('chart-card'):
                ui.html('<div class="chart-title">Durées par Niveau</div>')
                gCityLevelDuration = ui.echart(mk_bar('Niveau', 'Durée (s)', [
                    {'name': 'Durée', 'color': '#8b5cf6'},
                ])).classes('w-full')

    # ── Tab 2 ────────────────────────────────────────────────────────────────
    with ui.tab_panel(tab_water):
        with ui.element('div').classes('chart-grid'):
            with ui.element('div').classes('chart-card'):
                ui.html('<div class="chart-title">Réserve en Eau</div>')
                gWaterSupply = ui.echart(mk_line('Temps (s)', 'Eau', [
                    {'name': 'Réserve', 'color': '#00b4d8'},
                ])).classes('w-full')

            with ui.element('div').classes('chart-card'):
                ui.html("<div class='chart-title'>Consommation d'Eau</div>")
                gWaterConsumption = ui.echart(mk_line('Temps (s)', 'Eau', [
                    {'name': 'Consommation', 'color': '#0077a8'},
                ])).classes('w-full')

    # ── Tab 3 ────────────────────────────────────────────────────────────────
    with ui.tab_panel(tab_search):
        with ui.element('div').classes('chart-grid'):
            with ui.element('div').classes('chart-card'):
                ui.html('<div class="chart-title">Recherche & Vitesse</div>')
                gSearch = ui.echart(mk_line('Temps (s)', 'Valeur', [
                    {'name': 'Recherche', 'color': '#7300bb'},
                    {'name': 'Vitesse',   'color': '#e03030'},
                ])).classes('w-full')

    # ── Tab 4 ────────────────────────────────────────────────────────────────
    with ui.tab_panel(tab_game):
        with ui.element('div').classes('chart-grid'):
            with ui.element('div').classes('chart-card'):
                ui.html('<div class="chart-title">Durée des Phases</div>')
                gGamePhaseDuration = ui.echart(mk_bar('Phase', 'Durée (s)', [
                    {'name': 'Phase', 'color': '#00d4a0'},
                ])).classes('w-full')


# ═══════════════════════════════════════════════════════════════════════════════
#  ACTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def saveParameters():
    params = {
        'BehaviorSelector':       pBehaviorSelector.value,
        'SimulationDuration':     int(pSimulationDuration.value),
        'PlayerPriceTolerance':   float(pPlayerPriceTolerance.value),
        'WaterSupply':            float(pWaterSupply.value),
        'MaxWaterSupply':         float(pMaxWaterSupply.value),
        'WaterRegen':             float(pWaterRegen.value),
        'CurrentElectricity':     float(pCurrentElectricity.value),
        'InitialSectionLength':   float(pInitialSectionLength.value),
        'SpotPrices':             ast.literal_eval(pSpotPrices.value),
        'SpotCityLevels':         ast.literal_eval(pSpotCityLevels.value),
        'BoostElectricityOutput': float(pBoostElectricityOutput.value),
        'BoostWaterConsumption':  float(pBoostWaterConsumption.value),
        'CurrentNeeds':           float(pCurrentNeeds.value),
        'TargetNeeds':            float(pTargetNeeds.value),
        'TargetTime':             float(pTargetTime.value),
        'SpeedCoeffA':            float(pSpeedCoeffA.value),
        'SpeedCoeffB':            float(pSpeedCoeffB.value),
        'Distance':               float(pDistance.value),
        'DropRate':               ast.literal_eval(pDropRate.value),
        'SpeedCityLevel':         ast.literal_eval(pSpeedCityLevel.value),
        'EachPriceInvest':        ast.literal_eval(pEachPriceInvest.value),
    }
    with open('newParameters.json', 'w') as f:
        json.dump(params, f, indent=4)
    ui.notify('Paramètres sauvegardés', type='positive', timeout=2500)


def launch_simulation():
    loading_opts = {'text': 'Simulation...', 'textColor': '#7a9ab8', 'maskColor': 'rgba(7,12,20,.7)'}
    for chart in [gElec, gCityLevelTime, gSearch]:
        chart.run_chart_method('showLoading', loading_opts)

    try:
        subprocess.run(['python', 'launchSimulation.py'])
        ui.notify('Simulation terminée !', type='positive', timeout=3000)
    except FileNotFoundError:
        ui.notify('Erreur : fichier introuvable', type='negative', position='top-right')

    load_graph()

    for chart in [gElec, gCityLevelTime, gSearch]:
        chart.run_chart_method('hideLoading')


def load_graph():
    with open('data.json') as f:
        data = json.load(f)

    SimTimes   = data['SimulationTimes']
    CityLevels = data['CityLevelsData']
    Elec       = data['ElectricityOverTimeData']
    Needs      = data['NeedsOverTimeData']
    Search     = data['SearchOverTime']
    Water      = data['WaterOverTime']
    CLTimes    = data['CityLevelsTimes']
    GPTimes    = data['GamePhasesTimes']

    # Tab 1
    gElec.options['xAxis']['data']         = Elec['Time']
    gElec.options['series'][0]['data']     = Elec['Electricity']
    gElec.options['series'][1]['data']     = Needs['Needs']

    gCityLevelTime.options['xAxis']['data']     = CityLevels['Time']
    gCityLevelTime.options['series'][0]['data'] = CityLevels['Level']

    CLTimes.append(SimTimes[-1])
    durations = ComputeDurationsFromTimes(CLTimes)
    gCityLevelDuration.options['xAxis']['data']     = list(range(1, len(durations) + 1))
    gCityLevelDuration.options['series'][0]['data'] = durations

    # Tab 2
    gWaterSupply.options['xAxis']['data']         = Water['Time']
    gWaterSupply.options['series'][0]['data']      = Water['WaterSupply']
    gWaterConsumption.options['xAxis']['data']     = Water['Time']
    gWaterConsumption.options['series'][0]['data'] = Water['WaterConsumption']

    # Tab 3
    gSearch.options['xAxis']['data']       = Search['Time']
    gSearch.options['series'][0]['data']   = Search['Search']
    gSearch.options['series'][1]['data']   = Search['Speed']

    # Tab 4
    GPTimes.append(SimTimes[-1])
    gp_durations = ComputeDurationsFromTimes(GPTimes)
    gGamePhaseDuration.options['xAxis']['data']     = list(range(len(gp_durations)))
    gGamePhaseDuration.options['series'][0]['data'] = gp_durations

    for chart in [gElec, gCityLevelTime, gCityLevelDuration,
                  gWaterSupply, gWaterConsumption, gSearch, gGamePhaseDuration]:
        chart.update()


ui.run(title='Simulation', dark=True)