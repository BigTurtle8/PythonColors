class Colors:

    def __init__(self):
        self.start = '\033['
        self.style = {'none': '0', 'bold': '1', 'italicize':  '3', 'underline': '4'}
        self.fg = {'none': '0', 'black': '30', 'red': ';31', 'green': ';32', 'yellow': ';33', 'blue': ';34',
                   'cyan': ';36', 'white': ';37', 'gray': ';90', 'bright_red': ';91',
                   'bright_green': ';92', 'bright_yellow': ';93', 'bright_cyan': ';96',
                   'bright_white': ';97'}
        self.bg = {'none': '', 'black': '40', 'red': ';41', 'green': ';42', 'yellow': ';43', 'blue': ';44',
                   'cyan': ';46', 'white': ';47', 'gray': ';100', 'bright_red': ';101',
                   'bright_green': ';102', 'bright_yellow': ';103', 'bright_cyan': ';106',
                   'bright_white': ';107'}
        self.text_end = 'm'
        self.end = '\033[0m'

    def set_color(self, text, style, fg, bg):
        new_text = self.start + self.style[style] + self.fg[fg] + \
                   self.bg[bg] + self.text_end + text + self.end
        return new_text


# \033[style; text color; background color
# Make sure not end it with a 0. Just don't include it. Make sure the last digit has an m.
# That is how you edit it.
# ***Uses ANSI escapes.***
# In the wiki page for ANSI, there are two different columns for FG (Foreground/Text) and BG (Background).
c = Colors()


def example():
    print(c.start + c.style['none'] + c.fg['black'] + c.bg['none'] +
          c.text_end + 'Hello World!' + c.end)
    print(c.set_color('Hello World!', 'none', 'black', 'none'))


if __name__ == '__main__':
    example()
