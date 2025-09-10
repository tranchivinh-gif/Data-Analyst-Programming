import hinhvuong as hv

def Docfile(filename,ds):
    with open(filename, 'r') as file:
        for line in file:
            x = line.strip().split(':')
            canh = int(x[1])
            ds.append(hv.HinhVuong(canh))
        return ds
    
def GhiFile(filename,ds):
    for i in ds:
        with open(filename,'a') as file:
            file.write(f'{i.HienThi()}')
    print("in thanh cong!")
    
def Main():
    ds = []
    file = "input.txt"
    fileout = "output.txt"
    Docfile(file,ds)
    for i in ds:
        print(i.HienThi())
    
    GhiFile(fileout,ds)
        
Main()
         