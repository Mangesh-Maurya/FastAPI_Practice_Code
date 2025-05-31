from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkdin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_digits=5)]
    contact_details: Dict[str, str]


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.allergies)
    print(patient.married)
    print(patient.contact_details)


Patient_info = {'name':'nitish', 'email':'abc@gmail.com', 'linkdin_url':'http://linkdin.com/1322', 'age':'30', 'weight':75.2, 'contact_details':{'phone':'950612134'}}

patient1 = Patient(**Patient_info)

update_patient_data(patient1)