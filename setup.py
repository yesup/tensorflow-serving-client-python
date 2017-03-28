from setuptools import setup

setup(name='tensorflowservingclient',
      version='0.5.1-2',
      description='Prebuilt tensorflow serving client',
      url='https://github.com/yesup/tensorflow-serving-client-python',
      author='Jeff Ye',
      author_email='jeffye@yesup.com',
      license='Apache 2.0',
      packages=['tensorflow_serving.apis'],
      install_requires=[
            'grpcio',
            'tensorflow'
      ],
      zip_safe=False)
