#!/bin/bash

set -e




read -p "Elolvasta a 'read.md'-t. (I/N): " confirm && [[ $confirm == [iI] ]] || exit 1
read -p "a program telepíteni fogja a weboldalt a github-ról. Folytatja a telepítést? (I/N): " confirm && [[ $confirm == [iI] ]] || exit 1
git clone https://github.com/simsononroad/fullstack-website-wmtech-homework.git
read -p " a program telepíteni fog egy virtuális környezetet myenv néven. Folytatja a telepítést? (I/N): " confirm && [[ $confirm == [iI] ]] || exit 1

python3 -m venv myenv
echo "Virtuális környezet létrehozva"
source myenv/bin/activate
echo "Sikeres belépés a virtuális környezetbe"
read -p "A program telepíteni fogja a 'flask' nevezetű libary-t. Folytatja a telepítést? (I/N): " confirm && [[ $confirm == [iI] ]] || exit 1

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

read -p "Elindítja a weboldalt? (I/N): " confirm && [[ $confirm == [iI] ]] || exit 1
cd fullstack-website-wmtech-homework
python3 app.py