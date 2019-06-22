"""
    This module contains output display helper tools
"""
from terminaltables import AsciiTable


class TerminalDisplay:
    """
        Gives a readbale output format for variables and
        values on the commandline
    """

    def ouput(self, title='Output', **kwargs):
        """
            Gives a printable table-parameters object
        """
        disp = [kwargs.get('keys')]
        disp.append(kwargs.get('values'))
        print(AsciiTable([[title]]).table)
        print(AsciiTable(disp).table)


td = TerminalDisplay()
