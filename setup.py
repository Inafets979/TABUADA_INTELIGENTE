from setuptools import setup, find_packages
from pathlib import Path

# Use path relative to this file to work correctly when build runs in an isolated
# environment where the current working directory may be different.
BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open(BASE_DIR / "requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="tabuada_inteligente",
    version="1.0.0",
    author="Inafets979",
    author_email="biarragam@gmail.com",
    description="Aplicação educativa para aprender tabuadas com interface gráfica e terminal",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Inafets979/TABUADA_INTELIGENTE.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={
        "console_scripts": [
            "tabuada=main:main"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)