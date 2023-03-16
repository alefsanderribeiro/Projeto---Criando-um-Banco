import os
from setuptools import setup, find_packages


# Obter o diretório atual para usar na leitura dos arquivos de texto
here = os.path.abspath(os.path.dirname(_file_))

# Função auxiliar para obter o conteúdo de um arquivo de texto
def read_file(filename):
    with open(os.path.join(here, filename), encoding='utf-8') as f:
        return f.read()


# Lista de dependências necessárias
install_requires = [
    'openpyxl>=3.0.7',
    'bcrypt>=3.2.0',
    'flask>=2.1.0',
    'flask-restful>=0.3.9',
]

# Lista de dependências para desenvolvimento
dev_requires = [
    'pytest>=6.2.4',
    'flake8>=3.9.2',
]

# Dicionário de informações sobre o projeto
setup(
    name='banco_digital',
    version='1.0.0',
    description='Um banco digital simples',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/alefsanderribeiro/banco-digital',
    author='Alefsander Ribeiro Nascimento',
    author_email='alefsander@alefsander.dev',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='banco digital',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'console_scripts': [
            'banco_digital_cli = interfaces.cli:main', ],},)