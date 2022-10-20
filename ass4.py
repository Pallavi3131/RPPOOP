from abc import ABC, abstractmethod
from math import sqrt


class Polygon(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Polygon):

    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def get_perimeter(self):
        if (self.__length == self.__breadth):
            print("Sides are equal! It's a Square!")
            print("Perimeter of square is:")
            print(2 * (self.__length + self.__breadth))
        else:
            print("It's a Rectangle!")
            print("Perimeter of Rectangle is:")
            print(2 * (self.__length + self.__breadth))

    def get_area(self):
        if (self.__length == self.__breadth):
            print("Area of given sqaure is:")
            print(self.__length * self.__breadth)
        else:
            print("Area of Rectangle is:")
            print(self.__length * self.__breadth);


class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        self.__s1 = side1
        self.__s2 = side2
        self.__s3 = side3

    def get_perimeter(self):
        if (
                self.__s1 < self.__s2 + self.__s3 and self.__s2 < self.__s3 + self.__s1 and self.__s3 < self.__s2 + self.__s1):
            if (self.__s1 == self.__s2 or self.__s2 == self.__s3 or self.__s3 == self.__s1):
                if (self.__s1 == self.__s2 == self.__s3):
                    print("It's a equilateral triangle! ")
                    print("Perimeter of equilateral Triangle is:")
                    print(self.__s1 + self.__s2 + self.__s3)
                else:
                    print("It's a isoceles triangle! ")
                    print("Perimeter of isoceles Triangle:")
                    print(self.__s1 + self.__s2 + self.__s3)
            else:
                print("It's a scalene triangle! ")
                print("Perimeter of scalene Triangle:")
                print(self.__s1 + self.__s2 + self.__s3)
        else:
            print("Lengths of side are invaid. Hence, Triangle cannot be formed.")

    def get_area(self):
        if (
                self.__s1 < self.__s2 + self.__s3 and self.__s2 < self.__s3 + self.__s1 and self.__s3 < self.__s2 + self.__s1):
            s = (self.__s1 + self.__s2 + self.__s3) / 2
            if (self.__s1 == self.__s2 or self.__s2 == self.__s3 or self.__s3 == self.__s1):
                if (self.__s1 == self.__s2 == self.__s3):
                    print("Area of equilateral Triangle is:")
                    print(sqrt(s * (s - self.__s1) * (s - self.__s2) * (s - self.__s3)))
                else:
                    print("Area of isoceles Triangle is:")
                    print(sqrt(s * (s - self.__s1) * (s - self.__s2) * (s - self.__s3)))
            else:
                print("Area of scalene Triangle:")
                print(sqrt(s * (s - self.__s1) * (s - self.__s2) * (s - self.__s3)))
                # s = (self.__s1 + self.__s2 + self.__s3 )/2

        else:
            print("Lengths of side are invaid. Hence, Triangle cannot be formed.")


while True:
    side = eval(input("\n\n enter 3 : For Triangle \n enter 4 : For Rectangle \n enter 5 : To Exit \n\n "))
    if side == 4:
        a = eval(input("enter side1 :"))
        b = eval(input("enter side2 :"))
        rect = Rectangle(a, b)
        rect.get_perimeter()
        rect.get_area()

    elif side == 3:
        a = eval(input("enter side1 :"))
        b = eval(input("enter side2 :"))
        c = eval(input("enter side3 :"))
        tri = Triangle(a, b, c)
        tri.get_perimeter()
        tri.get_area()

    elif side == 5:
        print("You have exited!")
        break