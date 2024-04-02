"""
This tool is meant to be able to accept an image of a group of symbols and recognize them automatically, but for now users have to input the symbols manually

"""
import sys
import frequency

def interpret(text=""):
    """
    Takes a string representing non standard symbols
    """

    modes=["c", "p", "vbc", "vsbc"]
    if text=="":text=input("Symbols:  ")
    mode=input("What mode of analysis do you want? \n1] counts\n2] percentage\n3] verbose bar graph - count\n4] vervose simple bar graph - count\n")
    try:
        mode=int(mode)
    except:
        print("Invalid mode inputted")
        exit()

    if mode<3:
        mode=modes[mode-1]
        print(frequency.frequencyAnalysis(text, mode))
    else:
        mode=modes[mode-1]
        frequency.frequencyAnalysis(text, mode)
