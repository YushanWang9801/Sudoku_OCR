import os
import cv2


root = "C:/Users/yusha/Desktop/Sodoku_OCR/"

sodoku_path = 'C:/Users/yusha/Desktop/Sodoku_OCR/sol_data/'
data_path = "C:/Users/yusha/Desktop/Sodoku_OCR/solution_data/"

sodoku = os.listdir(sodoku_path)

for file in sodoku:
    images = os.listdir(sodoku_path+file+"/")
    if os.path.exists(data_path+file+"/") :
        pass
    else:
        os.mkdir(data_path+file+"/")
    os.chdir(data_path+file+"/")

    counter = 1
    print(images)
    for image_path in images:
        im = cv2.imread(sodoku_path+file+"/"+image_path)
        print(image_path)
        
        imgheight=im.shape[0]
        imgwidth=im.shape[1]

        y1 = 0
        M = imgheight//3
        N = imgwidth//2

        for y in range(0,imgheight,M):
            for x in range(0, imgwidth, N):
                y1 = y + M
                x1 = x + N
                tiles = im[y:y+M,x:x+N]

                #cv2.rectangle(im, (x, y), (x1, y1), (0, 255, 0))
                cv2.imwrite( data_path+file+"/" + str(counter) + ".png",tiles)
                counter += 1 
                #print("tile")