#!/usr/bin/env bash

if [ "$#" -eq "0" ]; then
    echo "Brak parametrów funkcji."
    echo "bash make_link.sh folder library.py"
    exit
fi

if [ "$1" = "--help" ]; then
    echo "Funkcja tworzy link do zadanego folderu z zadanego pliku."
    echo "bash make_link.sh folder library.py"
    echo "Np:"
    echo "bash make_link.sh L1 aplhastable.py"
    exit
fi

if [ "$0" = "make_link.sh" ]; then
    ln `echo $2` ../`echo $1`/`echo $2`
    exit
fi

ln packages/`echo $2` `echo $1`/`echo $2`
