from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ubo_app.services import register
    
def setup():
    from ubo_app.store import dispatch
    from ubo_app.store.main import RegisterRegularAppAction    
    from ubo_gui.menu.types import HeadlessMenu, SubMenuItem
    from led_demo import led_demo
    from qrcode_demo import qrcode_demo
    from sound_demo import sound_demo

    all_demo_services = HeadlessMenu(
        title='󰙨Demos',
        items=[
            led_demo, #is a sub menu
            sound_demo,
            qrcode_demo,
        ],
    )
    demo_service = SubMenuItem(
        label='Demos',
        icon='󰙨',
        sub_menu=all_demo_services,
    )
    dispatch(RegisterRegularAppAction(menu_item=demo_service))

register(
    service_id='demo_srv',
    label='demo',
    setup=setup,
)
