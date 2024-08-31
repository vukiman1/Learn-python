def tinh_tien_dien(so_kw, ho_ngheo):
    # Giá các mức điện
    gia = [450, 600, 750, 900, 1000, 1200]
    gioi_han = [100, 100, 100, 200, 500]
    
    # Xử lý cho hộ nghèo
    if ho_ngheo == 1:
        gioi_han[0] = 200

    tien_dien = 0
    kw_con_lai = so_kw

    # Tính tiền điện theo từng mức giá
    for i in range(len(gioi_han)):
        if kw_con_lai > gioi_han[i]:
            tien_dien += gioi_han[i] * gia[i]
            kw_con_lai -= gioi_han[i]
        else:
            tien_dien += kw_con_lai * gia[i]
            kw_con_lai = 0
            break

    if kw_con_lai > 0:
        tien_dien += kw_con_lai * gia[-1]

    # Tính thuế VAT
    thue_vat = tien_dien * 0.10
    
    # Tính phí bảo vệ môi trường
    phi_bao_ve_moi_truong = so_kw * 0.02 * gia[0]  # Tính theo giá rẻ nhất

    # Tổng số tiền phải trả
    tong_tien = tien_dien + thue_vat
    
    # In kết quả
    print(f"Tổng tiền điện trước thuế VAT: {tien_dien} VND")
    print(f"Thuế VAT (10%): {thue_vat} VND")
    print(f"Phí bảo vệ môi trường: {phi_bao_ve_moi_truong} VND")
    print(f"Tổng số tiền phải nộp (sau khi tính thuế VAT): {tong_tien} VND")

# Nhập số KW và tình trạng hộ nghèo
so_kw = int(input("Nhập số KW tiêu thụ điện: "))
ho_ngheo = int(input("Nhập 1 nếu là hộ nghèo, 0 nếu không nghèo: "))

# Gọi hàm tính tiền điện
tinh_tien_dien(so_kw, ho_ngheo)
