class HinhVuong:
    def __init__(self,canh):
        self.canh = canh
        
    def DienTich(self):
        return self.canh ** 2
    
    def ChuVi(self):
        return self.canh * 4
    
    def HienThi(self):
        return (f'hinh vuong canh {self.canh} co chu vi: {self.ChuVi():.2f} va dien tich: {self.DienTich():.2f}\n')
        