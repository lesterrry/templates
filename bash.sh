#!/bin/bash
#
# Handcrafted by Aydar N.
# 2022
#
# me@aydar.media
#

# Argument number check
if [ "$#" -ne 1 ]; then
        echo "Illegal number of arguments. Expected 'SERVICE NAME'"
        exit
fi

# Sudo check
if [[ ! "$EUID" = 0 ]]; then
        echo "Sudo is required."
        exit
fi

# Input read
read input

# String comparison
if [[ "$s1" == "$s2" ]]; then

fi

# Confirmation
read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1