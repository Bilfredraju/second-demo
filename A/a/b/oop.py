class bnkacct:
    def __init__(self,acchname,acctno,balance):
        self.acctm=acchname
        self.acctnu=acctno
        self.balnce=balance
    def deposit(self,amt):
        if amt>0:
            self.balnce+=amt
            print(f"{amt} is depodited")
    def withdrw(self,amt):
        if self.balnce>=amt:
            self.balnce-=amt
            print(f"{amt} is withdrawed")
    def checkbalnce(self):
        return f'your current balance={self.balnce}'

custm1=bnkacct('mike','23455',45000)
custm1.deposit(10000)
custm1.withdrw(7000)
print(custm1.checkbalnce())
            

        