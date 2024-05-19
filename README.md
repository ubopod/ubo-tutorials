# Building Your First App

When designing Ubo pod and its software stack, we wanted to ensure that other developers can easily build their applications 
with system modules and libraries. 

# hello world

To begin developing on your Ubo pod, you need to first connect to it. We can do this easily with `ssh` or VScode Remote Tunnel which is offered out of the box. We recommend VScode Remote Tunnel since it allows you to take full advantage of VScode capabilities and allow remote access even if you are not on the same network. 

// we probably need to have a different document for remote access and link to it. 
To connect with VScode Remote Tunnel, go to your device `Settings`, choose `Remote` Option, and select VScode. Follow the steps to setup Remote Tunnel. Please note that even if you don't have VScode installed on your machine, you can run it in your browser.

Once you connect to your pod, open a terminal and following the steps below:

1. Make ubo_services directoty in ubo user's home:

``` sh
> sudo su ubo
> mkdir /ubo/home/ubo_services
> cd ubo/home/ubo_services
```

`ubo/home/ubo_services` is the default directory that hold custom services/apps. If you want to place your services somewhere else you can simply create a symlink to point to this directory.  

In our first example, we are going to write a simple service that create a `hello.txt` file in `/tmp/` and writes `hello world` line into it as soon as Ubo app loads. To do this, create `ubo_handle.py` file in ubo_services directory that the following content:

```
def setup():
    file_path = '/tmp/hello.txt'
    with open(file_path, 'w') as file:
        file.write("Hello World")

register(
    service_id='helloworld',
    label='helloworld',
    setup=setup,
)
```
This essentially defines the function that runs when the main app starts and registers it along with a `service_id` and `label`.

After you make this change, run the following command to kill and restart `ubo_app`:

```sh
> kill -9 ubo_app
```

After app restarts, you can check /tmp/hello.txt file content and see that "hello world" line was indeed written into the file.


## Start app manually

In previous example, the service automatically runs when Ubo app starts. In many cases, you may just want to initiate the service call with press of a button on the keypad. 

We are next going to modify the code to do that.

To do this we need into import several items inside `setup()` function.

``
from ubo_app.store.main import RegisterRegularAppAction
``

By using `RegisterRegularAppAction` we can register the action entry point inside `Settings->Apps` section of the Ubo app. If you want to add a service under `Settings` (instead of `Apps` section), you need to import and use  `RegisterSettingAppAction` instead.

```
from ubo_gui.menu.types import ActionItem
```

`ActionItem` is menu item that involves an action when pressed. By contrast, `SubMenuItem` open another level of menu that can hold `ActionItem` inside. We will dive deeper into arranging `Items` in later chapters.

`from ubo_app.store import dispatch`

`dispatch` dispatches an action over redux bus. In this example, this sends a signal to register action item under Apps section.

We can revise the previous example to putting these pieces together.

```
def setup():
    from ubo_app.store.main import RegisterRegularAppAction
    from ubo_app.store import dispatch
    from ubo_gui.menu.types import ActionItem
    helloworld_main_menu = ActionItem(
        label='helloworld',
        icon='[color=#008100]\ue007[/color]',
        action=lambda print,
    )
    dispatch(RegisterRegularAppAction(menu_item=helloworld_main_menu))

register(
    service_id='helloworld',
    label='helloworld',
    setup=setup,
)
```

`ActionItem` takes an icon argument. We decided to use [Nerd Font Icons](https://www.nerdfonts.com/cheat-sheet) due to large collection of icons. You can search their website and use the desired icon code in your app. You can also change the color and style of the icon and any other font in your code by using the [available text markups](https://kivy.org/doc/stable/api-kivy.core.text.markup.html) of Kivy.

### Debug

To debug your app, you can easily look at the logs by running:

```sh
tail -f /opt/ubo/ubo-app.log
```
