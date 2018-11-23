import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_django_app",
    version="0.1.0",
    author="Karthick Prabu",
    author_email="karthikprabu.cs@gmail.com",
    description="A small example django app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://stash.mtvi.com/projects/CDCNRY/repos/vmn-python-django-canary-app",
    packages=setuptools.find_packages(),
    include_package_data= True,
    package_data= {'example_django_app': 'collected-static/*'},
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
)