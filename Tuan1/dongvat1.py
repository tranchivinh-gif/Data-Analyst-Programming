import loaichim as chim
import Thu as thu
def Menu1():
    luachon_menu = {
        1:'nhap vao danh sach',
        2:'hien thi danh sach',
        3: 'tinh tong so can nang cua loai thu',
        4: 'tim ra dong vat co can nang lon nhat',
        5: 'tim ra loai dong vat co chieu cao thap nhat',
        6: 'doc file',
        7: 'ghi file',
        8: 'thoat'
    }
    
    for i in luachon_menu.keys():
        print(i,'--',luachon_menu[i])
        
def Menu2():
    luachon_loai = {
        1: 'loai thu',
        2: 'loai chim'
    }
    for i in luachon_loai.keys():
        print(i,'--',luachon_loai[i])
        
def Nhap(ds):
    while True:
        try:
            id = int(input("nhap vao id: "))
            ten = input("nhap vao ten: ")
            weight = float(input("nhap vao weight: "))
            height = float(input("nhap vao height: "))
        except ValueError:
            print('vui long nhap so hop le')
            continue
        while True:
            Menu2()
            try:
                choice = int(input("nhap vao loai ban muon nhap: "))
            except ValueError:
                print('vui long nhap so 1 hoac 2: ')
            if choice == 1:
                sochan = int(input("nhap vao so chan: "))
                dv = thu.Thu(id,ten,weight,height,sochan)
                ds.append(dv)
                return
            elif choice == 2:
                limit = float(input("nhap vao gioi han bay: "))
                dv = chim.Chim(id,ten,weight,height,limit)
                ds.append(dv)
                return
            else:
                print("vui long lua chon lop le!")
            
def TongWeight(ds):
    tong = 0
    for i in ds:
        tong += i.weigh   
    return tong

def MaxWeight(ds):
    max = ds[0]
    for i in ds:
        if i.weigh > max.weigh:
            max = i
    return max

def MinHeight(ds):
    min = ds[0]
    for i in ds:
        if i.heigh < min.heigh:
            min = i
    return min

def DocFile(filename,ds):
    with open(filename, 'r') as file:
        for line in file:
            kq = []
            data = line.strip().split(';')
            for i in data:
                data1 = i.split(':')
                kq.append(data1[1].strip())
            dv = thu.Thu(kq[0],kq[1],kq[2],kq[3],kq[4])
            ds.append(dv)
    return ds


def GhiFile(filename,ds):
    with open(filename,'a') as file:
        for i in ds:
            file.write(f"{i.HienThi()}\n")

def main():
    ds = []
    while True:
        Menu1()
        choice = int(input('nhap vao lua chon cua ban: '))
        if choice == 1:
            Nhap(ds)
        elif choice == 2:
            for i in ds:
                print(i.HienThi())
        elif choice == 3:
            print(f'tong can nang la: {TongWeight(ds)}')
        elif choice == 4:
            print(f'dong vat co can nang lon nhat la: {MaxWeight(ds).HienThi()}')
        elif choice == 5:
            print(f'dong vat co chieu cao nho nhat la: {MinHeight(ds).HienThi()}')
        elif choice == 6:
            file = "input.txt"
            DocFile(file,ds)
        elif choice == 7:
            file = "output.txt"
            GhiFile(file,ds)
            
main()
            