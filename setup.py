from setuptools import setup, find_packages

setup(name='sera',
      version='0.1',
      description='My Python configuration.',
      packages=find_packages(),
      author_email='andrea.serafini@infn.it',
      zip_safe=False,
      install_requires=[
          'numpy','scipy', 'pandas', 'seaborn', 'tqdm', 'numba', 'matplotlib', 'uproot', 'iminuit', 
      ],
	  include_package_data=True,
      package_dir={'sera': 'sera'}, # directory which contains the python code
      package_data={'sera': []}, # directory which contains your data
      )
