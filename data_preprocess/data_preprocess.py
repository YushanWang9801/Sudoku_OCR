import os
import cv2


root = "C:/Users/yusha/Desktop/Sodoku_OCR/"

sol_path = 'C:/Users/yusha/Desktop/Sodoku_OCR/raw_images/solution/'
data_path = "C:/Users/yusha/Desktop/Sodoku_OCR/sol_data/"

sol = os.listdir(sol_path)

for file in sol:
    images = os.listdir(sol_path+file+"/")
    if os.path.exists(data_path+file+"/") :
        pass
    else:
        os.mkdir(data_path+file+"/")
    os.chdir(data_path+file+"/")

    counter = 1
    print(images)
    for image_path in images:
        im = cv2.imread(sol_path+file+"/"+image_path)
        print(image_path)
        
        #print(img.shape)
        height = im.shape[0]
        width = im.shape[1]

        # Cut the image in half
        width_cutoff = width // 2
        s1 = im[:, :width_cutoff]
        s2 = im[:, width_cutoff:]

        cv2.imwrite(data_path+file+"/" + str(counter) + ".png", s1)
        counter += 1
        cv2.imwrite(data_path+file+"/" + str(counter) + ".png", s2)
        counter += 1