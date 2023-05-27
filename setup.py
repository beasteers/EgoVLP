import setuptools

setuptools.setup(
    name='egovlp',
    version='0.0.1',
    description='EgoVLP: Egocentric Video-Language Pretraining',
    long_description=open('README.md').read().strip(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=[
        'torch', 'torchvision', 'supervision',
        'transformers', 'av', 'decord', 'ffmpeg', 
        'humanize', 'psutil', 'transformers', 
        'timm', 'einops',
    ],
    extras_require={})
