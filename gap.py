class Gap():
    def __init__(self, factor):
        self.factor = factor
        self.current_position = self.original_position = (factor, factor)

    def set_current_position(self, position):
        self.current_position = position

    def get_current_position(self):
        return self.current_position

    def get_borders(self):
        ret = []
        if self.current_position[0] - 1 > 0:
            ret.append((self.current_position[0] - 1, self.current_position[1]))
        if self.current_position[0] + 1 > self.factor:
            ret.append((self.current_position[0] + 1, self.current_position[1]))
        if self.current_position[1] - 1 > 0:
            ret.append((self.current_position[0], self.current_position[1] - 1))
        if self.current_position[1] + 1 > self.factor:
            ret.append((self.current_position[0], self.current_position[1] + 1))
        return ret

    def get_distance_to_position(self, position):
        return self.current_position[0] - position[0], self.current_position[1] - position[1]

