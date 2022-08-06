from setuptools import setup
with open("src/README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='word_cloud',
    version='1.3',
    description='Generate word cloud',
    py_modules=["image,JupWordCloud,uploader,wordCloud"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[


    ],
    extra_require ={
        "dev":[
            "pytest>=3.7",

        ],
    },
    author="Fuad",
    mail="mdfuad17724@gmail.com",

)
