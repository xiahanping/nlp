import pandas as pd


csv_path = "1558435.csv"

contents = pd.read_csv(csv_path, encoding = "gb18030")

contents = contents.fillna('')

print("wirte start")
for i in range(len(contents)):

    with open("news.txt", "a", encoding = "utf8") as f:

        data = contents['url'][i] + " " + contents['author'][i]
        f.write(data)

print("wirte end")




