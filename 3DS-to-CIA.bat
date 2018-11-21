@echo off
cls
title 3DS to CIA by tygamer
IF NOT EXIST BIN/boot9.bin echo HALTING, BOOT9.BIN NOT FOUND
IF NOT EXIST BIN/boot9.bin goto :stop
IF NOT EXIST 3DS/*.3ds ECHO NO GAMES/APPS FOUND, HALTING
IF NOT EXIST 3DS/*.3ds goto :stop
"BIN/3dsconv" --overwrite --boot9="BIN/boot9.bin" --output="CIA" "3DS/*.3ds"
:stop
echo Press any Key...
pause > nul
