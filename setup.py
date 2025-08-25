from setuptools import setup, find_packages

# Read README.md for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements.txt for dependencies
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="asciigen",
    version="0.0.1",
    author="Ishan Bhat",
    author_email="ishan2003bhat@gmail.com",
    description="A Python library for generating ASCII art from text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Artistic Software",
        "Topic :: Text Processing",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "asciigen=asciigen.cli:main",
        ],
    },
    keywords="ascii art text generator cli",
)
