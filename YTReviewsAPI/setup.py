from setuptools import find_packages, setup
#The packages gets all the relevant python packages, for non python files, you need to add
# them into the manifest.in
setup(
    name='TYReviewsAPI',
    version='0.1.0',
    author="Porter Hunley",
    author_email="porterhunley@gatech.edu",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)