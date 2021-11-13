#! /bin/bash

nitrogen --restore &
xrandr --output "eDP1"  --right-of "HDMI2" &
/bin/emacs  --daemon &
guake &
