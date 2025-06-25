import streamlit as st

st.set_page_config(page_title="Tỏ tình bí mật", layout="centered")

correct_password = "23122005"

st.title("🔐 Nhập mật khẩu để xem điều bí mật 💌")
password = st.text_input("Mật khẩu:", type="password")

if password == correct_password:
    st.success("Mật khẩu chính xác! Đây là điều anh muốn nói với em 💖")
    st.image("https://i.imgur.com/1r2IfAn.jpeg", caption="Vì em là duy nhất 💘", use_column_width=True)
    st.markdown("""
    ## 💝 Gửi đến em:
    > "Từ lần đầu tiên anh gặp em, anh biết trái tim mình không thể bình yên nữa.  
    > Em có muốn... trở thành vợ anh không? 😳❤️"

    ---  

    👉 Nếu em cũng có cảm xúc như anh... hãy nhấn nút bên dưới nhé!
    """)

    if st.button("💘 Em đồng ý!"):
        st.success("Anh biết mà!!! 😍 Anh yêu em nhiều lắm! 💑")
        st.balloons()
else:
    if password != "":
        st.error("Sai mật khẩu rồi 😢 Thử lại nhé!")
