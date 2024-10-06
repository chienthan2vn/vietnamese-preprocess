import setuptools
import os

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding = "utf-8") as fh:
    requirements = [re.strip() for re in fh.readlines()]
setuptools.setup(
    name = "vnpreprocess",
    version = "0.0.2",
    description='Preprocess Vietnamese language',
    url='https://github.com/chienthan2vn/vietnamese-preprocess',
    author='Thuan Luong',
    author_email='thuanluong19102001@gmail.com',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    include_package_data=True,
    package_data={
        '': ['*.txt', '*.sav', '*.xlsx', '*.md']
    },
    python_requires = ">=3.6"
)