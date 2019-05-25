def gen_ip(w_begin, w_end, x_begin, x_end, y_begin, y_end, z_begin, z_end):
    list_ip = list()
    for a1 in range(int(w_begin), int(w_end) + 1):
        for a2 in range(int(x_begin), int(x_end) + 1):
            for a3 in range(int(y_begin), int(y_end) + 1):
                for a4 in range(int(z_begin), int(z_end) + 1):
                    list_ip.append(str(a1) + '.' + str(a2) + '.' + str(a3) + '.' + str(a4))
    return list_ip


for a in gen_ip(192, 192, 168, 168, 1, 3, 1, 5):
    print(a)
