from setuptools import setup, find_packages

version = '1.0'

setup(name='davisagli.skel',
      version=version,
      description="David Glick's paster template",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Zope2",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone dexterity',
      author='David Glick',
      author_email='dglick@gmail.com',
      url='http://github.com/davisagli/davisagli.skel',
      license='GPL 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['davisagli'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript',
          'PasteDeploy',
          'Paste',
          'ZopeSkel'
          # -*- Extra requirements: -*-
      ],
      setup_requires=["PasteScript"],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      davisagli = davisagli.skel.davisagli:DavisagliSkel
      """,
      )
