#!/bin/bash

set -e



# fullname="USER INPUT"
read -p " a program telepíteni fog egy virtuális környezetet myenv néven. Folytatja a telepítést? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

python3 -m venv myenv
echo "Virtuális környezet létrehozva"
source myenv/bin/activate
echo "Sikeres belépés a virtuális környezetbe"
read -p "A program telepíteni fogja a 'flask' nevezetű libary-t. Folytatja a telepítést? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

pip3 install flask
clear
echo "Virtuális környezet létrehozva"
echo "Sikeres belépés a virtuális környezetbe"
echo "Python libary letöltve!"

echo "=======Csomagok verziói======="
python -m flask --version
echo "=============================="
echo ""
echo "============Fontos tudnivalók============"
echo "OLVASSA EL A README.MD-T"
echo "=========================================="
echo ""
echo "========Credit==========="
echo "Created by: Gyuris Dániel"
echo "========================="
