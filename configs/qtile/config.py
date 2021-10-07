import os
import subprocess
from typing import List  # noqa: F401

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

from text import str_formater_with_const_width

mod = "mod4"
terminal = "alacritty"
default_browser = "google-chrome-stable"

keys = [
    #### Basic
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #### Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    ##### Move windows
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    #### Apps
    Key([mod], "b", lazy.spawn(default_browser), desc="Google chrome"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    #    Key([mod], "r", lazy.spawncmd()desc="Spawn a command using a prompt widget",
    Key(
        [mod],
        "r",
        lazy.spawn("dmenu_run"),
        desc="Spawn a command using a prompt widget",
    ),
    Key(
        ["control", "shift"],
        "e",
        lazy.spawn("emacsclient -c -a emacs"),
        desc="Doom Emacs",
    ),
    KeyChord(
        [mod],
        "p",
        [
            Key(
                [], "e", lazy.spawn("dm-confedit"), desc="Choose a config file to edit"
            ),
            Key([], "q", lazy.spawn("dm-logout"), desc="Choose a config file to edit"),
        ],
    ),
    #### Resizing windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    #### Layouts
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    KeyChord(
        [mod],
        "o",
        [
            Key(
                [],
                "m",
                lazy.to_layout_index(1),
            ),
            Key(
                [],
                "b",
                lazy.to_layout_index(0),
            ),
        ],
    ),
    #### Monitors
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
]


class MyGroup(Group):
    def __init__(self, name: str, key: str, **kwargs):
        super().__init__(name, **kwargs)
        self.key = key


groups = [
    MyGroup(
        name="www",
        key="1",
        layout="max",
        matches=[Match(wm_class=["google-chrome", "Google-chrome"])],
    ),
    MyGroup(name="code", key="2", layout="max"),
    MyGroup(name="py", key="3", layout="max"),
    MyGroup(name="chat", key="4"),
    MyGroup(name="music", key="5", matches=[Match(wm_class=["spotify", "Spotify"])]),
    MyGroup(name="6", key="6"),
    MyGroup(name="7", key="7"),
    MyGroup(
        name="note",
        key="8",
        layout="max",
        matches=[Match(wm_class=["obsidian", "obsidian"])],
    ),
    MyGroup(
        name="todo",
        key="9",
        layout="max",
        matches=[Match(wm_class=["todoist", "Todoist"])],
    ),
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.key,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.key,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layout_theme = {
    "border_width": 2,
    "margin": 2,
    "border_focus": "e1acff",
    "border_normal": "1D2330",
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Floating(**layout_theme),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(fmt=str_formater_with_const_width()),
                widget.GroupBox(),
                widget.WindowName(),
                # widget.Prompt(),
                widget.Clock(format="%Y-%m-%d %a %H:%M"),
                widget.Battery(),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(fmt=str_formater_with_const_width()),
                widget.GroupBox(),
                widget.WindowName(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %H:%M"),
                widget.Battery(),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])
