from ubo_app.store import dispatch
from ubo_gui.menu.types import HeadlessMenu, SubMenuItem, ActionItem
from ubo_app.store.services.rgb_ring import (
        RgbRingRainbowAction, 
        RgbRingPulseAction, 
        RgbRingSpinningWheelAction,
    )

rainbow_action = ActionItem(
    label='Rain Bow',
    icon='󰜨',
    action=lambda: dispatch(RgbRingRainbowAction(rounds=15, wait=5)),
)
pulse_action = ActionItem(
    label='Pulse Red',
    icon='\uf469',
    action=lambda: dispatch(RgbRingPulseAction(color=(250,0,0),repetitions=10, wait=100)),
)
progress_wheel_action = ActionItem(
    label='Spinnig Wheel',
    icon='\uf110',
    action=lambda: dispatch(RgbRingSpinningWheelAction(color=(255,255,255),wait=20,length=2,repetitions=10)),
)
led_menu = HeadlessMenu(
    title='󰞏 LED Patterns',
    items=[
        rainbow_action,
        pulse_action,
        progress_wheel_action,
    ],
)
led_demo = SubMenuItem(
        label='LED Demo',
        icon='󰞏',
        sub_menu=led_menu,
    )