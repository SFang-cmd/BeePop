from math import exp
import numpy as np
np.set_printoptions(threshold=np.inf)

dE_list = np.array([])
dL_list = np.array([])
dP_list = np.array([])
dW_list = np.array([])
dD_list = np.array([])

# dE_list = []
# dLP_list = []
# dW_list = []
# dD_list = []

dE = 0
num_eggs = []
num_larva = []
num_pups = []
num_work = [30000]
num_drone = [500]
percent_work = 0.985
percent_drone = 0.015
total_bees = [num_work[0] + num_drone[0]]
cannibalism_larva = [0.23, 0.3, 0.58, 0.06, 0]

s_E = 0.97
s_L = 0.99
s_P = 0.999
s_W = 0.985
s_D = 0.985

days_E = 3
days_L = 5
days_P = 12
days_W = 21
days_D = 21

season1 = 0
season2 = 0

x1 = 385
x2 = 30
x3 = 36
x4 = 155
x5 = 30
sum = 0

egg_max = 1600

for t in range(4000):
    season1 = 1 - (1/(1 + (x1 * exp(-2 * (t%365)/x2))))
    season2 = 1/(1 + x3 * exp(-2 * (((t%365) - x4)/x5)))

    dE = egg_max * (1 - np.maximum(season1, season2))
    dE_list = np.append(dE_list, dE)
    dL_list = np.append(dL_list, dE_list[t - days_E] if t - days_E >= 0 else 0)
    dP_list = np.append(dP_list, dL_list[t - days_L] if t - days_L >= 0 else 0)
    dW_list = np.append(dW_list, percent_work * dP_list[t - days_P] if t - days_P >= 0 else 0)
    dD_list = np.append(dD_list, percent_drone * dP_list[t - days_P] if t - days_P >= 0 else 0)

    if(t == 0):
        dW_list[0] = num_work[0]
        dD_list[0] = num_drone[0]
    

    if t - days_E >= 0:
        dE_list[t - days_E] = 0
    if t - days_L >= 0:
        dL_list[t - days_L] = 0 
    if t - days_P >= 0:
        dL_list[t - days_P] = 0 
    if t - days_W >= 0:
        dW_list[t - days_W] = 0 
    if t - days_D >= 0:
        dD_list[t - days_D] = 0 

    dE_list = dE_list * s_E
    dL_list = dL_list * s_L
    dP_list = dP_list * s_P
    dW_list = dW_list * s_W
    dD_list = dD_list * s_D

    num_eggs.append(np.sum(dE_list))
    num_larva.append(np.sum(dL_list))
    num_pups.append(np.sum(dP_list))
    num_work.append(np.sum(dW_list))
    num_drone.append(np.sum(dD_list))
    sum = np.sum(dE_list) + np.sum(dL_list) + np.sum(dP_list) + np.sum(dW_list) + np.sum(dD_list)
    total_bees.append(sum)

    if(sum > 50000):
        dL_list[t - 1] = dL_list[t - 1] * (1 - 0.23)
        dL_list[t - 2] = dL_list[t - 2] * (1 - 0.3)
        dL_list[t - 3] = dL_list[t - 3] * (1 - 0.58)
        dL_list[t - 4] = dL_list[t - 4] * (1 - 0.06)

    if((t % 365) == 160 and sum > 50000):
        dW_list = dW_list * 0.5
        dD_list = dD_list * 0.5

    if((t % 365) == 200 and sum > 50000):
        dW_list = dW_list * 0.5
        dD_list = dD_list * 0.5

    # np.multiply(dE_list, s_E)
    # np.multiply(dLP_list, s_LP)
    # np.multiply(dW_list, s_W)
    # np.multiply(dD_list, s_D)

    # dE_list.append(1500)
    # dLP_list.append(dE_list(t - 2) if t - 2 >= 0 else 0)
    # dW_list.append(percent_work * dLP_list(t - 11) if t - 11 >= 0 else 0)
    # dD_list.append(percent_drone * dLP_list(t - 11) if t - 11 >= 0 else 0)
    # dE_list = dE_list * 2
print("Day")
# print(dE_list)
# print(dL_list)
# print(dP_list)
# print(dW_list)
# print(dD_list)
print(total_bees)