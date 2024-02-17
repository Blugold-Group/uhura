"""""
This file is the user facing interface for the translator tool

TODO:
    - Make thing
    - Add an option to edit text after interpretting, so huamsn can make sure its right
    - Only load the easyocr model when using ocr, maybe run it in a thread while the program asks the user for the filename
    - Maybe add a way to offload ocr to the cluster if the text is long and takes too much time on a laptop?

"""""

print("Translator loading...")
import readImage

