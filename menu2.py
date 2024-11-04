import random
import streamlit as st
import pandas as pd
st.title("水泳メニュ自動生成アプリ")
st.caption("プロトタイプ")
st.subheader("内容紹介")
st.text("現在はトータル距離を入力すると距離・種目のみ決まったメニューが表示されます。")

w = 25
x = 50
y = 100
z = 200
up = 200
down = 100

i = random.randint(0,10)
j = random.randint(0,10)
k = random.randint(0,10)
l = random.randint(0,10)

syumoku1 = ["Fly","Ba","Br","Fr"]
syumoku2 = ["IM","Fr","Choice"]
syumoku3 = ["Fr","Choice","IM"]

st.write("各距離に対する選出種目")
df = pd.DataFrame({
    '距離':['25m','50m','100m','200m'],
    '種目1':['Fly','Fly','IM','IM'],
    '種目2':['Ba','Ba','Fr','Fr'],
    '種目3':['Br','Br','Choice','Choice'],
    '種目4':['Fr','Fr',' ',' ']
    })
st.dataframe(df.style.highlight_min(axis=0))

total = st.number_input("今日のメニューの合計距離は？-->",0)
print(total)
generate_btn = st.button("生成")
print(f"generate_button:{generate_btn}")

Total = int(w*i+x*j+y*k+z*l+up+down)
#print(Total)
if generate_btn:
    while Total != total:
        i = random.randint(0,10)
        j = random.randint(0,10)
        k = random.randint(0,10)
        l = random.randint(0,10)
        q = random.randint(0,2)
        r = random.randint(0,2)
        s = random.randint(0,3)
        t = random.randint(0,3)
        Total = int(w*i+x*j+y*k+z*l+up+down)
        if Total==total:
            st.write("W-up",up,"m")
            st.write(w,"m",syumoku1[s],i,"本")
            st.write(x,"m",syumoku1[t],j,"本")
            st.write(y,"m",syumoku2[r],k,"本")
            st.write(z,"m",syumoku3[q],l,"本")
            st.write("Down",down,"m")
            st.write("Total",total,"m")  
        else:
            print(Total)



