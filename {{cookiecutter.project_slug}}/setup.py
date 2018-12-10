from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.1.0",
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    description="{{cookiecutter.description}}",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: {{cookiecutter.open_source_license}}",
        "Operating System :: OS Independent",
    ],
)
