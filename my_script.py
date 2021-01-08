# hello_file = open("hello.txt", "w")
# ga_intro = "Hello to all of my GA family"
# hello_file.write(ga_intro)
# print(hello_file.read())
# hello_file.close()


# car_file = open("car.txt", "w")
# new_car_list = 'Tesla Model S\nMercedes C300\nToyota Camry'
# car_file.write(new_car_list)
# print(car_file.read())
# car_file.close()

# create a file
# my_new_file = open("person.txt", "w")
# my_new_file.write('Alex Bustillos')
# my_new_file.close()

# # person_file = open("person.txt")
# # print(person_file.read())
# # person_file.close()

# with open('person.txt', 'w') as person_file:
#     person_file.write('Killua')

# # append to a file
# with open('person.txt', 'a') as person_file:
#     person_file.write('\nGon\nKurapika\nANOTHAONE')

# with open('person.txt') as people:
#     people_list = people.readlines()

#     for each_person in people_list:
#         print(each_person)




# txt_list = hello_file.read().split(' ')
# print(txt_list)

with open('prime_numbers.txt', 'r+') as multiply_file:
    
    for each_number in multiply_file:
        print(int(each_number) * 2)
        
    # def multiply_by_two(num):
    #     print(num * 2)
    # multiply_by_two(multiply_file)

# with open('one_to_hundred.txt', 'r+') as iterate_file:
#     for each_element in iterate_file:
        