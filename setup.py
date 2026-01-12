from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    this function will return list of requirements

    :return: Description
    :rtype: List[str]
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # read line form the file
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore empty line and -e.
                if requirement and requirement != "-e.":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Requirement.txt file not found")

    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.0.3",
    author="Gaurav Thote",
    author_email="iamgauravthote@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
