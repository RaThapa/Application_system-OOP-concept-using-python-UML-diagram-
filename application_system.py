from application_form import ApplicationForm
from applicant import Applicant
from language import Language
from education import Education

class ApplicationSystem:
    def __init__(self) -> None:
        self.__applications = []

    def add_application(self, application_form: ApplicationForm) -> None:
        self.__applications.append(application_form)

    def search_application(self, app_id: int) -> ApplicationForm:
        for application in self.__applications:
            if application.id == app_id:
                return application
        return None # type: ignore

    def search_application_by_email(self, email: str) -> ApplicationForm:
        for application in self.__applications:
            if application.applicant.email == email:
                return application
        return None # type: ignore

    def update_application(self, app_id: int, updated_application_form: ApplicationForm) -> bool:
        for i, application in enumerate(self.__applications):
            if application.id == app_id:
                self.__applications[i] = updated_application_form
                return True
        return False

    def delete_application(self, app_id: int) -> bool:
        for i, application in enumerate(self.__applications):
            if application.id == app_id:
                del self.__applications[i]
                return True
        return False

    def display_applications(self) -> None:
        for application in self.__applications:
            print(application)

def menu():
    system = ApplicationSystem()
    while True:
        print("\nMenu:")
        print("1. Add Application")
        print("2. Search Application by ID")
        print("3. Search Application by Email")
        print("4. Update Application")
        print("5. Delete Application")
        print("6. Display All Applications")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            app_id = int(input("Application ID: "))
            name = input("Full name: ")
            dob = input("Date of Birth (dd/mm/yyyy): ")
            sex = input("Sex (Male/Female): ")
            home_address = input("Home address: ")
            phone_home = input("Phone number (Home): ")
            mobile = input("Mobile phone number: ")
            email = input("Email address: ")
            applicant = Applicant(name, dob, sex, home_address, phone_home, mobile, email)
            application_form = ApplicationForm(app_id, applicant)

            while True:
                add_lang = input("Add a language? (yes/no): ")
                if add_lang.lower() == "yes":
                    lang_name = input("Language: ")
                    read = input("Ability to read (Very Good/Good/Weak): ")
                    write = input("Ability to write (Very Good/Good/Weak): ")
                    speak = input("Ability to speak (Very Good/Good/Weak): ")
                    language = Language(lang_name, read, write, speak)
                    application_form.add_language(language)
                else:
                    break

            while True:
                add_edu = input("Add education? (yes/no): ")
                if add_edu.lower() == "yes":
                    institution = input("Name of University/Institution, Place and Country: ")
                    from_date = input("Attended From (Month/Year): ")
                    to_date = input("Attended To (Month/Year): ")
                    certificate = input("Certificates, Diplomas, Degrees obtained: ")
                    field_of_study = input("Main field of study: ")
                    education = Education(institution, from_date, to_date, certificate, field_of_study)
                    application_form.add_education(education)
                else:
                    break

            system.add_application(application_form)
            print("Application added successfully!")

        elif choice == "2":
            app_id = int(input("Enter the application ID to search: "))
            application = system.search_application(app_id)
            if application:
                print(application)
            else:
                print("Application not found!")

        elif choice == "3":
            email = input("Enter the email address to search: ")
            application = system.search_application_by_email(email)
            if application:
                print(application)
            else:
                print("Application not found!")

        elif choice == "4":
            app_id = int(input("Enter the application ID to update: "))
            application = system.search_application(app_id)
            if application:
                name = input(f"Full name ({application.applicant.name}): ") or application.applicant.name
                dob = input(f"Date of Birth ({application.applicant.dob}): ") or application.applicant.dob
                sex = input(f"Sex ({application.applicant.sex}): ") or application.applicant.sex
                home_address = input(f"Home address ({application.applicant.home_address}): ") or application.applicant.home_address
                phone_home = input(f"Phone number (Home) ({application.applicant.phone_home}): ") or application.applicant.phone_home
                mobile = input(f"Mobile phone number ({application.applicant.mobile}): ") or application.applicant.mobile
                email = input(f"Email address ({application.applicant.email}): ") or application.applicant.email

                updated_applicant = Applicant(name, dob, sex, home_address, phone_home, mobile, email)
                updated_application_form = ApplicationForm(app_id, updated_applicant)
                for lang in application.languages:
                    updated_application_form.add_language(lang)
                for edu in application.education:
                    updated_application_form.add_education(edu)

                system.update_application(app_id, updated_application_form)
                print("Application updated successfully!")
            else:
                print("Application not found!")

        elif choice == "5":
            app_id = int(input("Enter the application ID to delete: "))
            if system.delete_application(app_id):
                print("Application deleted successfully!")
            else:
                print("Application not found!")

        elif choice == "6":
            system.display_applications()

        elif choice == "7":
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()
