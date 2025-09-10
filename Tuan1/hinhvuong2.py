import hinhvuong as hv

luachon_menu = {
    1: 'Thêm mới hình vuông', 
    2: 'Hiển thị danh sách hình vuông', 
    3: 'Tính tổng diện tích các hình vuông', 
    4: 'Hiển thị các hình vuông có chu vi nhỏ nhất', 
    'Others': 'Thoát chương trình\n'
}

def Menu():
    for i in luachon_menu.keys():
        print(i,'--',luachon_menu[i])
        
def Them(ds):
    canh = int(input("nhap vao canh hinh vuong: "))
    hv1 = hv.HinhVuong(canh)
    return ds.append(hv1)
    
def HienThiDS(ds):
    for i in ds:
        print(f'{i.HienThi()}')
        
def TongDT(ds):
    tongdt = 0
    for i in ds:
        tongdt += i.DienTich()
    return tongdt

def ChuViMin(ds):
    min = ds[0]
    for i in ds:
        if i.ChuVi() < min.ChuVi():
            min = i
    return min

ds = []

while True:
    Menu()
    choice = int(input('nhap vao lua chon cua ban: '))
    if choice == 1:
        Them(ds)
    elif choice == 2:
        print('danh sach hinh vuong la: \n')
        HienThiDS(ds)
    elif choice == 3:
        print(f'tong dien tich la: {TongDT(ds)}')
    elif choice == 4:
        a = ChuViMin(ds)
        print(f'hinh vuong nho nhat la: 1{a.HienThi()}')
    else: 
        break