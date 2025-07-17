#!/bin/sh
#
function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}
PATH="$HOME/.config/qtile/scripts:$PATH"
# dimension wide
xrandr --output DP-1 --off --output HDMI-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP-2 --off --output DP-3 --off
picom &
#feh --bg-fill $HOME/Imágenes/background/km_background.png
# start all this to entry the system
sxhkd -c $HOME/.config/qtile/sxhkdrc &
dunst -config "$HOME"/.config/qtile/dunstrc &
# xss-lock -- i3lockmore -n --image-fill $HOME/Imágenes/background/surreal_art_by_thenumberoneai_dgfi3bl-fullview.jpg &
#run variety &
run nitrogen &
run nm-applet &
run blueman-applet &
run pamac-tray &
# run xfce4-power-manager &
numlockx on &
udiskie -t &
# run volumeicon &
blueman-applet &
kitty &
# alacritty &
parcellite &
# knotes &
# setxkbmap latam

