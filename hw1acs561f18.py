def readFile(inputFileName, outputFileName) :
    file = open(inputFileName, "r")
    output = open(outputFileName, "w+")
    f=file.readlines()
    for x in f:
        if x == "\n" or len(x.split(",")) <= 1:
            continue
        position = x.split(",")[0].strip()
        state = x.split(",")[1].strip()
        if position == "A" and state == "Clean":
            output.write("Right\n")
        elif position == "B" and state == "Clean":
            output.write("Left\n")
        elif (position == "A" or position == "B") and state == "Dirty":
            output.write("Suck\n")
    file.close()
    output.close()

if __name__=="__main__" :
    readFile("./input.txt", "output.txt")