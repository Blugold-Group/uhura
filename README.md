# Uhura

Uhura is a universal translator, able to translate between languages, encodings, and formats, as well as translate physical forms into digital.

Abilities:
- [x] Read text from an image with OCR
- [ ] Read and translate other known symbols from an image
  - [ ] Braille
  - [ ] Morse
  - [ ] Semaphore?
- [ ] Can interpret symbols in a code which aren't recognizable ASCII symbols into a format for cryptanalysis 
- [x] Can read a text and find the language used
- [ ] Can translate between languages

## Symbol Interpreter

A tool which takes an image of physical symbols which aren't recognizable ascii characters (IE a message encrypted with the [Templar Cipher](https://www.dcode.fr/templars-cipher) on a piece of paper)

It uses a machine learning model to classify the synbols, but it assumes that the symbols haven't been seen before so it can't actually recognize them, it builds the model on the fly based on how the user classifies it

Or now that I'm thinking about it, the user could just color in a bunch of the symbols, so on the paper they color symbol A as a red background and symbol B as a green, and the model is built of off classifying using the color. It could still build the model assuming that the user won't color in all of the symbols, or just assume that the user will fill in all of the symbols
