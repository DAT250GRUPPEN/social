# from setuptools import setup

# setup(name='atsocial',
#       packages=['atsocial'],
#       include_package_data=True,
#       install_requires=[
#           'flask',
#       ],
#       )

from atsocial import app

if __name__ == "__main__":
    app.run(debug=True)
