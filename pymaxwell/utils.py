from cStringIO import StringIO


class StringBuilder:
    _my_string = None

    def __init__(self):
            self._my_string = StringIO()

    def append(self, str):
        self._my_string.write(str)

    def __str__(self):
        return self._my_string.getvalue()