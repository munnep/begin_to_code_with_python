class Prop:
@property
def x(self):
    print('property x get')
    return self.__x
    @x.setter
    def x(self,x):
    print('property x set:', x)
    self.__x = x

