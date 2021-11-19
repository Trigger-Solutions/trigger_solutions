from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in trigger_solutions/__init__.py
from trigger_solutions import __version__ as version

setup(
	name="trigger_solutions",
	version=version,
	description="ERP UI made simple",
	author="Trigger Solutions pvt. ltd.",
	author_email="trigger.solutions.eg@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
