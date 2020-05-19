from setuptools import setup, find_packages


setup(name='SpCL',
      version='0.0.1',
      description='Self-paced Contrastive Learning with Hybrid Memory for Domain Adaptive Object Re-ID',
      author='Anonymous',
      author_email='Anonymous',
      url='Anonymous',
      install_requires=[
          'numpy', 'torch', 'torchvision',
          'six', 'h5py', 'Pillow', 'scipy',
          'scikit-learn', 'metric-learn', 'faiss'],
      packages=find_packages(),
      keywords=[
          'Unsupervised Domain Adaptation',
          'Object Re-identification',
          'Contrastive Learning',
      ])
