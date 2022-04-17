import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="thelittlethings",
    version="1.0.4",
    author="Simon Kriele",
    author_email="kriele.simon@gmail.com",
    description="a library full of small utilities for you to use in your code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dots-git/thelittlethings",
    project_urls={
        "Bug Tracker": "https://github.com/dots-git/thelittlethings/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
)