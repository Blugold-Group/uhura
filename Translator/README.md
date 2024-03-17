# Translator

Translator is a tool which analyses an image and retrieves readable text in order to be used on a computer without a human having to copy all of the text by hand. 

Abilities:
    - [ ] Read text from an image with OCR
    - [ ] Read Braille from an image
    - [ ] Can interpret symbols in a code which aren't recognizable ASCII symbols 
    - [ ] Can read a text and find the language used
    
#### Symbol Interpreter

A tool which is fed an image of symbols, usually a code which is encrypted as symbols (not standard english letters or numbers)

The operator marks the corners of each symbol, and using the marks the tool can determine which are shapes. 

It optionally grayscales the image so colors won't strew the results, but can preserve color in case the code uses color