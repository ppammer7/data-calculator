print("Last updated on 29.06.2022 0:49")
print("")
print("Welcome to Data Calculator! v1.0")
print("")
print("With this Program you can calculate your network speed.")
print("")
print("Bits/s = bit")
print("Kilobits/s = kbit")
print("Megabits/s = mbit")
print("Gigabits/s = gbit")
print("")
unit = input("In which unit do you want to enter your network speed? ... ")

if unit == "bit":

    print("")
    bit = input("Now enter your bits per second ... ")

    kbit = int(bit) / 1000
    mbit = int(bit) / 1000000
    gbit = int(bit) / 1000000000
    byte = int(bit) / 8
    kbyte = int(kbit) / 8
    mbyte = int(mbit) / 8
    gbyte = int(gbit) / 8

    print("")
    print("")
    print("Gigabit/s: " + str(gbit) + "")
    print("")
    print("Megabit/s: " + str(mbit) + "")
    print("")
    print("Kilobit/s: " + str(kbit) + "")
    print("")
    print("Bit/s: " + str(bit) + "")

    print("")
    print("")

    print("Gigabyte/s: " + str(gbyte) + "")
    print("")
    print("Megabyte/s: " + str(mbyte) + "")
    print("")
    print("Kilobyte/s: " + str(kbyte) + "")
    print("")
    print("Byte/s: " + str(byte) + "")

    print("")
    print("")
    print("")

    print("© 2022 Paul Pammer")

    input("")

if unit == "kbit":

        print("")
        kbit = input("Now enter your kbits per second ... ")

        bit = int(kbit) * 1000
        mbit = int(kbit) / 1000
        gbit = int(kbit) / 1000000
        byte = int(bit) / 8
        kbyte = int(kbit) / 8
        mbyte = int(mbit) / 8
        gbyte = int(gbit) / 8

        print("")
        print("")
        print("Gigabit/s: " + str(gbit) + "")
        print("")
        print("Megabit/s: " + str(mbit) + "")
        print("")
        print("Kilobit/s: " + str(kbit) + "")
        print("")
        print("Bit/s: " + str(bit) + "")

        print("")
        print("")

        print("Gigabyte/s: " + str(gbyte) + "")
        print("")
        print("Megabyte/s: " + str(mbyte) + "")
        print("")
        print("Kilobyte/s: " + str(kbyte) + "")
        print("")
        print("Byte/s: " + str(byte) + "")

        print("")
        print("")
        print("")

        print("© 2022 Paul Pammer")

        input("")

if unit == "mbit":

        print("")
        mbit = input("Now enter your mbits per second ... ")

        bit = int(mbit) * 1000000
        kbit = int(mbit) * 1000
        gbit = int(mbit) / 1000
        byte = int(bit) / 8
        kbyte = int(kbit) / 8
        mbyte = int(mbit) / 8
        gbyte = int(gbit) / 8

        print("")
        print("")
        print("Gigabit/s: " + str(gbit) + "")
        print("")
        print("Megabit/s: " + str(mbit) + "")
        print("")
        print("Kilobit/s: " + str(kbit) + "")
        print("")
        print("Bit/s: " + str(bit) + "")

        print("")
        print("")

        print("Gigabyte/s: " + str(gbyte) + "")
        print("")
        print("Megabyte/s: " + str(mbyte) + "")
        print("")
        print("Kilobyte/s: " + str(kbyte) + "")
        print("")
        print("Byte/s: " + str(byte) + "")

        print("")
        print("")
        print("")

        print("© 2022 Paul Pammer")

        input("")

if unit == "gbit":

    print("")
    gbit = input("Now enter your gbits per second ... ")

    bit = int(gbit) * 1000000000
    kbit = int(gbit) * 1000000
    mbit = int(gbit) * 1000
    byte = int(bit) / 8
    kbyte = int(kbit) / 8
    mbyte = int(mbit) / 8
    gbyte = int(gbit) / 8

    print("")
    print("")
    print("Gigabit/s: " + str(gbit) + "")
    print("")
    print("Megabit/s: " + str(mbit) + "")
    print("")
    print("Kilobit/s: " + str(kbit) + "")
    print("")
    print("Bit/s: " + str(bit) + "")

    print("")
    print("")

    print("Gigabyte/s: " + str(gbyte) + "")
    print("")
    print("Megabyte/s: " + str(mbyte) + "")
    print("")
    print("Kilobyte/s: " + str(kbyte) + "")
    print("")
    print("Byte/s: " + str(byte) + "")

    print("")
    print("")
    print("")

    print("© 2022 Paul Pammer")

    input("")


