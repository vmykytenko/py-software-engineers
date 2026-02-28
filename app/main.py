from __future__ import annotations


class SoftwareEngineer:

    def __init__(self, name: str) -> None:

        pass

    def learn_skill(self, skill: str) -> None:

        pass


class FrontendDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:

        pass

    def create_awesome_web_page(self) -> None:

        pass


class BackendDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:

        pass

    def create_powerful_api(self) -> None:

        pass


class AndroidDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:

        pass

    def create_smooth_mobile_app(self) -> None:

        pass


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):

    def create_web_application(self) -> None:

        pass
