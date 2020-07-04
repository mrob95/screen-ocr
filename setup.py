import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="screen-ocr",
    version="0.0.1",
    author="James Stout",
    author_email="james.wolf.stout@gmail.com",
    description="Library for processing screen contents using OCR",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wolfmanstout/screen-ocr",
    packages=["screen_ocr"],
    install_requires=[
        "fuzzywuzzy[speedup]",
        "numpy",
        "pandas",
        "pillow",
        "pytesseract",
        "scikit-image",
        'enum34; python_version < "3.4"',
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
