class DongVat:
    def __init__(self,id,name,weigh,heigh):
        self.id = id
        self.name = name
        self.weigh = weigh
        self.heigh = heigh
    def HienThi(self):
        return (f'id:{self.id}; name:{self.name}; weigh:{self.weigh}; heigh:{self.heigh}')
        
def main():

    dv1 = DongVat(1,'cho',30,70)
    print(dv1.HienThi())
    