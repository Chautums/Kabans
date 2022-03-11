with open("text.txt", encoding="utf-8") as fin, open ('cits.txt', encoding="utf-8", mode="w") as font:
        for line in fin: 
                if line.startswith("Ceļš"):
                        font.write(line)