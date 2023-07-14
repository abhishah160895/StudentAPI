from database import student


class studentBO(object):

    def __init__(self,StudentId ,FirstName, LastName, DOB, Amount_Due):
        self.StudentId = StudentId
        self.FirstName = FirstName
        self.LastName = LastName
        self.DOB = DOB
        self.Amount_Due= Amount_Due

    def setObjFromOrMObj(self, ormuserdetail: student):
        self.StudentId = ormuserdetail.StudentId
        self.FirstName = ormuserdetail.FirstName
        self.LastName = ormuserdetail.LastName
        self.DOB = ormuserdetail.DOB
        self.Amount_Due = ormuserdetail.Amount_Due