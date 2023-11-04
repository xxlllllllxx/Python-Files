import test5_module as tm

# print(tm.global_x)
# print(tm.setup())
# print(tm.App().setup())
# print(tm.global_x)


# print(dt.datetime.now().hour)


st1 = tm.Student(birthday=[2002, 6, 6], name="Lewis")

# Calling the data method
print(st1.data())
print(st1.data().name)
print(st1.data().birthday)
