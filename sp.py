class SanPham:
    # hàm khởi tạo
    def __init__(self,ten_san_pham, gia, giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia 
        self.__giam_gia = giam_gia 
    #getter/setter
    def get_ten(self):
        return self.__ten_san_pham
    def set_ten(self, ten_san_pham):
        self.__ten_san_pham = ten_san_pham

    def get_gia(self):
        return self.__gia
    def set_gia(self, gia):
        self.__gia = gia

    def get_giam_gia(self):
        return self.__giam_gia
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia   
    #tính thuế nhập khẩu 
    def thue_nhap_khau(self):
        return self.gia * 0.1
    #nhập thông tin từ bàn phím
    def nhap_thong_tin(self):
        self.ten_san_pham = input("tên sản phẩm")
        self.gia = float(input("giá"))
        self.giam_gia =float(input("giảm giá:"))
    #xuất thông tin
    def xuat_tt_sp(self):
        print(f"sản phẩm {self.ten_san_pham} có giá {self.gia} và được giảm giá {self.giam_gia}, Thuế nhập khẩu {self.thue_nhap_khau()}")
    def __str__(self):
        return f"sản phẩm {self.ten_san_pham} có giá {self.gia} và được giảm giá {self.giam_gia}"