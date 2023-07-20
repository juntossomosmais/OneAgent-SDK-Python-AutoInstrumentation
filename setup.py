from setuptools import setup, find_packages

setup(
    name="jsm-autodynatrace",
    version="1.1.0",
    packages=find_packages(),
    package_data={"autodynatrace": ["wrappers/*"]},
    install_requires=["wrapt>=1.11.2", "oneagent-sdk>=1.3.0", "six>=1.10.0", "autowrapt>=1.0"],
    tests_require=["pytest", "mock", "tox", "django"],
    entry_points={"autodynatrace": ["string = autodynatrace:load"]},
    python_requires=">=3.6",
    author="Juntos Somos Mais",
    author_email="labs@juntossomosmais.com.br",
    description="Auto instrumentation for the OneAgent SDK",
    long_description="The autodynatrace package will auto instrument your python apps",
    url="https://github.com/juntossomosmais/OneAgent-SDK-Python-AutoInstrumentation",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: Apache Software License",  # 2.0
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: System :: Monitoring",
    ],
    project_urls={"Issue Tracker": "https://github.com/juntossomosmais/OneAgent-SDK-Python-AutoInstrumentation/issues"},
)
