class Applicant:
    def __init__(self, name: str, dob: str, sex: str, home_address: str, phone_home: str, mobile: str, email: str) -> None:
        self.__name = name
        self.__dob = dob
        self.__sex = sex
        self.__home_address = home_address
        self.__phone_home = phone_home
        self.__mobile = mobile
        self.__email = email

    def __str__(self) -> str:
        return (f"Name: {self.__name}\nDOB: {self.__dob}\nSex: {self.__sex}\n"
                f"Home Address: {self.__home_address}\nPhone (Home): {self.__phone_home}\n"
                f"Mobile: {self.__mobile}\nEmail: {self.__email}")

    def __repr__(self) -> str:
        return (f"Applicant(name={self.__name!r}, dob={self.__dob!r}, sex={self.__sex!r}, "
                f"home_address={self.__home_address!r}, phone_home={self.__phone_home!r}, mobile={self.__mobile!r}, email={self.__email!r})")

    def __eq__(self, other) -> bool:
        if isinstance(other, Applicant):
            return (self.name == other.name and 
                    self.dob == other.dob and 
                    self.sex == other.sex and 
                    self.home_address == other.home_address and 
                    self.phone_home == other.phone_home and 
                    self.mobile == other.mobile and 
                    self.email == other.email)
        return False

    # Getter and setter functions

    # Getter and setter for name
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    # Getter and setter for dob
    @property
    def dob(self) -> str:
        return self.__dob

    @dob.setter
    def dob(self, dob: str) -> None:
        self.__dob = dob

    # Getter and setter for sex
    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, sex: str) -> None:
        self.__sex = sex

    # Getter and setter for home_address
    @property
    def home_address(self) -> str:
        return self.__home_address

    @home_address.setter
    def home_address(self, home_address: str) -> None:
        self.__home_address = home_address

    # Getter and setter for phone_home
    @property
    def phone_home(self) -> str:
        return self.__phone_home

    @phone_home.setter
    def phone_home(self, phone_home: str) -> None:
        self.__phone_home = phone_home

    # Getter and setter for mobile
    @property
    def mobile(self) -> str:
        return self.__mobile

    @mobile.setter
    def mobile(self, mobile: str) -> None:
        self.__mobile = mobile

    # Getter and setter for email
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        self.__email = email
