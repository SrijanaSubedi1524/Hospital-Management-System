class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    
    def full_name(self) :
        return f'{self.__first_name} {self.__surname}'
        #ToDo1    
        

    def get_first_name(self) :
        return f'{self.__first_name}'
        #ToDo2
        

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name
        #ToDo3
       

    def get_surname(self) :
        return f'{self.__surname}'
        #ToDo4
        

    def set_surname(self, new_surname):
        self.__surname= new_surname
        #ToDo5
       

    def get_speciality(self) :
        return f'{self.__speciality}'
        #ToDo6
       

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality
        #ToDo7
        

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_total_patients(self):
        return len(self.__patients)
    
    def get_total_appointments(self):
        return len(self.__appointments)


    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
    





