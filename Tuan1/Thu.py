import dongvat as dv

class Thu(dv.DongVat):
    def __init__(self, id, name, weigh, heigh,sochan):
        super().__init__(id, name, weigh, heigh)
        self.sochan = sochan
    
    def HienThi(self):
        return super().HienThi() + f';so chan: {self.sochan}'
        