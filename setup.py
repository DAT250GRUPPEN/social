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
# Husk at debugger må skrus av ved deployment :) hvis ikke så kommer hele tracebacken til "offentligheten" 