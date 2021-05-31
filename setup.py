import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='peloton-importer',  
     version='0.1',
     scripts=['importer'] ,
     author="Graham Mackie",
     author_email="gmackie@gmac.io",
     description="Data Importer for Peloton Workouts",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/gmackie/peloton-importer",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
