import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Affy-ETL", # Replace with your own username
    version="0.0.1",
    author="Hung Chang",
    author_email="zero102x@gmail.com",
    description="Affydata ETL package",
    long_description="Easy to extract/transform/loading Affy data ",
    long_description_content_type="text/markdown",
    url="https://github.com/dapingtai/Affy-ETL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)