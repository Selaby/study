### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import csv
file = "./list.csv"

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    if word in source:
        print("{}が見つかりました".format(word))
        print(source)
    else:
        print("{}が見つかりませんでした".format(word))
        #リストになかった場合に、キャラクターをsourceに追加出来るようにする
        with open(file, "r", encoding="utf-8-sig") as f:
        #https://qiita.com/msk02/items/c3a1c4a1e1ef94c37228 utf-8だと\ufeffが出力されてしまう
            rows = csv.reader(f)
            for row in rows:
                source.append(*row)
                #https://pillow545.com/programming/way_to_output ［］を出力しないようにする
        print(source)
        print("csvから追加しました")
    
if __name__ == "__main__":
    search()
    with open("./newlist.csv", "w", encoding="utf-8-sig", newline="\n") as f:
        writer = csv.writer(f, delimiter="\n")
        #https://qiita.com/ryokurta256/items/defc553f5165c88eac95 余計な改行を無くす
        writer.writerow(source)
        print("キャラクターリストを出力しました")