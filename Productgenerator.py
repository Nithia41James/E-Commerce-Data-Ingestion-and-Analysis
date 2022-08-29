from faker import Faker
from datetime import datetime
from fileinput import close
import csv
import random

#Global variables
ng_list = []
cities = []

payment_type = ["Card", "Internet Banking", "UPI", "Wallet"]

states = []

ecommerce_website_name = [
    "Car Max",
    "AutoTrader",
    "Carvana",
    "Carfax",
    "eBay"
]

fake = Faker('en_US')


def main():
    cities_array()
    states_array()

    with open("product_file.csv", "w") as f:
        f.write("order_id,customer_id,customer_name,product_id,product_name,product_category,payment_type,quantity,price,datetime,city,country(state),ecommerce_website_name,payment_txn_id,payment_txn_success,failure_reason\n")

        for i in range(12500):

            ###### O_ID, C_ID, C_NAME
            x = random.randint(1, 25)
            if x == 1:
                f.write("{}, 1, John Smith,".format(i))
            elif x == 2:
                f.write("{}, 2, Mary Jane,".format(i))
            elif x == 3:
                f.write("{}, 3 ,Alexander Hopkins,".format(i))
            elif x == 4:
                f.write("{}, 4, Rashid Matthews,".format(i))
            elif x == 5:
                f.write("{}, 5, Brandon Johnson,".format(i))
            elif x == 6:
                f.write("{}, 6, Alex Poppins,".format(i))
            elif x == 7:
                f.write("{}, 7, Calvin Harris,".format(i))
            elif x == 8:
                f.write("{}, 8, Justin Thomas,".format(i))
            elif x == 9:
                f.write("{}, 9, Chloe Howells,".format(i))
            elif x == 10:
                f.write("{}, 10, Max Halloway,".format(i))
            elif x == 11:
                f.write("{}, 11, Chris Jones,".format(i))
            elif x == 12:
                f.write("{}, 12, Eric Kemsley,".format(i))
            elif x == 13:
                f.write("{}, 13, James Rodriguez,".format(i))
            elif x == 14:
                f.write("{}, 14, Kumar Singh,".format(i))
            elif x == 15:
                f.write("{}, 15, Micheal Smith,".format(i))
            elif x == 16:
                f.write("{}, 16, Dave Hernandez,".format(i))
            elif x == 17:
                f.write("{}, 17, Maria Garcia,".format(i))
            elif x == 18:
                f.write("{}, 18, Susan Boyle,".format(i))
            elif x == 19:
                f.write("{}, 19, Jordan Brown,".format(i))
            elif x == 20:
                f.write("{}, 20, Ryan Collier,".format(i))
            elif x == 21:
                f.write("{}, 21, Louis Way,".format(i))
            elif x == 22:
                f.write("{}, 22, Jenny Pickard,".format(i))
            elif x == 23:
                f.write("{}, 23, Usamah Khan,".format(i))
            elif x == 24:
                f.write("{}, 24, Amy Barnes,".format(i))
            elif x == 25:
                f.write("{}, 25, Karen Smith,".format(i))





            ##### P_ID, P_Name, P_Category,

            x = random.randint(1, 25)
            if x == 1:
                f.write("100243,F-150,Ford,")
            elif x == 2:
                f.write("100145,Silverado,Chevrolet,")
            elif x == 3:
                f.write("100379,1500,Ram,")
            elif x == 4:
                f.write("200482,RAV4,Toyota,")
            elif x == 5:
                f.write("300479,Camry,Toyota,")
            elif x == 6:
                f.write("200528,Grand Cherokee,Jeep,")
            elif x == 7:
                f.write("100648,Sierra,GMC,")
            elif x == 8:
                f.write("100494,Highlander,Toyota,")
            elif x == 9:
                f.write("300451,Corolla,Toyota,")
            elif x == 10:
                f.write("200122,Equinox,Chevrolet,")
            elif x == 11:
                f.write("200787,CR-V,Honda,")
            elif x == 12:
                f.write("100409,Tacoma,Toyota,")
            elif x == 13:
                f.write("300857,Model Y,Tesla,")
            elif x == 14:
                f.write("200233,Explorer,Ford,")
            elif x == 15:
                f.write("400562,Wrangler,Jeep,")
            elif x == 16:
                f.write("300804,Model 3,Tesla,")
            elif x == 17:
                f.write("200967,Rogue,Nissan,")
            elif x == 18:
                f.write("201081,Tucson,Hyundai,")
            elif x == 19:
                f.write("201137,CX-5,Mazda,")
            elif x == 20:
                f.write("300723,Accord,Honda,")
            elif x == 21:
                f.write("300995,Altima,Nissan,")
            elif x == 22:
                f.write("201278,Outback,Subaru,")
            elif x == 23:
                f.write("200261,Escape,Ford,")
            elif x == 24:
                f.write("200794,HR-V,Honda,")
            elif x == 25:
                f.write("300786,Civic,Honda,")

            ##### Payment Type Quantity

            f.write(payment())
            f.write(",")
            f.write(get_quantity())
            f.write(",")

            ##### Price

            if x == 1:
                f.write("45525.00,")
            elif x == 2:
                f.write("34600.00,")
            elif x == 3:
                f.write("33975.00,")
            elif x == 4:
                f.write("26975.00,")
            elif x == 5:
                f.write("25945.00,")
            elif x == 6:
                f.write("39000.00,")
            elif x == 7:
                f.write("37195.00,")
            elif x == 8:
                f.write("35855.00,")
            elif x == 9:
                f.write("20425.00,")
            elif x == 10:
                f.write("26300.00,")
            elif x == 11:
                f.write("26800.00,")
            elif x == 12:
                f.write("27150.00,")
            elif x == 13:
                f.write("65990.00,")
            elif x == 14:
                f.write("35510.00,")
            elif x == 15:
                f.write("30295.00,")
            elif x == 16:
                f.write("46990.00,")
            elif x == 17:
                f.write("27150.00,")
            elif x == 18:
                f.write("24950.00,")
            elif x == 19:
                f.write("26250.00,")
            elif x == 20:
                f.write("26520.00,")
            elif x == 21:
                f.write("24900.00,")
            elif x == 22:
                f.write("26945.00,")
            elif x == 23:
                f.write("27185.00,")
            elif x == 24:
                f.write("23650.00,")
            elif x == 25:
                f.write("22550.00,")

            ##### DATETIME
            f.write(get_datetime())
            f.write(",")

            #### Website and City / Country(State)

            f.write(locations())
            f.write(",")
            f.write(website())
            f.write(",")



            ####

            if payment_status() == True:
                status = "Y"
                temporary_value = True
            else:
                status = "N"
                temporary_value = False
            reason_for_failure = reason(temporary_value)
              
            f.write(f"{fake.bothify(text='??-######')},{status},{reason_for_failure}")
            f.write("\n")




#Functons
def website(): #Prints webstite name based on values from generated values in ng_list
    x = random.randint(0, 4)
    if x == 0:
        return (ecommerce_website_name[0])
    elif x == 1:
        return (ecommerce_website_name[1])
    elif x == 2:
        return (ecommerce_website_name[2])
    elif x == 3:
        return (ecommerce_website_name[3])
    elif x == 4:
        return (ecommerce_website_name[4])
    else:
        return("NULL")

def number_generator(data, var): #Randomly creates user-defined values and stores into ng_list
    i = data
    n = var
    for each in range(i): 
        x = random.randrange(0,n)
        ng_list.append(x)
    return ng_list

def cities_array(): #Builds the cities array from stored csv file
    with open('cities.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            cities.append(line[0])
        #print(cities)

def states_array(): #Builds the states array from stored csv file
    with open('cities.csv', 'r') as csv_file:    
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            states.append(line[1])
        #print(states)

def locations(): #Prints city and state name based on values from generated values in ng_list
    #UGLY AF, BUT WORKS
    x = random.randint(0, 11)
    if x == 0:
        x = random.randrange(0,4)
        cit_str = str(cities[x])
        st_str = str(states[0])
        fin_str = cit_str + "," + st_str
        return(fin_str)
    elif x == 1:
        x = random.randrange(4,7)
        cit_str = str(cities[x])
        st_str = str(states[4])
        fin_str = cit_str + "," + st_str
        return(fin_str)
    elif x == 2:
        x = random.randrange(7,20)
        cit_str = str(cities[x])
        st_str = str(states[7])
        fin_str = cit_str + "," + st_str
        return(fin_str)
    elif x == 3:
        x = random.randrange(20,26)
        cit_str = str(cities[x])
        st_str = str(states[20])
        fin_str = cit_str + "," + st_str
        return(fin_str)
    elif x == 4:
        x = random.randrange(26,31)
        cit_str = str(cities[x])
        st_str = str(states[26])
        fin_str = cit_str + "," + st_str
        return(fin_str)
    elif x == 5:
        x = random.randrange(31,35)
        cit_str = str(cities[x])
        st_str = str(states[31])
        fin_str = cit_str + "," + st_str
        return(fin_str)
    elif x == 6:
        x = random.randrange(35,38)
        cit_str = str(cities[x])
        st_str = str(states[35])
        fin_str = cit_str + "," + st_str
        return(fin_str)
    elif x == 7:
        x = random.randrange(38,46)
        cit_str = str(cities[x])
        st_str = str(states[38])
        fin_str = cit_str + "," + st_str
        return(fin_str)
    elif x == 8:
        x = random.randrange(46,50)
        cit_str = str(cities[x])
        st_str = str(states[46])
        fin_str = cit_str + "," + st_str
        return(fin_str)
    elif x == 9:
        x = random.randrange(50,58)
        cit_str = str(cities[x])
        st_str = str(states[50])
        fin_str = cit_str + "," + st_str
        return(fin_str)
    elif x == 10:
        x = random.randrange(58,63)
        cit_str = str(cities[x])
        st_str = str(states[58])
        fin_str = cit_str + "," + st_str
        return(fin_str)
    elif x == 11:
        x = random.randrange(63,67)
        cit_str = str(cities[x])
        st_str = str(states[63])
        fin_str = cit_str + "," + st_str
        return(fin_str)

# Status of the payment (Success or Failed)
def payment_status():
    range = random.randint(0, 100)
    if range < 80:
        return True
    else:
        return False

# Failure reasons
def reason(success):
    if success == False:
        reasons = ["The payment gateway does not support", "Merchant account blocks the transaction", "The billing address is invalid ", "Credit or debit card is expired ", "Credit or debit card is canceled", "Incorrect Pin", "The consumers account is suspended or closed "]
        rof = random.choice(reasons)
        return f"{rof}"
    else:
        return ""

# CSV generation
def datagenerate(records, headers):
    fake = Faker('en_US')
    with open("Payment_data.csv", 'w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):   
            if payment_status() == True:
                status = "Y"
                temporary_value = True
            else:
                status = "N"
                temporary_value = False
            reason_for_failure = reason(temporary_value)
              
            writer.writerow({
                    "payment_txn_id" : fake.bothify(text='??-######'),
                    "payment_txn_success" : status,
                    "failure_reason" : reason_for_failure                   
                    })



#!Generates a random date from a range of two dates
def get_datetime():
    date_time = []
    initial = datetime(2021, 1, 1)
    final = datetime(2021, 12, 30) 
    random_date = initial + (final - initial) * random.random()
    random_date = random_date.strftime("%m-%d-%Y %H:%M:%S")
    date_time = random_date
    return date_time

#!Generates a random payment type from the list of payment options
def payment():
    p_type = []
    random_payment = random.SystemRandom()
    pay = random_payment.choice(payment_type)
    p_type = pay
    return p_type

#!Generates a random product quantity
def get_quantity():
    qt = []
    qty = (random.random()*20 + 1).__round__()
    qt = str(qty)
    return qt
get_quantity()


if __name__ == "__main__":
    main()