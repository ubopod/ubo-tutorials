from ubo_app.store import dispatch
from ubo_app.store.services.voice import VoiceReadTextAction

from ubo_gui.menu.types import HeadlessMenu, SubMenuItem, ActionItem
from ubo_app.utils.qrcode import qrcode_input
from ubo_app.utils.async_ import create_task

def action():
    async def act():
        result, _ = await qrcode_input(pattern='.*',
                        prompt='Show QR Code to Scan',
                        extra_information='Go to qrcode.sassanh.com to enter text to craete qrcode',
                        title='Scan QR Code'
                        )
        dispatch(VoiceReadTextAction(text=result))
    create_task(act())

scan_qrcode = ActionItem(
    label='Scan',
    icon='󰁲',
    action=action
)
qrcode_menu = HeadlessMenu(
    title='󰐲 QR Code',
    items=[
        scan_qrcode,
    ],
)
qrcode_demo = SubMenuItem(
    label='QR Code Demo',
    icon='󰐲',
    sub_menu=qrcode_menu,
)