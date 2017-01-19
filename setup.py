from setuptools import setup, find_packages

setup(
    name='recommendation',
    version='0.1.8',
    url='https://github.com/wikimedia/research-recommendation-api',
    license='Apache Software License',
    maintainer='Wikimedia Research',
    maintainer_email='',
    description='',
    long_description='',
    packages=find_packages(exclude=['test', 'test.*', '*.test']),
    install_requires=['flask',
                      'flask-restplus',
                      'requests',
                      'numpy',
                      'scipy',
                      'sklearn'],
    package_data={'recommendation.web': ['static/*.*',
                                         'static/i18n/*',
                                         'static/images/*',
                                         'static/suggest-searches/*',
                                         'templates/*'],
                  'recommendation': ['data/*']},
    zip_safe=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest',
                   'responses'])
