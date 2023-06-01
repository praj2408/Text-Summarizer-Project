import setuptools

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()


__version__ ="0.0.1"
REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "prajwal"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "prajwalgbdr03@gmail.com"




setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/praj2408/{REPO_NAME}",
    project_urls= {
        "Bug Tracker": f"https://github.com/praj2408/{REPO_NAME}"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)