#!/bin/bash
sudo wget https://raw.githubusercontent.com/KremowkaFFV/Israel/main/Israel_app -O /opt/Israel_app #ogólna paka
sudo wget https://raw.githubusercontent.com/KremowkaFFV/Israel/main/Uninstall_Israel.sh -O /usr/local/bin/Uninstall_Israel.sh && sudo chmod +x /usr/local/bin/Uninstall_Israel.sh #uninstall paczka
sudo wget https://raw.githubusercontent.com/KremowkaFFV/Israel/main/Israel.desktop -O /usr/share/applications/Israel.desktop && sudo chmod +x /usr/share/applications/Israel.desktop
sudo apt update && sudo apt install -y python3-tk python3-pil python3-pil.imagetk python3-pygame
echo "all is done!"
