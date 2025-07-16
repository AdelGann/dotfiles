from libqtile.config import Group, Match, Key
from libqtile.lazy import lazy
from .keys import mod, keys
from .layouts import layouts_maxtowide, layouts
import re

__groups = {
    1: Group(
        " 1 ",
        layout="max",
        layouts=layouts,
        matches=[
            Match(
                wm_class=re.compile(
                    r"^(qutebrowser|Navigator|Firefox|Vivaldi\-stable|Vivaldi\-snapshot|Chromium|Google\-chrome|Brave|Brave\-browser|navigator|firefox|vivaldi\-stable|vivaldi\-snapshot|chromium|google\-chrome|Google\-chrome|brave|brave\-browser|min|Min)$"
                )
            )
        ],
    ),
    2: Group(
        " 2 ",
        layout="tile",
        layouts=layouts,
        matches=[Match(wm_class=re.compile(r"^(Alacritty|kitty)$"))],
    ),
    3: Group(
        " 3 ",
        layout="max",
        layouts=layouts_maxtowide,
        matches=[Match(wm_class=re.compile(r"^(code\-oss|subl|code|Code)$"))],
    ),
    4: Group(
        " 4 ",
        layout="tile",
        layouts=layouts,
        matches=[Match(wm_class=re.compile(r"^(insomnia|Insomnia|postman|Postman)$"))],
    ),
    5: Group(
        " 5 ",
        layout="tile",
        layouts=layouts_maxtowide,
        matches=[
            Match(
                wm_class=re.compile(
                    r"^(docker\ desktop|Docker\ Desktop|github\ desktop|GitHub\ Desktop|DBeaver|DBeaver|beekeeper\-studio|GitAhead|dataflare|Dataflare)$"
                )
            )
        ],
    ),
    6: Group(
        " 6 ",
        layout="tile",
        layouts=layouts,
        matches=[
            Match(
                wm_class=re.compile(
                    r"^(Thunar|Nemo|Caja|Nautilus|org\.gnome\.Nautilus|Pcmanfm|Pcmanfm\-qt|thunar|nemo|caja|nautilus|org\.gnome\.nautilus|pcmanfm|pcmanfm\-qt|file\-roller|File\-roller)$"
                )
            )
        ],
    ),
    7: Group(
        " 7 ",
        layout="tile",
        layouts=layouts,
        matches=[Match(wm_class=re.compile(r"^(blender|Inkscape)$"))],
    ),
    8: Group(
        " 8 ",
        layout="max",
        layouts=layouts,
        matches=[
            Match(wm_class=re.compile(r"^(steam|game\.exe|mtga\.exe|spotify|Spotify)$"))
        ],
    ),
    9: Group(
        " 9 ",
        layout="max",
        layouts=layouts,
        matches=[
            Match(
                wm_class=re.compile(
                    r"^(qtpad|Notes|slack|Slack|notion\-app|notion\-app|telegram\-desktop|TelegramDesktop|whatsapp\-nativefier\-d40211|whatsapp\-nativefier\-d40211|franz|Franz|Mail|thunderbird|knotes|merkuro\-calendar|discord)$"
                )
            )
        ],
    ),
}
groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1+shift+letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )
