"""
Created on Sun Apr 19 15:21:58 2020

@author: Vishal
"""

import copy

import random

class Matrix4X4:
    
    def __init__(self, matrix):
        
        self.mat = copy.deepcopy(matrix)
        
        #Rows will be same its compatible with matrix returned from random_matrix
        self.rows = self.mat
        
        #columns are taken from rows with following iteration
        self.columns = [[i[j] for i in self.rows] for j in range(0, 4)]
        
        #subgrids 4X4
        sub_1 = [self.rows[0][0], self.rows[0][1],self.rows[1][0], self.rows[1][1]]
        sub_2 = [self.rows[0][2], self.rows[0][3],self.rows[1][2], self.rows[1][3]]
        sub_3 = [self.rows[2][0], self.rows[2][1],self.rows[3][0], self.rows[3][1]]
        sub_4 = [self.rows[2][2], self.rows[2][3],self.rows[3][2], self.rows[3][3]]
        
        self.submats = [sub_1, sub_2, sub_3, sub_4];
        
        
        
        
        
    
    def show(self):
        print('===solved_sudoku===')
        for i in self.rows:
            print(i)
            
            

def random_matrix(matrix, frequency):#This function is to generate the random matrix.
    y = copy.deepcopy(matrix)
    #deepcopy reflects the copy
    for i in range(0,frequency):
        x = int(random.uniform(0, len(matrix)))
        value = y.pop(x)
        y.append(value)
    shuffled_matrix = copy.deepcopy(y)
    return shuffled_matrix
    
    
def checking_condition(matrix):#This function checks the condition sudoku

    #For each rows columns and and sub blocks it checks the repitative elements if any present 
    
    check = [True, True, True]
    
    for i in matrix.rows:
        if len(set(i))!=4: #set removes the repitative elements
            check[0] = False
            break
        
        
    for i in matrix.columns:
        if len(set(i))!=4:
            check[1] = False
            break
        
        
    for i in matrix.submats:
        if len(set(i))!=4:
            check[2] = False
            break
        
    if False in check: # If all conditionssatisfy then only it returns true
        return False
    else:
        return True
        
        
        
#matrix passed is initial matrix
def sudoku_generate(matrix, frequency):
    store = list() # To store the intermediate results
    
    time = int(0)#to store the number of attempts
    
    while not checking_condition(matrix):
        
        #It means that If checking returns false thenthe following statements will get executed
        
        while (matrix.rows in store):
            #matrix is an object of class Matrix4 matrix.rows actully returns rows
            
            Mat = list()
            #to store the Intermedite random matrix
            for i in range(0, 4):
                Y= random_matrix(num, frequency)
                
                
                while Y in Mat :#To get unique matrix in matrix
                    Y = random_matrix(num, frequency)
                Mat.append(Y)
                
            matrix = Matrix4X4(Mat)#pass the randomly generated matrix to class Matrix4 as constuctor to the matrix
            
        store.append(copy.deepcopy(matrix.rows))
        #deepcopy helps to reflect the changes
        
        time += 1
        print(time)
    return matrix
    
    
    
    


if __name__ == "__main__": 
    
    frequency = 20
    Mat = list()
    num=[1,2,3,4]
    for i in range(0, 4):
        Y = random_matrix(num, frequency)
        Mat.append(Y)

    Matrix = Matrix4X4(Mat)
    
    sudoku_generate(Matrix, frequency).show()



