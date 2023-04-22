class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, n):
    self.width = abs(n)

  def set_height(self, n):
    self.height = abs(n)

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."

    line = "*" * self.width
    return self.height * (line + "\n")

  def get_amount_inside(self, shape):
    fit_width = self.width // shape.width
    fit_height = self.height // shape.height

    if (fit_width and fit_height):
      return fit_width * fit_height
    else:
      return 0

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)
    self.side = side

  def set_side(self, n):
    self.side = n
    super().set_width(self.side)
    super().set_height(self.side)

  def set_width(self, n):
    self.set_side(n)

  def set_height(self, n):
    self.set_side(n)

  def __str__(self):
    return f"Square(side={self.side})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
