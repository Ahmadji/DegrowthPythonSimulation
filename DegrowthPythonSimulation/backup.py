from nicegui import ui

# ═══════════════════════════════════════════════════════════════════════════════
#  MENU & TAB
# ═══════════════════════════════════════════════════════════════════════════════

from local_file_picker import local_file_picker

with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')

    with ui.tabs() as tabs:
        ui.tab('A')
        ui.tab('B')
        ui.tab('C')
    
    ui.space()

with ui.footer(value=False) as footer:
    ui.label('Footer')

with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    ui.label('Side menu')

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

with ui.tab_panels(tabs, value='A').classes('w-full'):
    with ui.tab_panel('A'):
        ui.label('Content of A')
    with ui.tab_panel('B'):
        ui.label('Content of B')
    with ui.tab_panel('C'):
        ui.label('Content of C')

# ═══════════════════════════════════════════════════════════════════════════════
#  LOOK FILE PICKER 
# ═══════════════════════════════════════════════════════════════════════════════

async def pick_file() -> None:
    result = await local_file_picker('~', multiple=True)
    ui.notify(f'You chose {result}')


@ui.page('/')
def index():
    ui.button('Choose file', on_click=pick_file, icon='folder')

# ═══════════════════════════════════════════════════════════════════════════════
#  UPDATE GRAPH 
# ═══════════════════════════════════════════════════════════════════════════════

echart = ui.echart({
                'xAxis': {'type': 'category'},
                'yAxis': {'type': 'value'},
                'series': [{'type': 'line', 'data': [150, 230, 224, 218, 135]}],
                })

def update():
    echart.options['series'][0]['data'] = [50, 30, 75, 30, 90]

ui.button('Update', on_click=update)