#for文でデータフレーム作成
import pandas as pd
names=["a","b","c","d"]
list=[]
for i in names:
    list.append(i)
df=pd.DataFrame(list,columns=["name"])

#三角形を求める関数を作成して底辺5、高さ10を計算する。計算結果をanswerという変数に代入する。
#その後fストリングスで三角形の面積は●です。という文を出力する。
def tri(base,height):
    return base*height*0.5
answer=tri(5,10)
f"三角形の面積は{answer}です。"
