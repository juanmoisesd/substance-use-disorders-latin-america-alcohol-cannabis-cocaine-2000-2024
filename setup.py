from setuptools import setup, find_packages
setup(
    name="substance-use-disorders-latin-america-alcohol-cannabis-cocaine-2000-2024",
    version="1.0.0",
    description="Substance use disorders database for 14 Latin American countries (2000–2024): alcohol, cannabis, coc",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/substance-use-disorders-latin-america-alcohol-cannabis-cocaine-2000-2024",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="zenodo, open-data",
)