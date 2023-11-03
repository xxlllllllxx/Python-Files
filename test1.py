num = 9651627255
#name = "Lewis Daveriel Masallo"

num_format = "{:011d}"


print(f"format using (num :011d) : {num :011d}")
print("format using (:011d).format(num)",num_format.format(num))
print("format using str(num).rjust(11, '0')", str(num).rjust(11, '0'))
#print(name)


