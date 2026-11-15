#!/usr/bin/env bash

# Terminate already running bar instances
# If all your bars have ipc enabled, you can use 
# polybar-msg cmd quit
# Otherwise you can use the nuclear option:
killall polybar
killall trayer

polybar

trayer --widthtype pixel --width 600 --height 52 --edge bottom --monitor 1 --transparent true --tint 0x282A2E --alpha 0 --padding 1000 --iconspacing 20
