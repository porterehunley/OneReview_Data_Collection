from setuptools import find_packages, setup
#The packages gets all the relevant python packages, for non python files, you need to add
# them into the manifest.in
VERSION = "0.1.2"

setup(
    name='YTReviewsAPI',
    version=VERSION,
    author="Porter Hunley",
    author_email="porterhunley@gatech.edu",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)