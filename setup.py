import os
from typing import List
from setuptools import setup

def reader(root: str, file: str) -> List:
	with open(os.path.join(root, file), "r") as f:
		return f.readlines()

setup(
	name = "SEAL",
	description = "A Secure Design Pattern Approach Toward Tackling Lateral-Injection Attacks",
	license = "GNU GENERAL PUBLIC LICENSE Version 3",
	author = "Chidera 'Chi' Biringa",
	author_email = "biringachidera@gmail.com",
	url = "https://github.com/biringaChi/SEAL",
	install_requires = [req.rstrip() for req in reader(os.getcwd(), "requirements.txt")],
	python_requires = ">=3.10.0"
)