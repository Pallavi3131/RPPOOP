import time as t
from datetime import *


class Time:
    def __init__(self):
        print("Use characters only")
        self.__result = 0
        self.__startTime = 0
        self.__endTime = 0

    def test(self):
        start = input("Type enter to begin the test, ALL THE BEST!  : ")
        if (start == "enter" or "ENTER"):
            self.__startTime = t.time()
            self.__startDetail = datetime.now().strftime("%H:%M:%S")
            print("Which Language is a OOP language?")
            print("a.Python \nb.C \nc.C++ \nd.None of the above")
            ans = input("Ans:")
            if (ans == "a" or ans == "A"):
                self.__result += 1
            elif ans != "b" or ans != "B" or ans != "c" or ans != "C" or ans != "d" or ans != "D":
                self.__result -= 1

            print("What is the full form of OOP?")
            print("a.Object of Python \nb.Object oriented Programming \nc.Options of Python \nd.None of the above")
            ans = input("Ans:")
            if (ans == "b" or ans == "B"):
                self.__result += 1
            elif ans != "a" or ans != "A" or ans != "c" or ans != "C" or ans != "d" or ans != "D":
                self.__result -= 1

            print("Which of the following are Python data structures?")
            print("a.Set \nb.List \nc.All of them \nd.Tuple")
            ans = input("Ans:")
            if (ans == "c" or ans == "C"):
                self.__result += 1
            elif ans != "b" or ans != "B" or ans != "a" or ans != "A" or ans != "d" or ans != "D":
                self.__result -= 1

            print("Who uses python language?")
            print("a.IBM \nb.NASA \nc.NETFLIX \nd.All of them")
            ans = input("Ans:")
            if (ans == "d" or ans == "D"):
                self.__result += 1
            elif ans != "b" or ans != "B" or ans != "a" or ans != "A" or ans != "c" or ans != "C":
                self.__result -= 1
            self.__endTime = t.time()
            self.__endDetail = datetime.now().strftime("%H:%M:%S")
            print(
                f'Your Result = {self.__result} out of 4 marks,Well Done!\nYour Start Time = {self.__startDetail}\nYour End Time = {self.__endDetail}\nTotal Time Taken = {self.__endTime - self.__startTime} seconds')

        else:
            raise Exception("Invalid input to begin test")


time = Time()
time.test()
