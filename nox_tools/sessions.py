#!/usr/bin/env python3
from dataclasses import dataclass
from glob import glob
from os.path import join
from typing import Optional

import nox


@dataclass
class Config:
    """Session configuration

    :param module: user's module name
    """
    module: Optional[str] = None

    @property
    def python_files(self):
        if self.module is None:
            raise RuntimeError('User must set config.module')
        return self.module, 'tests', *glob('*.py')


config = Config()


def install_requirements(requirements_file: str, session: nox.Session) -> None:
    session.install('-r', join('requirements', requirements_file))


def install_current_package(session: nox.Session) -> None:
    install_requirements('requirements.txt', session)
    session.install('.')


def install_test_packages(session: nox.Session) -> None:
    install_requirements('test_requirements.txt', session)


@nox.session
def tests(session: nox.Session) -> None:
    install_current_package(session)
    install_test_packages(session)
    session.run('coverage', 'run', '-m', 'pytest')
    session.run('coverage', 'report')


@nox.session
def typing(session: nox.Session) -> None:
    install_current_package(session)
    install_test_packages(session)
    install_requirements('typing_requirements.txt', session)
    install_requirements('toolchain_requirements.txt', session)
    session.run('mypy')


@nox.session
def linting(session: nox.Session) -> None:
    install_requirements('linting_requirements.txt', session)
    session.run('isort', '--check-only', *config.python_files)
    session.run('flake8', *config.python_files)
