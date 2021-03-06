import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mobtexting_python",
    version="0.0.1",
    author="lucky",
    author_email="lakshminarayana.s@mobtexting.com",
    description="Python plugin to send sms using mobtexting",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
       "requests"
    ]

)
