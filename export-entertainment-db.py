import os


with open("D:\\codes\\msc\\databases\\entertainment.sql", "w") as d:
    pass

with open("D:\\codes\\msc\\databases\\import.sql", "r") as datas:
    for i in datas:
        with open("D:\\codes\\msc\\databases\\entertainment.sql", "a") as f:
            if "INSERT INTO" in i:
                f.write(f"{i[:i.index('VALUES') + 6]}\n")
                f.write(i[i.index("VALUES") + 7:].replace("),", "),\n").replace(");", ");\n"))
            else:
                f.write(i)

os.remove("D:\\codes\\msc\\databases\\import.sql")
