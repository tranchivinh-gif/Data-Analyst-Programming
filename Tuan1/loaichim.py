import dongvat as dv

class Chim(dv.DongVat):
    def __init__(self, id, name, weigh, heigh,litmit_fly):
        super().__init__(id, name, weigh, heigh)
        self.litmit_fly = litmit_fly
    
    def HienThi(self):
        return super().HienThi() + f';litmit_fly: {self.litmit_fly}'
        

