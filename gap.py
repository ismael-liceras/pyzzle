class Gap():
    def __init__(self, factor):
        self.factor = factor
        self.current_position = self.original_position = factor * factor
        self.borders = [
            self.current_position - self.factor,
            self.current_position - 1
        ]

    def get_borders(self):
        return self.borders

    def set_current_position(self, position):
        self.current_position = position
        self.borders = []
        for n in (position - 1, position - self.factor):
            if n > 0:
                self.borders.append(n)
        for n in (position + 1, position + self.factor):
            if n <= (self.factor * self.factor):
                self.borders.append(n)

