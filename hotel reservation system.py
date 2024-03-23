class Hotel_Reservation:
    total_rooms_first_floor=15
    total_rooms_second_floor=20
    def __init__(self):
        self.current_update_first_floor=10
        self.current_update_second_floor=15
    def room_availability(self):
        print(f"total rooms in first floor={Hotel_Reservation.total_rooms_first_floor}")
        print(f"total rooms in second floor={Hotel_Reservation.total_rooms_second_floor}")
        print(f"Total rooms occupied  in first floor={self.current_update_first_floor}")
        print(f"Total rooms occupied  in second floor={self.current_update_second_floor}")
    def getting_confirmation(self):
        while True:
            getting_again=input("still your are interseted to book rooms because only {self.available_rooms_in_first_floor} rooms are available..[yes/no]")
            if getting_again.casefold()=="yes":
                print("We proceed further..")
                break
            elif getting_again.lower()=="no":
                print("Ok...your going to exit...")
                exit()
            else:
                print(f"please check your input..")
    def room_booking(self):
        self.available_rooms_in_first_floor=Hotel_Reservation.total_rooms_first_floor-self.current_update_first_floor
        self.available_rooms_in_second_floor=Hotel_Reservation.total_rooms_second_floor-self.current_update_second_floor
        print(f"Menu\n1.first_floor\n2.second_floor")
        while True:
            floor_choice=input("Which floor u want to book..Enter your choice from  the above menu").lower()
            if floor_choice=="1" or floor_choice=="2":
                break
            else:
                print("Enter  a valid input")
        try:
            getting_rooms=int(input("Enter how many rooms you want.."))
        except ValueError as e1:
            print(e1)
            getting_rooms=int(input("Enter how many rooms you want.."))
        else:
            while True:
                if getting_rooms>self.available_rooms_in_first_floor and floor_choice=="1":
                    print(f"Only {self.available_rooms_in_first_floor} are available")
                    self.getting_confirmation()
                    break
                elif getting_rooms>self.available_rooms_in_first_floor and floor_choice=="2":
                    print(f"Only {self.available_rooms_in_second_floor} are available")
                    self.getting_confirmation()
                    break
                else:
                    print(f"Enter a valid input....")
        while True:    
            getting_capacity=input("Enter room capacity [single/double/trible]")
            if getting_capacity.lower()=="single" or getting_capacity.lower()=="double" or getting_capacity.lower()=="trible":
                break
            else:
                print(f"Enter a valid input")
        getting_reason=input("Purpose of booking rooms :").lower()
        print(f"your request..")
        print(f"Floor= {floor_choice}")
        print(f"Total_Rooms= {getting_rooms}")
        print(f"Room_capacity= {getting_capacity}")
        print("Is successfully booked!!!")
        print(f"********===HAPPY {getting_reason}===********")
    def cancel_booking(self):
        getting_input=input("Do u want do cancel your room booking..[yes/no]").casefold()
        if getting_input.isalpha():

            list_val=["Menu","1.I cancelled my trip","2.too costly","3.no idea","4.other"]
            for i in list_val:
                print(i)        
        
            getting_reason=input("Enter why u are decided to cancel booking chooce any one from the above menu")
            
            if getting_reason=="1" or getting_reason=="2" or getting_reason=="3":
                print(f"Alset your booking is cancelled!")
            elif getting_reason=="4":
                getting_suggestion=input("Enter your reason :")
                print(f"Alset your booking is successfully cancelled!")
            else:
                print("Enter a valid input")
        else:
            print("Enter a valid input")
if __name__=="__main__":
    obj=Hotel_Reservation()
    def menu():
        print("******Welcome to sri murugan hotel******")
        
        print("Here are the menu available for you.....")
        list_val=["Menu","1.room availability checking","2.room booking",
                  "3.cancel booking","4.Exit"]
        for option in list_val:
            print(option)
    def main_block():
        menu()
        while True:    
            getting_input=input("what are u looking from here..... Enter your choice from the menubar :")
            if getting_input=="1":
                obj.room_availability()
                break
            elif getting_input=="2":
                obj.room_booking()
                break
            elif getting_input=="3":
                obj.cancel_booking()
                break
            elif getting_input=="4":
                print("exit!")
                break
            else:
                print(f"Enter a valid input")
    def continues():
        while True:
            continue_choice=input("Do you want do continue this page [yes/no]")
            if continue_choice.lower()=="yes":
                main_block()
                break
            elif continue_choice.lower()=="no":
                print(f"You are going to exit...")
                exit()
            else:
                print("Thankyou visit again !")
            

    main_block()
    continues()
                    

                
                

