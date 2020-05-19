from setuptools import setup, find_packages


setup(name='SpCL',
      version='0.1.0',
      description='Self-paced Contrastive Learning with Hybrid Memory for Domain Adaptive Object Re-ID',
      author='Anonymous',
      author_email='Anonymous',
      url='https://github.com/spcl-reid/SpCL',
      install_requires=[
          'numpy', 'torch', 'torchvision',
          'six', 'h5py', 'Pillow', 'scipy',
          'scikit-learn', 'metric-learn', 'faiss'],
      packages=find_packages(),
      keywords=[
          'Unsupervised Learning',
          'Unsupervised Domain Adaptation',
          'Contrastive Learning',
          'Object Re-identification'
      ])
