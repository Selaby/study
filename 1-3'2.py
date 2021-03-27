import pandas as pd
# csvの読み書きをする際はpandasを利用することを心掛ける

file = "./list.csv"

### 検索ツール
def search():
    # 検索対象
    df = pd.read_csv("./list.csv")
    source = list(df["name"])

    while True:
    #https://www.headboost.jp/python-while-true/ 連続して入力できるようになる
        # ユーザー入力
        word=input("鬼滅の登場人物を入力　＞＞　")

        # 検索
        if word in source:
            print("『{}』が見つかりました".format(word))
        else:
            print("『{}』は見つかりませんでした".format(word))
            # 追加
            add_flg = input("追加登録しますか？(0:しない 1:する)　＞＞　")
            if add_flg == "1":
                source.append(word)

        df=pd.DataFrame(source,columns=["name"])
        df.to_csv("./list.csv",encoding="utf_8-sig")
        print(source)

if __name__ == "__main__":
    search()
