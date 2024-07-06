class Language:
    def __init__(self, name: str, ability_read: str, ability_write: str, ability_speak: str) -> None:
        self.__name = name
        self.__ability_read = ability_read
        self.__ability_write = ability_write
        self.__ability_speak = ability_speak

    def __str__(self) -> str:
        return (f"Language: {self.__name}\n"
                f"Ability to Read: {self.__ability_read}\n"
                f"Ability to Write: {self.__ability_write}\n"
                f"Ability to Speak: {self.__ability_speak}")

    def __repr__(self) -> str:
        return (f"Language(name={self.__name!r}, ability_read={self.__ability_read!r}, "
                f"ability_write={self.__ability_write!r}, ability_speak={self.__ability_speak!r})")

    def __eq__(self, other) -> bool:
        if isinstance(other, Language):
            return (self.name == other.name and 
                    self.ability_read == other.ability_read and 
                    self.ability_write == other.ability_write and 
                    self.ability_speak == other.ability_speak)
        return False

    # Getter and setter functions

    # Getter and setter for name
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    # Getter and setter for ability_read
    @property
    def ability_read(self) -> str:
        return self.__ability_read

    @ability_read.setter
    def ability_read(self, ability_read: str) -> None:
        self.__ability_read = ability_read

    # Getter and setter for ability_write
    @property
    def ability_write(self) -> str:
        return self.__ability_write

    @ability_write.setter
    def ability_write(self, ability_write: str) -> None:
        self.__ability_write = ability_write

    # Getter and setter for ability_speak
    @property
    def ability_speak(self) -> str:
        return self.__ability_speak

    @ability_speak.setter
    def ability_speak(self, ability_speak: str) -> None:
        self.__ability_speak = ability_speak
