class pyramid():
    P_length = ''
    P_width = ''
    P_height = ''

    def cal(self):
        self. volume = (self.P_length.length *
                        self.P_width.width*self.P_height.height)
        return self.volume


class Base_length():
    length = ''


class Base_width():
    width = ''


class Pyramid_height():
    height = ''


height = myPyramid = pyramid()
myPyramid_length = Base_length()
myPyramid_width = Base_width()
myPyramid_height = Pyramid_height()

myPyramid_length. length = 10
myPyramid_width.width = 7
myPyramid_height .height = 17

myPyramid.P_length = myPyramid_length
myPyramid.P_width = myPyramid_width
myPyramid.P_height = myPyramid_height

print(myPyramid.cal())
