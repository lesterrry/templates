#!/bin/bash
if [ "$#" -ne 1 ]; then
        echo "Illegal number of arguments. Expected 'SERVICE NAME'"
        exit
fi
if [[ ! "$EUID" = 0 ]]; then
        echo "Sudo is required."
        exit
fi
