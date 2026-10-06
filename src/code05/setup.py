from setuptools import find_packages, setup

package_name = 'code05'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='IHAiko',
    maintainer_email='nomokoko@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'static_tf = code05.static_tf_broadcaster:main',
            'dynamic_tf = code05.dynamic_tf_broadcaster:main',
            'tf_listener = code05.tf_listener:main',
        ],
    },
)
