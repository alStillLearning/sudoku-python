import numpy as np
import random 

myArray = np.array([
    [3,5,7,1,2,3,4,5,2],
    [1,2,3,2,4,1,2,3,4],
    [7,8,2,3,4,5,6,7,9],
    [4,3,1,2,1,6,7,8,4],
    [1,2,3,4,5,6,7,8,9],
    [2,1,3,4,5,6,7,8,9],
    [3,1,2,4,5,6,7,8,9],
    [4,1,2,3,5,6,7,8,9],
    [5,1,2,3,4,6,7,8,9]
], dtype=np.int8)

def nColumn(arr,n):
    columnArray=np.array([],dtype=np.int8)
    for i in range(arr.shape[0]):
        columnArray = np.append(columnArray,arr[i][n])
    return columnArray
    
def nRow(arr,n):
    rowArray=np.array([],dtype=np.int8)
    for i in range(arr.shape[1]):
        rowArray = np.append(rowArray,arr[n][i])
    return rowArray
    
def partitionRow(arr, n, part):
    partitionedRow=np.array([], dtype=np.int8)
    rowArray=nRow(arr,n)
    partEnd = part*3
    partStart = partEnd - 3
    for i in range(partStart, partEnd):
        partitionedRow = np.append(partitionedRow, rowArray[i])
    return partitionedRow
    
def xyGrids(arr,x_axis,y_axis):
    gridsArray = np.array([], dtype=np.int8)
    y_end = y_axis*3
    y_start = y_end - 3
    for i in range(y_start,y_end):
        tempList=partitionRow(arr,i,x_axis)
        gridsArray=np.append(gridsArray, tempList)
    return gridsArray
        
def noSameElement(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j == i:
                pass
            elif arr[i] == arr[j]:
                return False
            else: pass
    return True
    
def rowsAllGood(arr):
    for i in range(arr.shape[0]):
        tempList=nRow(arr,i)
        if noSameElement(tempList):
            pass
        else:
            return False
    return True
    
def columnsAllGood(arr):
    for i in range(arr.shape[1]):
        tempList=nColumn(arr,i)
        if noSameElement(tempList):
            pass
        else:
            return False
    return True

def gridsAllGood(arr):
    for i in range(1,3):
        for j in range(1,3):
            tempList=xyGrids(myArray, i, j)
            if noSameElement(tempList):
                pass
            else: return False
    return True

def allGood(arr):
    if columnsAllGood(arr)==rowsAllGood(arr)==gridsAllGood(arr)==True:
        return True
    else:
        return False

def rowExtender(arr, extend):                 #Make Sure The length of "to-be-extended" row match that of row of Array
    newArray=np.append(arr, [extend], axis=0)
    return newArray
    
def nRowMod(arr, n, index, newValue):
    tempList=np.array([],dtype=np.int8)
    for i in range(arr.shape[1]):
        if i == index:
            tempList = np.append(tempList,newValue)
        else:
            tempList = np.append(tempList,arr[n][i])
    return tempList
    
def arrayMod(arr, Row, Column, newValue):
    Row = Row-1
    Column = Column-1
    newArray=np.array([],dtype=np.int8)
    for i in range(arr.shape[0]):
        if i == 0:
            if i == Row:
                newArray= np.append(newArray, [nRowMod(arr,i, Column, newValue)])
            else:
                newArray= np.append(newArray, [nRow(arr,i)])
        elif i == 1:
            if i == Row:
                newArray= np.append([newArray], [nRowMod(arr,i, Column, newValue)], axis=0)
            else:
                newArray= np.append([newArray], [nRow(arr,i)], axis=0)
        else:
            if i == Row:
                newArray= np.append(newArray, [nRowMod(arr,i, Column, newValue)], axis=0)
            else:
                newArray= np.append(newArray, [nRow(arr,i)], axis=0)
    return newArray

# Game Mechanism
# for i in range(1000):
    # if i == 0:
        # print(myArray)
        # Row= int(input('Enter The Row:'))
        # Column=int(input('Enter The Column:'))
        # Value=int(input('Enter The Value:'))
        # tempArray= arrayMod(myArray, Row, Column, Value)
    # elif allGood(tempArray):
        # print(tempArray)
        # print("YOU HAVE SOLVED THE SUDOKU!!!")
        # break
    # else:
        # print(tempArray)
        # Row= int(input('Enter The Row:'))
        # Column=int(input('Enter The Column:'))
        # Value=int(input('Enter The Value:'))
        # tempArray= arrayMod(myArray, Row, Column, Value)
        
