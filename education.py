class Education:
    def __init__(self, institution: str, from_date: str, to_date: str, certificate: str, field_of_study: str) -> None:
        self.__institution = institution
        self.__from_date = from_date
        self.__to_date = to_date
        self.__certificate = certificate
        self.__field_of_study = field_of_study

    def __str__(self) -> str:
        return (f"{self.__institution}, {self.__from_date}-{self.__to_date}, {self.__certificate}, {self.__field_of_study}")

    def __repr__(self) -> str:
        return (f"Education(institution={self.__institution!r}, from_date={self.__from_date!r}, to_date={self.__to_date!r}, "
                f"certificate={self.__certificate!r}, field_of_study={self.__field_of_study!r})")

    def __eq__(self, other) -> bool:
        if isinstance(other, Education):
            return (self.institution == other.institution and 
                    self.from_date == other.from_date and 
                    self.to_date == other.to_date and 
                    self.certificate == other.certificate and 
                    self.field_of_study == other.field_of_study)
        return False

    # Getter and setter functions

    # Getter and setter for institution
    @property
    def institution(self) -> str:
        return self.__institution

    @institution.setter
    def institution(self, institution: str) -> None:
        self.__institution = institution

    # Getter and setter for from_date
    @property
    def from_date(self) -> str:
        return self.__from_date

    @from_date.setter
    def from_date(self, from_date: str) -> None:
        self.__from_date = from_date

    # Getter and setter for to_date
    @property
    def to_date(self) -> str:
        return self.__to_date

    @to_date.setter
    def to_date(self, to_date: str) -> None:
        self.__to_date = to_date

    # Getter and setter for certificate
    @property
    def certificate(self) -> str:
        return self.__certificate

    @certificate.setter
    def certificate(self, certificate: str) -> None:
        self.__certificate = certificate

    # Getter and setter for field_of_study
    @property
    def field_of_study(self) -> str:
        return self.__field_of_study

    @field_of_study.setter
    def field_of_study(self, field_of_study: str) -> None:
        self.__field_of_study = field_of_study
