"""Tests for the Patient model."""


def test_create_patient():
    """check if patient created has a name"""
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

def test_create_doctor():
    """Check doctor has a name"""
    from inflammation.models import Doctor

    name='Smith'
    d=Doctor(name=name)

    assert d.name==name

def test_doctor_is_person():
    """Check doctor belongs to person class"""
    from inflammation.models import Doctor, Person
    d = Doctor('Smith') 
    assert isinstance(d,Person)

def test_person_is_person():
    """Check patient belongs to person class"""
    from inflammation.models import Patient, Person
    p = Patient('Smith') 
    assert isinstance(p,Person)
    
def test_patients_added_correctly():
    """Check patients are being added correctly by a doctor. """
    from inflammation.models import Doctor, Patient
    doc = Doctor("Sheila Wheels")
    alice = Patient("Alice")
    doc.add_patient(alice)
    assert doc.patients is not None
    assert len(doc.patients) == 1

def test_no_duplicate_patients():
    """Check adding the same patient to the same doctor twice does not result in duplicates. """
    from inflammation.models import Doctor, Patient
    doc = Doctor("Sheila Wheels")
    alice = Patient("Alice")
    doc.add_patient(alice)
    doc.add_patient(alice)
    assert len(doc.patients) == 1 