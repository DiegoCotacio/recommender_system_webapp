from setuptools import setup

with open("README.md", "r", encoding ="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Books Recommender System"
AUTHOR_USER_NAME = "DiegoCotacio"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['pandas','numpy','scipy','scikit-learn','pickle','joblib', 'streamlit']

setup(
    name = SRC_REPO,
    version = "0.0.1",
    author= AUTHOR_USER_NAME,
    description = "A small package for Book Recommender System",
    long_description= long_description,
    long_descriptión_content_type = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email= "diego.cotacio@correounivalle.edu.co",
    packages= [SRC_REPO],
    python_requires = ">3.8",
    install_requires = LIST_OF_REQUIREMENTS
    )


