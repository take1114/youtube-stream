import streamlit as st
import pandas as pd
import math

# --- ページ設定 ---
st.set_page_config(
    page_title="ジャンボウサイト",
    page_icon=":bear:",
    layout="centered"  # ←モバイル最適化（中央寄せ）
)

# --- タイム表示整形 ---
def reshape_recode(z):
    if z < 60:
        return z
    else:
        m = int(z // 60)
        s = round((z % 60), 2)
        return m, s

# --- ポイント計算 ---
def point_get(t, nr):
    p = ((nr / t) ** 3) * 1000
    return math.floor(p)

# --- 比較選択（日本記録） ---
def Select_jrecode_style():
    distance = st.selectbox("距離を選択：", ['50m', '100m', '200m', '400m', '800m', '1500m'])
    style = st.selectbox("種目を選択：", ['Fr', 'Ba', 'Br', 'Fly', 'IM', 'FR', 'XFR', 'MR', 'XMR'])
    return distance, style

# --- 比較選択（マスターズ記録） ---
def Select_mrecode_style():
    distance = st.selectbox("距離を選択：", ['25m', '50m', '100m', '200m', '400m', '800m', '1500m'])
    style = st.selectbox("種目を選択：", ['Fr', 'Ba', 'Br', 'Fly', 'IM', 'FR', 'XFR', 'MR', 'XMR'])
    return distance, style

# --- 比較選択（チーム記録） ---
def Select_trecode_style():
    distance = st.selectbox("距離を選択：", ['25m', '50m', '100m', '200m', '400m', '800m', '1500m'])
    style = st.selectbox("種目を選択：", ['Fr', 'Ba', 'Br', 'Fly', 'IM'])
    return distance, style

# --- タイム入力 ---
def input_time(d, s):
    st.write(f"【{d} {s}】のタイム入力")
    t_m = st.number_input("分", min_value=0, step=1, key=f"{d}{s}_min")
    t_s = st.number_input("秒", min_value=0.0, step=0.01, key=f"{d}{s}_sec")
    total = t_m * 60 + t_s
    return total

# --- 記録表示 ---
def real(sr, t, d, s):
    myPoint = point_get(t, sr)
    Maxpoint = point_get(sr, sr)

    st.markdown(f"### {d} {s}")
    if sr < 60:
        shape_recode = reshape_recode(sr)
        st.write(f"【日本記録】 {shape_recode}秒　{Maxpoint}ポイント")
        st.write(f"【あなたの記録】 {t}秒　{myPoint}ポイント")
    else:
        m, sec = reshape_recode(sr)
        tm, ts = reshape_recode(t)
        st.write(f"【日本記録】 {m}分{sec}秒　{Maxpoint}ポイント")
        st.write(f"【あなたの記録】 {tm}分{ts}秒　{myPoint}ポイント")

# --- 目標比較表示 ---
def target(Sr, T, d1, s1, ud_t):
    myPoint = point_get(T, Sr)
    Maxpoint = point_get(Sr, Sr)
    ud_p = point_get(ud_t, Sr)

    st.markdown(f"### {d1} {s1}")
    if Sr < 60:
        st.write(f"【日本記録】 {reshape_recode(Sr)}秒　{Maxpoint}ポイント")
        st.write(f"【目標記録】 {ud_t}秒　{ud_p}ポイント")
        st.write(f"【あなたの記録】 {T}秒　{myPoint}ポイント")
    else:
        sr_m, sr_s = reshape_recode(Sr)
        ud_m, ud_s = reshape_recode(ud_t)
        t_m, t_s = reshape_recode(T)
        st.write(f"【日本記録】 {sr_m}分{sr_s}秒　{Maxpoint}ポイント")
        st.write(f"【目標記録】 {ud_m}分{ud_s}秒　{ud_p}ポイント")
        st.write(f"【あなたの記録】 {t_m}分{t_s}秒　{myPoint}ポイント")

# --- 各タブ作成 ---
tab1, tab2, tab3 = st.tabs(["日本記録へ至る道", "マスターズの頂", "チームトップ"])

# --- 日本記録タブ ---
with tab1:
    st.title("フィナポイント（日本記録）")
    df1 = pd.DataFrame({
        'Fr': [20.95, 46.22, 101.29, 216.87, 453.78, 865.95],
        'Ba': [22.81, 49.65, 108.25, None, None, None],
        'Br': [25.91, 55.77, 120.35, None, None, None],
        'Fly': [22.19, 49.54, 106.85, None, None, None],
        'IM': [None, 51.29, 110.47, 234.81, None, None],
        'FR': [83.80, 187.79, 412.04, None, None, None],
        'XFR': [89.51, None, None, None, None, None],
        'MR': [91.28, 201.07, None, None, None, None],
        'XMR': [97.29, None, None, None, None, None]
    }, index=['50m', '100m', '200m', '400m', '800m', '1500m'])
    st.dataframe(df1, use_container_width=True)

    distance, style = Select_jrecode_style()
    try:
        select_recode = float(df1.at[distance, style])
    except ValueError:
        st.error("記録が空白です")

    time = input_time(distance, style)
    if st.button("比較する", key="compare1"):
        real(select_recode, time, distance, style)

    update_time = st.number_input("目標タイム（秒）", key="goal1")
    if st.button("目標設定する", key="target1"):
        target(select_recode, time, distance, style, update_time)

# --- マスターズ記録タブ ---
with tab2:
    st.title("ジャンボウポイント（マスターズ記録）")
    df2 = pd.DataFrame({
        'Fr': [9.83, 21.84, 49.21, 108.95, 236.47, 498.16, 951.03],
        'Ba': [11.44, 23.95, 51.63, 116.01, None, None, None],
        'Br': [12.01, 26.58, 58.13, 128.28, None, None, None],
        'Fly': [10.52, 23.33, 52.42, 113.72, None, None, None],
        'IM': [None, None, 53.93, 118.91, 254.51, None, None],
    }, index=['25m', '50m', '100m', '200m', '400m', '800m', '1500m'])
    st.dataframe(df2, use_container_width=True)

    distance, style = Select_mrecode_style()
    try:
        select_recode = float(df2.at[distance, style])
    except ValueError:
        st.error("記録が空白です")

    time = input_time(distance, style)
    if st.button("比較する", key="compare2"):
        real(select_recode, time, distance, style)

    update_time = st.number_input("目標タイム（秒）", key="goal2")
    if st.button("目標設定する", key="target2"):
        target(select_recode, time, distance, style, update_time)

# --- チーム記録タブ ---
with tab3:
    st.title("ツキノワグマポイント（チーム記録）")
    df3 = pd.DataFrame({
        'Fr': [11.18, 23.61, 51.75, 139.62, None, None, None],
        'Ba': [13.08, 26.68, 62.29, 164.59, None, None, None],
        'Br': [14.19, 30.62, 67.47, None, None, None, None],
        'Fly': [11.02, 25.97, 61.13, None, None, None, None],
        'IM': [None, None, 62.06, 145.45, None, None, None],
    }, index=['25m', '50m', '100m', '200m', '400m', '800m', '1500m'])
    st.dataframe(df3, use_container_width=True)

    distance, style = Select_trecode_style()
    try:
        select_recode = float(df3.at[distance, style])
    except ValueError:
        st.error("記録が空白です")

    time = input_time(distance, style)
    if st.button("比較する", key="compare3"):
        real(select_recode, time, distance, style)

    update_time = st.number_input("目標タイム（秒）", key="goal3")
    if st.button("目標設定する", key="target3"):
        target(select_recode, time, distance, style, update_time)

