from ubo_app.store import dispatch
from ubo_gui.menu.types import HeadlessMenu, SubMenuItem, ActionItem
from ubo_app.store.services.notifications import Chime
from ubo_app.store.services.sound import SoundPlayChimeAction
from ubo_app.store.services.voice import VoiceReadTextAction

success_chime = ActionItem(
    label='Play Success',
    icon='',
    action=lambda: dispatch(SoundPlayChimeAction(name=Chime.DONE)),
)
failure_chime = ActionItem(
    label='Play Failure',
    icon='',
    action=lambda: dispatch(SoundPlayChimeAction(name=Chime.FAILURE)),
)
say_hello = ActionItem(
    label='Greetings',
    icon='󰙊',
    action=lambda: dispatch(VoiceReadTextAction(text='Hello there!')),
)
sound_menu = HeadlessMenu(
    title=' Sound Bites',
    items=[
        success_chime,
        failure_chime,
        say_hello,
    ],
)
sound_demo = SubMenuItem(
    label='Sound Demo',
    icon='',
    sub_menu=sound_menu,
)