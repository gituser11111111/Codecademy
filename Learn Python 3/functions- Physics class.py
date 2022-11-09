# Uncomment this when you reach the "Use the Force" section
# train_mass = 22680
# train_acceleration = 10
# train_distance = 100
# bomb_mass = 1


# Write your code below:
def f_to_c(f_temp, c_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100,())

def c_to_f(c_temp, f_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp

c0_in_farenheit = c_to_f(0,())

def get_force(mass,acceleration):
  return mass * acceleration

train_mass = 22680
train_acceleration = 10

train_force = get_force(train_mass, train_acceleration)
print(train_force)

x = train_force

print('The GE train supplies ' + str(x) + ' Newtons of force')

def get_energy(mass, c):
  c = 3*10**8
  return mass * (c**2)

c = 3*10**8
bomb_mass = 1

bomb_energy = get_energy(bomb_mass, c)

print(bomb_energy)

x = bomb_energy

print('A 1kg bomb supplies ', + x , ' Joules')

def get_work(mass,acceleration,distance):
  force = get_force(train_mass,train_acceleration) * train_distance
  return force

train_distance = 100

get_work(train_mass,train_acceleration,train_distance)

train_work = get_work(train_mass,train_acceleration,train_distance)
print(train_work)

x = str(train_work)
y = str(train_distance)

print('The GE train does ', x + ' Joules of work over', y + ' meters.')





