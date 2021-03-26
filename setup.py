import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="translate-across-pond",
    version="1.0.0",
    author="Jack Weber",
    author_email="jackdavidweber at gmail dot com",
    description="Package to translate back and forth between American and British spellings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="<<< URL TO DOC WEBSITE OR GIT PROJECT >>>",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
