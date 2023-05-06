from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
   '''
     returns the list of requirements 
   '''
   requirements=[]
   with open(file_path) as file_obj:
      
      # returns a list with each line in the file as a separate element
      requirements=file_obj.readlines()
      
		# removes the newline character \n at the end of each line
      requirements=[req.replace("\n", "")for req in requirements]
      
      if HYPEN_E_DOT in requirements:
         requirements.remove(HYPEN_E_DOT)
         
   return requirements

setup(
    name='ml-project',
    version='0.1.0',
    description='A short description of the project.',
    author='Lee Godden',
    author_email ='lgodden@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
 