from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wordfrequencies",
    version="0.1.0",
    author="Chrisjan Wust",
    author_email="chrisjanwust@gmail.com",
    description="Retrieve word frequency rankings for English words",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrisjanwust/wordfrequencies",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "wordfrequencies": ["word_frequency_data.tsv"],
    },
    install_requires=[
        "lazy_object_proxy",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
