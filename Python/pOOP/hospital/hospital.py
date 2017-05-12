''' HOSPITAL '''


class patient(object):
    def __init__(self, patient_id, name, allergies, bed_number=None):
        self.patient_id = patient_id
        self.name = name
        self.allegeries = allergies
        self.bed_number = bed_number
    def patientRecords(self):
        print self.name
        print self.bed_number

class hospital(object):
    def __init__(self, name, capacity=10):
        self.patients = ['','','']
        self.name = name
        #var newArr = Array(self.capacity,"")
        self.capacity = capacity
    def admit(self, patient):
        for i in range(0,len(self.patients)):
            if self.patients[i] != '':
                if i == len(self.patients)-1:
                    print "Hospital is full"
                continue
            if self.patients[i] == '':
                print "Admission Complete"
                self.patients[i] = patient
                self.patients[i].bed_number = i+1
                break
            # else:
            #     print "Hospital is Full"
        return self
    def discharge(self, patient_id_check):
        for i in range(len(self.patients)):
             if self.patients[i].patient_id == patient_id_check:
                name = self.patients[i].name
                self.patients[i].bed_number = None
                self.patients[i] = ''
                print "Goodbye", name
                break
        return self
    def patientInfo(self):
        for i in range(len(self.patients)):
            if self.patients[i] != '':
                print self.patients[i].name, "in Bed #:", self.patients[i].bed_number
            else:
                continue
        return self

p1 = patient(1, "Bruce", "Guns")
p2 = patient(2, "Diana", "None")
p3 = patient(3, "Laura", "Bananas")
p4 = patient(4, "Clark", "Kryptonite")

h1 = hospital("Good Hospital")

# h1.admit(p1)
h1.admit(p1).patientInfo().admit(p2).patientInfo().admit(p3).patientInfo().admit(p4).patientInfo().discharge(2).patientInfo().admit(p4).patientInfo()
# h1.admit(p1).admit(p2).admit(p3).admit(p4)
