# Write your code below:
def trip_planner_welcome(name):
    print('Welcome to tripplanner v1.0' + name)


def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print('Your trip starts off in' + origin)
    print('And you are traveling to' + destination)
    print('You will be traveling by' + mode_of_transport)
    print('It will take approximately' + str(estimated_time), + 'hours')


def estimated_time_rounded(estimated_time):
    rounded_time = estimated_time
    return rounded_time


trip_planner_welcome('Wade')
destination_setup('Butte', 'New York', int('15'), 'Plane')
estimated_time_rounded('15')

# Uncomment these in the last step
# trip_planner_welcome(" <YOUR NAME HERE> ")
# estimate = estimated_time_rounded(2.43)
# destination_setup(" <PICK A ORIGIN> ", "<PICK A DESTINATION > ", estimate, "Car")
