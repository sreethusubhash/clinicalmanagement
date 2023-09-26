from django.test import TestCase
from apps.resources import models


class TestHospitalModel(TestCase):
    def setUp(self):
        self.hospital=models.Hospital.objects.create(hos_name='CMMS')
    def test_Hospitaldetails(self):
        self.assertEqual(self.hospital.hos_name,'CMMS')



class TestDeptModel(TestCase):
    
    def setUp(self):
        self.dept_name='Cardiology'
        self.dept=models.Dept(dept_name=self.dept_name)#check obj created correctly
        
   
    def test_create_dept_object_successful(self):
        #Check if the obj created is of the instance Tag
        self.assertIsInstance(self.dept,models.Dept)
        
    
#Unit Test For Contact Model
class TestContactModel(TestCase):
    
    def setUp(self) -> None:
        self.name='sanu'
        self.ct=models.Contact(name=self.name)
      
    def test_create_contact_object_successful(self):
        self.assertIsInstance(self.ct,models.Contact)
        
        
       
        
    