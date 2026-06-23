#! /bin/sh

sudo -u tss /usr/bin/clevis-decrypt-tpm2 <$HOME/.config/gnome-keyring.tpm2 | /usr/bin/python3 $HOME/.local/bin/gnome-keyring-unlock.py
