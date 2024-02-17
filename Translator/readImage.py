import easyocr

def ocr(imagepath, format="pretty"):


    reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
    result = reader.readtext(imagepath)


    if format=="pretty":
        text=""

        for i in result:
            text+=i[1]

        return(text)
    else:
        return(result)

