import sys
import cv2
import os
import os.path
import argparse

thresholdScale = 0.90   #The higher the more black pixels are needed to trigger an invert
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
    parser.add_argument('--skipConfirm', help='Skip confirmation for auto processing. Pass Y as value')

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

    skipConfirm = False
    if(args.skipConfirm):
        skipConfirm = True
        confirm = args.skipConfirm

    #Cheching for files
    print("Those following images will be processed:")

    fileList = []
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(fileFilter)]:
            filePath = os.path.join(dirpath, filename)
            fileList.append(filePath)
            print(filePath)

    #Show summary
    if(not skipConfirm):
        confirm = raw_input("Press Y to continue, any other key to cancel: ")

    if(confirm == "Y"):
        print("Processing.. This might take some time")

        #Processing
        invCounter = 0
        for filePath in fileList:
            image = cv2.imread(filePath)
            imagem = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            print("Processing " + filePath)
            if(autoThemeDetect(imagem)):
                print("This Image will be inverted")
                InvertImage(imagem, prefix+filePath)
                invCounter = invCounter + 1

        print("Inverted " + str(invCounter) + " images")
    else:
        print("Operation cancelled")


if __name__ == '__main__':
    main()