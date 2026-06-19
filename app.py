import streamlit as st
from PIL import Image
img = Image.open("thao.png")
st.image(img, width=300)

# ==============================
# HÀM TÍNH THUẾ TNCN
# ==============================

def calculate_pit(
    salary,
    insurance,
    dependent
):

    # Giảm trừ gia cảnh (từ 2026)
    personal_deduction = 15_500_000
    dependent_deduction = dependent * 6_200_000


    # Thu nhập tính thuế
    taxable_income = (
        salary
        - insurance
        - personal_deduction
        - dependent_deduction
    )


    # Nếu không có thu nhập chịu thuế
    if taxable_income <= 0:
        return 0, taxable_income


    # Biểu thuế lũy tiến từng phần

    if taxable_income <= 10_000_000:

        tax = taxable_income * 0.05


    elif taxable_income <= 30_000_000:

        tax = (
            10_000_000 * 0.05
            + (taxable_income - 10_000_000) * 0.10
        )


    elif taxable_income <= 60_000_000:

        tax = (
            10_000_000 * 0.05
            + 20_000_000 * 0.10
            + (taxable_income - 30_000_000) * 0.20
        )


    elif taxable_income <= 100_000_000:

        tax = (
            10_000_000 * 0.05
            + 20_000_000 * 0.10
            + 30_000_000 * 0.20
            + (taxable_income - 60_000_000) * 0.30
        )


    else:

        tax = (
            10_000_000 * 0.05
            + 20_000_000 * 0.10
            + 30_000_000 * 0.20
            + 40_000_000 * 0.30
            + (taxable_income - 100_000_000) * 0.35
        )


    return tax, taxable_income



# ==============================
# GIAO DIỆN STREAMLIT
# ==============================


st.title("Ứng dụng tính thuế thu nhập cá nhân_VuThanhThao")


salary = st.number_input(
    "Tổng thu nhập tháng (VNĐ)",
    min_value=0,
    step=100000
)


insurance = st.number_input(
    "Bảo hiểm bắt buộc (VNĐ)",
    min_value=0,
    step=100000
)


dependent = st.number_input(
    "Số người phụ thuộc",
    min_value=0,
    step=1
)



if st.button("Tính thuế"):


    tax, taxable_income = calculate_pit(
        salary,
        insurance,
        dependent
    )


    st.write(
        f"Thu nhập tính thuế: {taxable_income:,.0f} VNĐ"
    )


    st.success(
        f"Thuế TNCN phải nộp: {tax:,.0f} VNĐ"
    )
