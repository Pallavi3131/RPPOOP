from random import random
import numpy as np


class Matrix():

    def matrices(self):
        self.__flag = 1
        print("********* MATRIX CALCULATOR *********")
        print("Please enter details for 1st matrix!")

        row1 = int(input("Enter the Number of rows : "))
        self.__row1 = row1
        col1 = int(input("Enter the numbers of the columns : "))
        self.__col1 = col1

        self.__m1 = np.random.randint(0, 50, (self.__row1, self.__col1))
        print("Matrix 1 : \n", self.__m1)

        print("Please enter details for 2nd matrix: ")
        row2 = int(input("Enter the number of rows : "))
        self.__row2 = row2
        col2 = int(input("Enter the numbers of the columns : "))
        self.__col2 = col2

        self.__m2 = np.random.randint(0, 50, (self.__row2, self.__col2))
        print("Matrix 2 : \n", self.__m2)
        return self.__flag

    def addMatrix(self):

        if self.__row1 == self.__row2:
            print(np.add(self.__m1, self.__m2), "\n")
        else:
            print("Number of rows must be same in the matrices for addition operation!!")

    def mulMatrix(self):

        if self.__col1 == self.__row2:
            print(np.multiply(self.__m1, self.__m2), "\n")
        else:
            print(
                "Number of columns in first matrix and number of rows of second matrix should be same for matrix multiplication !!")

    def subMatrix(self):

        if self.__row1 == self.__row2:
            print(np.subtract(self.__m1, self.__m2), "\n")
        else:
            print("Number of rows must be same in the matrices for subtraction operation!!")

    def divMatrix(self):
        if self.__row1 == self.__row2:
            print(np.divide(self.__m1, self.__m2), "\n")

    def transpose_mat(self):
        choice = eval(input("1.Transpose of M1\n2.Transpose of M2\n"))
        if (choice == 1):
            print("The transpose of matrix 1 is:")
            print(np.transpose(self.__m1), "\n")
        if (choice == 2):
            print("The transpose of matrix 2 is:")
            print(np.transpose(self.__m2), "\n")


matrix = Matrix()
if (matrix.matrices()):
    while True:
        print(
            "******** OPERATIONS ********\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Transpose of matrix1 \n6.exit")
        op = int(input("Enter the Choice : "))
        if op == 1:
            print("The addition of matrix is:")
            matrix.addMatrix()
        elif op == 2:
            print("The substraction of matrix is:")
            matrix.subMatrix()
        elif op == 3:
            print("The Multiplication of matrix is:")
            matrix.mulMatrix()
        elif op == 4:
            print("The division of matrix is:")
            matrix.divMatrix()
        elif op == 5:
            matrix.transpose_mat()
        elif op == 6:
            break;
        else:
            print("Invalid choice!!")


