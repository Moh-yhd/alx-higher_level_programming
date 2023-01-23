#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    j, k = 0, 0
    res_list = []
    for i in range(list_length):
        try:
            result = my_list_1 [j] / my_list_2[k]
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("divion by 0")
            result = 0
        finally:
            j += 1
            k += 1
            res_list.append(result)
    return res_list



