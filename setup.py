import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "vietnamese-preprocess",
    version = "0.0.1",
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
    package_dir = {"": "vietnamese-preprocess"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)