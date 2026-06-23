import streamlit as st
from PIL import Image
img = Image.open("thao.png")
st.image(img, width=300)
# Tiêu đề
st.title("💰 Ứng dụng tính Thuế Thu nhập cá nhân_Vũ Thanh Thao")
st.subheader("Vũ Thanh Thảo")

# Nhập dữ liệu
thu_nhap = st.number_input(
    "Nhập tổng thu nhập hàng tháng (triệu đồng)",
    min_value=0.0,
    value=30.0
)

luong_bhxh = st.number_input(
    "Nhập mức lương đóng BHXH (triệu đồng)",
    min_value=0.0,
    value=10.0
)

nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc",
    min_value=0,
    value=0
)

if st.button("Tính thuế"):

    # Bảo hiểm người lao động đóng
    bao_hiem = luong_bhxh * 0.105

    # Giảm trừ gia cảnh
    giam_tru_ban_than = 15.5
    giam_tru_phu_thuoc = 6.2 * nguoi_phu_thuoc

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = (
        thu_nhap
        - bao_hiem
        - giam_tru_ban_than
        - giam_tru_phu_thuoc
    )

    if thu_nhap_tinh_thue < 0:
        thu_nhap_tinh_thue = 0

    # Thuế TNCN lũy tiến từng phần
    if thu_nhap_tinh_thue <= 10:
        thue = thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 30:
        thue = (
            10 * 0.05
            + (thu_nhap_tinh_thue - 10) * 0.10
        )

    elif thu_nhap_tinh_thue <= 60:
        thue = (
            10 * 0.05
            + 20 * 0.10
            + (thu_nhap_tinh_thue - 30) * 0.20
        )

    elif thu_nhap_tinh_thue <= 100:
        thue = (
            10 * 0.05
            + 20 * 0.10
            + 30 * 0.20
            + (thu_nhap_tinh_thue - 60) * 0.30
        )

    else:
        thue = (
            10 * 0.05
            + 20 * 0.10
            + 30 * 0.20
            + 40 * 0.30
            + (thu_nhap_tinh_thue - 100) * 0.35
        )

    # Thu nhập thực nhận
    thu_nhap_net = thu_nhap - bao_hiem - thue

    # Kết quả
    st.success("KẾT QUẢ TÍNH TOÁN")

    st.write(f"Tổng thu nhập: {thu_nhap:.2f} triệu đồng")
    st.write(f"Mức lương đóng BHXH: {luong_bhxh:.2f} triệu đồng")

    st.write(
        f"Bảo hiểm người lao động (10,5%): {bao_hiem:.2f} triệu đồng"
    )

    st.write(
        f"Giảm trừ bản thân: {giam_tru_ban_than:.2f} triệu đồng"
    )

    st.write(
        f"Giảm trừ người phụ thuộc: {giam_tru_phu_thuoc:.2f} triệu đồng"
    )

    st.write(
        f"Thu nhập tính thuế: {thu_nhap_tinh_thue:.2f} triệu đồng"
    )

    st.write(
        f"Thuế TNCN phải nộp: {thue:.2f} triệu đồng"
    )

    st.write(
        f" Thu nhập thực nhận: {thu_nhap_net:.2f} triệu đồng"
    )
