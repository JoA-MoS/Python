import uuid
import datetime


class Patient(object):
    def __init__(self, name, allergies=[], bed_number=None):
        self.id = uuid.uuid4()
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number

    def __str__(self, template='{0}\t{1}\t{2}\t{3}'):
        return template.format(self.id, self.name, self.allergies, self.bed_number)


class Hospital(object):
    def __init__(self, name, capacity, patients=[],):
        self.name = name
        self.capacity = capacity
        self.patients = patients

    def admit(self, patient):
        if len(self.patients) < self.capacity:
            patient.bed_number = len(self.patients)
            self.patients.append(patient)
            print '{} admitted to bed {}'.format(patient.name, patient.bed_number)
        else:
            print 'The hospital is full'
        return self

    def discharge(self, patient):
        self.patients.remove(patient)
        return self

    def display_patients(self):
        print 'Patient ID\tName\tAlergies\tBed'
        for p in self.patients:
            print p
        return self


p = Patient('Justin', ['penicilin', 'c-chlor'])
h = Hospital('HM', 10)
h.admit(p)
h.admit(Patient('James'))
h.discharge(p)
h.display_patients()
