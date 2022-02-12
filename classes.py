## doctors and patients


class Doctor():

    def __init__ (self , name , lastname , specialty , room_number ):
        self.name=name
        self.lastname = lastname
        self.specialty = specialty
        self.room_number = room_number

    def change_name(self,new_name):
        self.name = new_name
        





class Patient():
    def __init__ (self , name , lastname , phone , doctor ):
        self.name=name
        self.lastname = lastname
        self.phone = phone
        self.doctor = doctor
