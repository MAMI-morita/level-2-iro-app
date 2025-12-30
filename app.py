import streamlit as st

st.title("🎨 色えらびアプリ")

st.write("あなたの好きな色は？")

color = st.radio(
    "えらんでね！",
    ["赤", "青", "黄色", "ピンク", "みどり", "むらさき"]
)

if color == "赤":
    st.markdown("### :red[赤が好きなんだね！ ❤️]")
elif color == "青":
    st.markdown("### :blue[青が好きなんだね！ 💙]")
elif color == "黄色":
    st.markdown("### :orange[黄色が好きなんだね！ 💛]")
elif color == "ピンク":
    st.markdown("### :violet[ピンクが好きなんだね！ 💗]")
elif color == "みどり":
    st.markdown("### :green[みどりが好きなんだね！ 💚]")
else:
    st.markdown("### :violet[むらさきが好きなんだね！ 💜]")

st.balloons()
```

**4. 下にスクロールして「新しいファイルをコミット」をクリック**

---

### ステップ3: 公開する

**1. Streamlit Cloudを開く**
```
https://share.streamlit.io/
