class Bank:
    def Company(self):
        print("HDFC Bank is the Bank")

class President(Bank):
    def Name(self):
        print("Rohit Verma is the President")

class BranchManager(President):
    def Bmanger(self):
        print("Rahul Srivastava is the Manager")
b = BranchManager()
b.Company()
b.Name()
b.Bmanger()
