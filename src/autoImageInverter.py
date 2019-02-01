import sys
import cv2
import os
import os.path
import argparse

thresholdScale = 0.6   #The higher the more black pixels are needed to trigger an invert
precision = 10          #Only process every precision'th line
prefix = ""
fileFilter = ".png"


def InvertImage(imagem, name):
    imagem = cv2.bitwise_not(imagem)
    cv2.imwrite(name, imagem)

def autoThemeDetect(imagemem):
    totalCount = len(imagemem)

    blackCount = 0
    whiteCount = 0

    precisionCounter = 0

    for line in imagemem:
        if(precisionCounter == precision):
            for pixel in line:
                if(pixel == 0):
                    blackCount = blackCount + 1
                else:
                    whiteCount = whiteCount + 1

            precisionCounter = 0
        else:
            precisionCounter = precisionCounter + 1

    if(blackCount * thresholdScale > whiteCount):
        return True
    else:
        return False


def main():
    #Parsing Arguments
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--filter', help='Filter applying when searching for images')
    parser.add_argument('--prefix', help='Prefix to indicate converted files')
    parser.add_argument('--precision', help='Only process every precision th line')

    args = parser.parse_args()

    global fileFilter
    if(args.filter):
        fileFilter = args.filter

    global prefix
    if(args.prefix):
        prefix = args.prefix

    global precision
    if(args.precision):
        prefix = args.precision

    #Cheching for files
    print("Those following images will be processed:")

    fileList = []
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(fileFilter)]:
            filePath = os.path.join(dirpath, filename)
            fileList.append(filePath)
            print(filePath)

    #Show summary
    confirm = raw_input("Press Y to continue, any other key to cancel: ")

    if(confirm == "Y"):
        #Processing
        invCounter = 0
        for filePath in fileList:
            image = cv2.imread(filePath)
            image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            (thresh, image_bw) = cv2.threshold(image_gs, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

            print("Processing " + filePath)
            if(autoThemeDetect(image_bw)):
                print("This Image will be inverted")
                InvertImage(image, prefix+filePath)
                invCounter = invCounter + 1

        print("Inverted " + str(invCounter) + " images")
    else:
        print("Operation cancelled")


if __name__ == '__main__':
    main()