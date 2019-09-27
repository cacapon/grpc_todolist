class GetCh():
    @staticmethod
    def getch():
        try:
            from msvcrt import getch
            return getch()
        except ImportError:
            import sys
            import tty
            import termios
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
