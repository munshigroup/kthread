import setuptools

with open("README.md", "r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="kthread",
    version="0.2",
    author="The Munshi Group",
    author_email="support@munshigroup.com",
    description="Killable threads in Python!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/munshigroup/kthread",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)