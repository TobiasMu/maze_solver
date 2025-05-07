from elements import Point, Line
class Cell:
    def __init__(self,win=None):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_right_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.center = None
        self._win = win
        self.visited = False

    def draw(self, x1,y1,x2,y2):
        self.center={"x": (x1+x2)/2,
                     "y": (y1+y2)/2}
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        top_left = Point(self._x1,self._y1)
        top_right = Point(self._x2,self._y1)
        bottom_left = Point(self._x1,self._y2)
        bottom_right = Point(self._x2,self._y2)
        top_line = Line(Point(self._x1,self._y1), Point(self._x2, self._y1))
        bottom_line = Line(Point(self._x1,self._y2), Point(self._x2, self._y2))
        left_line= Line(Point(self._x1,self._y1), Point(self._x1, self._y2))
        right_line = Line(Point(self._x2,self._y1), Point(self._x2, self._y2))
        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(top_left, top_right)
            self._win.draw_line(line) 
        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(bottom_right, bottom_left)
            self._win.draw_line(line)

    def remove_lines(self):
        if self.center ==None:
            return
        top_line = Line(Point(self._x1,self._y1), Point(self._x2, self._y1))
        bottom_line = Line(Point(self._x1,self._y2), Point(self._x2, self._y2))
        left_line= Line(Point(self._x1,self._y1), Point(self._x1, self._y2))
        right_line = Line(Point(self._x2,self._y1), Point(self._x2, self._y2))
        if not self.has_left_wall:
            self._win.draw_line(left_line, "white")
        if not self.has_top_wall:
            self._win.draw_line(top_line, "white")
        if not self.has_right_wall:
            self._win.draw_line(right_line, "white")
        if not self.has_bottom_wall:
            self._win.draw_line(bottom_line, "white")



    def draw_move(self, to_cell, undo=False):
        centerpoint = Point(self.center["x"], self.center["y"])
        to_cell_center = Point(to_cell.center["x"], to_cell.center["y"])
        line = Line(centerpoint, to_cell_center)
        if undo:
            self._win.draw_line(line, color="gray")
        if not undo:
            self._win.draw_line(line, color="red")
    def __str__(self):

        return f"{self.has_left_wall},{self.has_bottom_wall}, {self.has_top_wall}, {self.has_right_wall}" 




