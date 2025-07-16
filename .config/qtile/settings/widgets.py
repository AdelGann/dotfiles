# from libqtile import widget
from qtile_extras import widget
from .theme import colors
from libqtile import bar
from libqtile import qtile
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.popup.templates.mpris2 import COMPACT_LAYOUT, DEFAULT_LAYOUT
# from qtile_extras.widget import GlobalMenu
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg="text", bg="background"):
    return {
        "foreground": colors[fg],
        "background": colors[bg],
    }


def separator():
    return widget.sep(**base(), linewidth=0, padding=5)


def spacer(length=bar.STRETCH):
    return widget.Spacer(length=length, background=colors["background"])


def icon(
    fg=colors["background"][0], bg="background", fontsize=16, text="?", decorations=[]
):
    return widget.TextBox(
        foreground=colors[fg],
        background=bg,
        fontsize=fontsize,
        text=text,
        padding=12,
        decorations=decorations,
    )


decor_group = {
    "decorations": [
        RectDecoration(colour=colors["background"], filled=True, group=True, radius=11),
    ],
}

decor_groupbox = {
    "decorations": [
        RectDecoration(
            colour=colors["background"],
            radius=11,
            filled=True,
        ),
    ],
    "padding": 18,
}


def workspaces():
    return [
        widget.GroupBox(
            #background="#00000000",
            font="FiraCode NF Bold",
            fontsize=12,
            margin_y=2,
            margin_x=10,
            padding_y=6,
            padding_x=0,
            borderwidth=1,
            active=colors["active"],
            inactive=colors["inactive"],
            rounded=True,
            highlight_method="text",
            urgent_alert_method="text",
            urgent_border=colors["urgent"],
            this_current_screen_border=colors["focus"],
            this_screen_border=colors["extra"],
            other_current_screen_border=colors["focus"],
            other_screen_border=colors["background"],
            disable_drag=True,
            #**decor_groupbox,
        ),
    ]


def text_funki(text):
    dsub = {
        "Google Chrome": "Google Chrome",
        "Firefox": "Firefox",
        "Visual Studio": "Visual Studio",
    }
    for sub in dsub:
        if sub in text:
            text = dsub[sub]
    return text


primary_widgets = [
    # widget.LaunchBar(
    #     default_icon="/home/krashmello/.config/qtile/assets/logo64x64_sakura_light.png",
    #     progs=[("rofy", "rofi -show drun")],
    #     padding=3,
    # ),
    # widget.WindowName(
    #     max_chars=50, format="{name} | ", scroll=True, width=450, parse_text=text_funki
    # ),
    spacer(length=50),
    widget.Visualiser(),
    widget.Mpris2(
        width=220,
        popup_layout=DEFAULT_LAYOUT,
        scroll=True,
        scroll_step=2,
        scroll_interval=0.1,
        format="{xesam:title}{% if xesam:artist %} - {xesam:artist}{% endif %}"
    ),
    spacer(),
    *workspaces(),
     widget.Clock(
        **base(),
        format=" %d/%m/%Y  %I:%M %p ",
    ),
    widget.Notify(),
    spacer(),
    widget.CheckUpdates(
        distro="Fedora",
        display_format=" {updates} updates",
        no_update_string=" Up to date",
        colour_have_updates=colors["focus"],
        colour_no_updates=colors["active"],
        update_interval=1800,
    ),
    spacer(length=10),
    widget.Systray(**base()),
    spacer(length=10),
    widget.CPU(
        **base(bg="background", fg="text"),
        fontsize=14,
        format="{load_percent}% ",
        max_chars=5,
    ),
    spacer(length=5),
    # icon(bg=colors["background"], fg="icon", fontsize=14, text=" ", **decor_group),
     widget.Memory(
        **base(bg="background", fg="text"),
        fontsize=14,
        format="{MemUsed: .0f}{mm} ",
    ),
    # widget.ThermalSensor(
    #     tag_sensor="Package id 0",
    #     threshold=75,
    #     foreground_alert=colors["urgent"],
    #     foreground=colors["text"],
    #     background=colors["background"],
    #     fmt=" {}",
    # ),
    spacer(length=5),
    widget.ThermalSensor(),
    spacer(length=5),
    widget.Net(
        format="{down} ↓↑ {up}",
        foreground=colors["text"],
        background=colors["background"],
    ),
    spacer(length=5),
    widget.IWD(show_image=True, show_text=False, **base(), padding=5),
    spacer(length=50)
    # widget.UPowerWidget(
    #     border_colour=colors["focus"],
    #     fill_colour=colors["active"],
    #     background=colors["background"],
    #     font="FiraCode NF Bold",
    # ),
]

# secondary_widgets = [
#     widget.LaunchBar(
#         default_icon="/home/krashmello/.config/qtile/assets/logo64x64_sakura_light.png",
#         progs=[("rofy", "rofi -show drun")],
#         padding=5,
#     ),
#     spacer(length=15),
#     *workspaces(),
#     spacer(),
#     icon(bg="#00000000", fg="icon", fontsize=14, text=" ", **decor_group),
#     widget.CPU(
#         **base(bg="background", fg="text"),
#         fontsize=14,
#         format="{load_percent}% ",
#         max_chars=5,
#         **decor_group,
#     ),
#     icon(bg="#00000000", fg="icon", fontsize=14, text=" ", **decor_group),
#     widget.Memory(
#         **base(bg="background", fg="text"),
#         fontsize=14,
#         format="{MemUsed: .0f}{mm} ",
#         **decor_group,
#     ),
#     icon(bg="#00000000", fg="icon", fontsize=14, text=" ", **decor_group),
#     widget.Clock(
#         background="#00000000",
#         foreground=colors["text"],
#         fontsize=14,
#         format="%d/%m/%Y ",
#         **decor_group,
#     ),
#     icon(bg="#00000000", fg="icon", fontsize=14, text=" ", **decor_group),
#     widget.Clock(
#         background="#00000000",
#         foreground=colors["text"],
#         format="%I:%M %p ",
#         **decor_group,
#     ),
#     widget.Systray(background="#00000000", foreground=colors["text"]),
# ]


widget_defaults = {
    "font": "GohuFont 11 Nerd Font Bold",
    "fontsize": 14,
    "padding": 1,
}
extension_defaults = widget_defaults.copy()
