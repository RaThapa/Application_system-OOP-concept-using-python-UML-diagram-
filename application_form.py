from applicant import Applicant
from language import Language
from education import Education

class ApplicationForm:
    def __init__(self, app_id: int, applicant: Applicant) -> None:
        self.__id = app_id
        self.__applicant = applicant
        self.__languages = []
        self.__education = []

    def add_language(self, language: Language) -> None:
        self.__languages.append(language)

    def add_education(self, education: Education) -> None:
        self.__education.append(education)

    def update_language(self, index: int, read=None, write=None, speak=None) -> None:
        if 0 <= index < len(self.__languages):
            self.__languages[index].ability_read = read or self.__languages[index].ability_read
            self.__languages[index].ability_write = write or self.__languages[index].ability_write
            self.__languages[index].ability_speak = speak or self.__languages[index].ability_speak

    def update_education(self, index: int, institution=None, from_date=None, to_date=None, certificate=None, field_of_study=None) -> None:
        if 0 <= index < len(self.__education):
            self.__education[index].institution = institution or self.__education[index].institution
            self.__education[index].from_date = from_date or self.__education[index].from_date
            self.__education[index].to_date = to_date or self.__education[index].to_date
            self.__education[index].certificate = certificate or self.__education[index].certificate
            self.__education[index].field_of_study = field_of_study or self.__education[index].field_of_study

    def __str__(self) -> str:
        languages_str = "\n".join([str(lang) for lang in self.__languages])
        education_str = "\n".join([str(edu) for edu in self.__education])
        return (f"Application ID: {self.__id}\n{self.__applicant}\n\nLanguages:\n{languages_str}\n\nEducation:\n{education_str}")

    @property
    def id(self) -> int:
        return self.__id

    @property
    def applicant(self) -> Applicant:
        return self.__applicant

    @property
    def languages(self) -> list:
        return self.__languages

    @property
    def education(self) -> list:
        return self.__education
