class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms=[]):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
            symptoms (string): symptoms
        """

        #ToDo1
        self.first_name= first_name
        self.surname = surname
        self.__age = age
        self.__mobile= mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = symptoms
        
    
    def full_name(self) :
        """full name is first_name and surname"""
        return f' {self.first_name} {self.surname}'
        #ToDo2
      


    def get_doctor(self) :
        return f'{self.__doctor}'
        #ToDo3
        

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        for items in self.__symptoms:
            print(items)
        #ToDo4
    
    def get_symptoms(self):
        return {self.__symptoms}
    
    def set_symptoms(self, new_symptoms):
        self.__symptoms = new_symptoms
    
    def get_surname(self):
        return f'{self.surname}'

   
    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{self.__symptoms:^10}'

