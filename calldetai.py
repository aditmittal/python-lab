class calldetails:
    def cdetail(self,cd):
        li = cd.split(',')
        print("sender =", li[0])
        print("reciever =", li[1])
        print("time =", li[2])
        print("ctype = ",li[3])
        print("\n\n")
class util:
    def __init__(self):
        self.locb = None
    def pcust(self,locs):
        for cd in locs:
            calldetails().cdetail(cd)
call1 = "9283748903,9182736450,23,std"
call2 = "9284748903,9182336450,13,isd"
call3 = "9285748903,9182636450,16,loc"

locs = [call1,call2,call3]
util().pcust(locs)
