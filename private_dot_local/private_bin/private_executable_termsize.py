#!/usr/bin/env python3

# Get the current size of the terminal window, and set stty size accordingly.
# A replacement for xterm's resize program, with no X dependency.
# Useful when logged in over a serial line.
# Modified by Patrick W. Healy to work better in Azure serial console, based on
# the original version by Akkana Peck.
# Copyright 2013,2017 by Akkana Peck. Share and enjoy under the GPL v2 or later.

import os, sys
import fcntl
import struct
import time
import re
import tty
import termios
import select

# Python3 needs extra flags set, which requires a 2-step open process:
fd = os.open('/dev/tty', os.O_RDWR|os.O_NOCTTY)
ttyfd = open(fd, 'wb+', buffering=0)

def get_terminal_size_noncurses():
    # The non-curses version works well under xterm, but in urxvt,
    # the terminal echoes back the rows and columns, but in a way
    # that makes it see those characters as input. I haven't
    # found a way around that.

    # Save the terminal state
    fileno = sys.stdin.fileno()
    stty_sav = termios.tcgetattr(sys.stdin)
    fc_sav = fcntl.fcntl(fileno, fcntl.F_GETFL)

    # Turn off echo.
    stty_new = termios.tcgetattr(sys.stdin)
    stty_new[3] = stty_new[3] & ~termios.ECHO
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, stty_new)

    ttyfd.write(b'\033[7\033[r\033[999;999H\033[6n')
    ttyfd.flush()

    # Put stdin into cbreak mode.
    # Python2 can use fd here, but in Python3 we have to get sys.stdin.fileno.
    tty.setcbreak(sys.stdin)

    # Nonblocking mode.
    fcntl.fcntl(fileno, fcntl.F_SETFL, fc_sav | os.O_NONBLOCK)

    try:
        while True:
            r, w, e = select.select([ttyfd], [], [])
            if r:
                output = sys.stdin.read()
                break
    finally:
        # Reset the terminal back to normal cooked mode
        termios.tcsetattr(fileno, termios.TCSAFLUSH, stty_sav)
        fcntl.fcntl(fileno, fcntl.F_SETFL, fc_sav)

    rows, cols = list(map(int, re.findall(r'\d+', output)))

    return rows, cols


if __name__ == '__main__':
    rows, cols = get_terminal_size_noncurses()

    fcntl.ioctl(ttyfd, termios.TIOCSWINSZ,
                struct.pack("HHHH", rows, cols, 0, 0))
    print("\nReset the terminal to %d rows, %d cols" % (rows, cols))
