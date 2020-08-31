from puzzle import extract_digit
from puzzle import find_puzzle
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from sudoku import Sudoku
import numpy as np
import argparse
import imutils
import cv2
import random

print("[Start INFO] Welcome to Yushan's Sudoku OCR Solver.")
print("[Start INFO] There are 3 levels of diffculty of puzzles could be chosen:")
print("[Start INFO] Easy : 1")
print("[Start INFO] Medium : 2")
print("[Start INFO] Difficult : 3")

path = ''

import sys
val = input("[Start INFO] Enter difficulty Level: ")
if int(val) not in [1,2,3]:
    print("[Error INFO] Please enter a valid diffcult level from 1,2,3 ")
elif int(val) == 1:
        path = 'sudoku_data/60_Sudokus_New_Easy'    
elif int(val) == 2:
        path = 'sudoku_data/60_Sudokus_New_Medium'
elif int(val) == 3:
        path = 'sudoku_data/60_Sudokus_New_Difficult'        
    

image_Num = random.randint(1, 61)

image_path = path + '/' + str(image_Num) + '.jpg'

print("[Loading INFO] loading Sudoku Image...")
image = cv2.imread(image_path)
image = imutils.resize(image, width=600)

print("[Loading INFO] loading digit classifier...")
model = load_model("digit_classifier.h5")

(puzzleImage, warped) = find_puzzle(image, False)

board = np.zeros((9, 9), dtype="int")

stepX = warped.shape[1] // 9
stepY = warped.shape[0] // 9

cellLocs = []

for y in range(0, 9):
    # initialize the current list of cell locations
    row = []
    for x in range(0, 9):
        startX = x * stepX
        startY = y * stepY
        endX = (x + 1) * stepX
        endY = (y + 1) * stepY
        # add the (x, y)-coordinates to our cell locations list
        row.append((startX, startY, endX, endY))

        cell = warped[startY:endY, startX:endX]
        digit = extract_digit(cell, False)
        if digit is not None:

            roi = cv2.resize(digit, (28, 28))
            roi = roi.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            
            pred = model.predict(roi).argmax(axis=1)[0]
            board[y, x] = pred

    cellLocs.append(row)


print("[INFO] OCR'd Sudoku board:")
puzzle = Sudoku(3, 3, board=board.tolist())
puzzle.show()
# solve the Sudoku puzzle
print("[INFO] solving Sudoku puzzle...")
solution = puzzle.solve()
solution.show_full()

for (cellRow, boardRow) in zip(cellLocs, solution.board):
    # loop over individual cell in the row
    for (box, digit) in zip(cellRow, boardRow):
        startX, startY, endX, endY = box
		

        textX = int((endX - startX) * 0.33)
        textY = int((endY - startY) * -0.2)
        textX += startX
        textY += endY
        # draw the result digit on the Sudoku puzzle image
        cv2.putText(puzzleImage, str(digit), (textX, textY),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

cv2.imshow("Sudoku Result", puzzleImage)
cv2.waitKey(0)