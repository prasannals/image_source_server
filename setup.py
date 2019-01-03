import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="image_source_server",
    version="1.0.1",
    author="Prasanna Lakkur Subramanyam",
    author_email="prasanna.lakkur@gmail.com",
    description="Server for the Image Source app (available on Expo). Image Source helps send images, get predictions on images and train image models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prasannals/image_source_server",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
