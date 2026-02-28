from __future__ import annotations


class SoftwareEngineer:

    def __init__(self, name: str) -> None:

        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:

        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:

        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> None:

        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


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
