# This file is part of dummypack.

# dummypack is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by
# the Free Software Foundation.

# dummypack is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# MIT License for more details.

# You should have received a copy of the MIT License
# along with dummypack. If not, see <https://opensource.org/licenses/MIT>.

from setuptools import setup, find_packages


setup(
      name='dummypack',
      version='1.0.0',
      author="Ayal Taitler",
      author_email="ataitler@gmail.com",
      description="dummypack: dummy package for pypi install",
      license="MIT License",
      url="https://github.com/ataitler/dummypack",
      packages=find_packages(),
      install_requires=[],
      python_requires=">=3.8",
      package_data={},
      include_package_data=True,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
