"""""
Client facing file to interface with Translator tools

Options are:
    -ri [blank] read image
        Use ocr to read text from an image

    -dlo [blank] detect language online
        Detect the language from a string using an api (key stored in passwords.py)

    -dl [blank] detect language
        Detect the language from a string using an on-device model 

    -i [optional] interpret
        Takes a string of letters which represent non standard symbols

TODO:
    - Make thing
    - Add an option to edit text after interpretting, so humans can make sure its right
    - Only load the easyocr model when using ocr, maybe run it in a thread while the program asks the user for the filename
    - Maybe add a way to offload ocr to the cluster if the text is long and takes too much time on a laptop?

"""""

import readImage
import detectLanguage
import interpretSymbols
import sys

argsnum = len(sys.argv)

if argsnum > 1:

    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Help here")
        exit()

    # Accessing subsequent arguments in a similar way
    for i in range(1, len(sys.argv)):

        if sys.argv[i] == "-ri":
            # OCR Read image
            print(readImage.ocr(sys.argv[i+1]))

        elif sys.argv[i] == "-dlo":
            # Detect language with a third party api
            print(detectLanguage.detect_language(sys.argv[i+1]))

        elif sys.argv[i] == "-dl":
            # Detect language with an on-device model
            print(detectLanguage.detect_language_offline(sys.argv[i+1]))

        elif sys.argv[i] == "-i":
            # Interpret symbol string
            if len(sys.argv)>i+1:
                print(interpretSymbols.interpret(sys.argv[i+1]))

            print(interpretSymbols.interpret())

else:
    print("No arguments provided.")
