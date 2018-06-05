class Baseline:
    def __init__(self, data: bytes):
        self._header = data

    def rows(self):
        return self._rows
