def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if so_nuoc <= 10:
        tien_nuoc = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_nuoc = (10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2])
    else:
        tien_nuoc = (10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] +
                     (so_nuoc - 30) * gia_ban_nuoc[3])
    return tien_nuoc

# print("Nhap so nuoc su dung (m3): ", end="")
# so_nuoc = float(input())
# print(so_nuoc, "m3")
# print("So tien nuoc phai tra: ", tinh_tien_nuoc(so_nuoc), "VND")


# Tinh nguyen lieu lam banh.
def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd):
    banh_dau_xanh = {"duong": 0.04, "dau": 0.07}
    banh_thap_cam = {"duong": 0.06, "dau": 0}
    banh_deo = {"duong": 0.05, "dau": 0.02}
    nguyen_lieu = {}

    dau_hop_banh = sl_bdx * banh_dau_xanh["dau"] + sl_btc * banh_thap_cam["dau"] + sl_bd * banh_deo["dau"]
    duong_hop_banh = sl_bdx * banh_dau_xanh["duong"] + sl_btc * banh_thap_cam["duong"] + sl_bd * banh_deo["duong"]

    nguyen_lieu["duong"] = duong_hop_banh
    nguyen_lieu["dau"] = dau_hop_banh
    return nguyen_lieu

# print("Nhap so luong banh dau xanh:",  end="")
# sl_bdx = int(input())
# print("\n Nhap so luong banh thap cam: ", end="")
# sl_btc = int(input())
# print("\n Nhap so luong banh deo: ", end="")
# sl_bd = int(input())

# nguyen_lieu = tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd)
# print("\n So luong duong can dung: ", nguyen_lieu["duong"], "kg")
# print("So luong dau can dung: ", nguyen_lieu["dau"], "kg")