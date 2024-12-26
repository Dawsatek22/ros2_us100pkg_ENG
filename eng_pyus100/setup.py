from setuptools import find_packages, setup # type: ignore

package_name = 'eng_pyus100'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rx3',
    maintainer_email='rx3@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sense = eng_pyus100.gpio0test:main',
            'sub = eng_pyus100.pwmtest:main',
            
        ],
    },
)
