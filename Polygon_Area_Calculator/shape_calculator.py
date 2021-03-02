class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        draw_rectangule = str()
        for i in range(self.height):
            for j in range(self.width):
                draw_rectangule += "*"
            draw_rectangule += "\n"
        return draw_rectangule

    def get_amount_inside(self, another_shape):
        amount_inside = int(self.get_area() / another_shape.get_area())
        return amount_inside

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def  set_height(self, height):
        self.set_side(height)
    
    def  set_width(self, width):
        self.set_side(width)

    def __str__(self):
        return f"Square(side={self.height})"


# * Testing
# rect = Rectangle(1, 1)
# sq = Square(5)

# rect.set_height(10)
# rect.set_width(15)
# actual = rect.get_amount_inside(sq)
# expected = 6
# #assertEqual(actual, expected, 'Expected `get_amount_inside` to return 6.')

# print(actual)
# print(expected)

# if actual == expected:
#     print("yeah")
# else:
#     print("NO")
