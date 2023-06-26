#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = [0]
    newlist *= list_length
    div = 0
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        finally:
            newlist[i] = div
    return newlist
