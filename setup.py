import setuptools
import setuptools.command.test

class NoseTestCommand(setuptools.command.test.test):
    def finalize_options(self):
        setuptools.command.test.test.finalize_options(self)
        self.test_args = []
        self.test_suite = True
        
    def run_tests(self):
        import nose
        nose.run_exit(argv=["nosetests"])
        

with open("README.md", "r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="kthread",
    version="0.2.2",
    author="The Munshi Group",
    author_email="support@munshigroup.com",
    description="Killable threads in Python!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="threading threads terminate",
    url="https://github.com/munshigroup/kthread",
    packages=setuptools.find_packages(exclude=["tests"]),
    tests_require=["nose"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={"test": NoseTestCommand},
)