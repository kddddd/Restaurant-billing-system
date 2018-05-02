from tkinter import *
import random
import time;

# to intialise tkinter we need to create tk root widget which is an ordinary window contains title bar amn other decoration and only one root is provided for each program
root = Tk()
# size of window
root.geometry("1600x800+0+0")
root.title("Restaurant biling system")

text_Input = StringVar()
operator = ""

# frames of a window

Tops = Frame(root, width=1600, height=70, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=1400, height=1200, bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

# time
localtime = time.asctime(time.localtime(time.time()))
# info
lbleinfo = Label(Tops, font=('aerial', 50), text="RESTAURANT BILLING SYSTEM")
lbleinfo.grid(row=0, column=0)

lbleinfo = Label(Tops, font=('aerial', 20,), text=localtime)
lbleinfo.grid(row=1, column=0)


def display(event):
    kd = open('kd.txt', 'r')
    kd_list = []
    j = 0
    s = kd.readlines()
    for i in s:
        l = s[j].split()
        j += 1
        kd_list.append(l)
    print(kd_list)
    global count
    if count <= len(kd) - 1:
        kd1.set(kd_list[count][0])
        kd2.set(kd_list[count][1])
        kd3.set(kd_list[count][2])
        kd4.set(kd_list[count][3])
        kd5.set(kd_list[count][4])
        count += 1
        kd.close()
    else:
        count = 0


def record_added():
    l8 = Label(root, text='Record Added')
    l8.grid(row=20, columns=3)


def updated():
    l8 = Label(root, text='Record Updated')
    l8.grid(row=20, columns=3)


def add():
    kd = open('kd.txt', 'a')
    reference = kd1.get()
    pizzameal = kd2.get()
    filetofishmeal = kd3.get()
    zangomeal = kd4.get()
    chickenmeal = kd5.get()
    drinks = kd6.get()
    servicetax = kd7.get()
    discount = kd8.get()
    total = kd9.get()
    subtotal = kd10.get()

    text = "\n"+reference +" "+pizzameal+" "+chickenmeal+" "+filetofishmeal+" "+zangomeal+" "+drinks+" "+servicetax+" "+subtotal+" "+total+" "+discount
    kd.write(text)
    kd1.set("")
    kd2.set("")
    kd3.set("")
    kd4.set("")
    kd5.set("")
    kd6.set("")
    kd7.set("")
    kd8.set("")
    kd9.set("")
    kd10.set("")


def display_first():
    import re
    kd = open('kd.txt', 'r')
    s = kd.readline()
    string = re.sub(' +', ' ', s)
    l = string.split()
    kd1.set(l[0])
    kd2.set(l[1])
    kd3.set(l[2])
    kd4.set(l[3])
    kd5.set(l[4])
    kd6.set(l[5])
    kd7.set(l[6])
    kd8.set(l[7])
    kd9.set(l[8])
    kd10.set(l[9])
    kd.close()


def display_last():
    kd = open('kd.txt', 'r')
    for i in kd:
        s = i
    string = re.sub(' +', ' ', s)
    l = string.split()
    kd1.set(l[0])
    kd2.set(l[1])
    kd3.set(l[2])
    kd4.set(l[3])
    kd5.set(l[4])
    kd6.set(l[5])
    kd7.set(l[6])
    kd8.set(l[7])
    kd9.set(l[8])
    kd10.set(l[9])
    kd.close()


def delete():
    kd = open('kd.txt', 'r')
    ref = kd1.get()
    s = kd.readlines()
    kd.close();
    kd = open('kd.txt','w')
    for i in  s :
        x =i.split()
        if (x[0] != ref) :
            kd.write(i)
    kd1.set("")
    kd2.set("")
    kd3.set("")
    kd4.set("")
    kd5.set("")
    kd6.set("")
    kd7.set("")
    kd8.set("")
    kd9.set("")
    kd10.set("")
    kd.close()


def update():
    kd = open('kd.txt', 'r')
    ref = kd1.get()
    line = kd.readlines()
    sd = False

    for i in line :
        f = i.split()
        if (sd == True) :
            kd1.set(f[0])
            kd2.set(f[1])
            kd3.set(f[2])
            kd4.set(f[3])
            kd5.set(f[4])
            kd6.set(f[5])
            kd7.set(f[6])
            kd8.set(f[7])
            kd9.set(f[8])
            kd10.set(f[9])
        if (f[0] == ref) :
            sd =True


def Ref():
    x = random.randint(10000, 100000)
    kd15 = str(x)
    kd1.set(kd15)

    copm = float(kd2.get())
    cofof = float(kd3.get())
    cocm = float(kd4.get())
    cozm = float(kd5.get())
    cod = float(kd6.get())

    costofpizzameal = copm * 299
    costofiletoffish = cofof * 399
    costofchickenmeal = cocm * 299
    costofzangomeal = cozm * 199
    costofdrinks = cod * 99

    S = float(costofpizzameal + costofiletoffish + costofchickenmeal + costofzangomeal + costofdrinks)
    discountamount = float((S) - ((S) * 0.8))
    print(discountamount)
    servicecharge = (S * 0.18)
    totalamount = "Rs" + str(int(S) + int(servicecharge))

    kd7.set(servicecharge)
    kd8.set(totalamount)
    kd10.set(S)
    kd9.set(discountamount)

    Subtotal.set(S)
    Servicectax.set(servicecharge)
    Discount.set(discountamount)
    Total.set(int(subtotal) + int(servicetax))


def exitt():
    root.destroy()


def Reset():
    kd1.set("")
    kd2.set("")
    kd3.set("")
    kd4.set("")
    kd5.set("")
    kd6.set("")
    kd7.set("")
    kd8.set("")
    kd9.set("")
    kd10.set("")


kd1 = StringVar()
kd2 = StringVar()
kd3 = StringVar()
kd4 = StringVar()
kd5 = StringVar()
kd6 = StringVar()
kd7 = StringVar()
kd8 = StringVar()
kd9 = StringVar()
kd10 = StringVar()

lblreference = Label(f1, font=('aerial', 20, 'bold'), text='Reference', anchor='w')
lblreference.grid(row=0, column=0)
txtreference = Entry(f1, font=('aerial', 20, 'bold'), textvariable=kd1, insertwidth=4, justify='right')
txtreference.grid(row=0, column=1)

lblpizzameal = Label(f1, font=('aerial', 20, 'bold'), text='Pizza meal', anchor='w')
lblpizzameal.grid(row=1, column=0)
txtpizzameal = Entry(f1, font=('aerial', 20, 'bold'), textvariable=kd2, insertwidth=4, justify='right')
txtpizzameal.grid(row=1, column=1)

lblfiletofishmeal = Label(f1, font=('aerial', 20, 'bold'), text='Filet-o-fish', anchor='w')
lblfiletofishmeal.grid(row=1, column=2)
txtfiletofishmeal = Entry(f1, font=('aerial', 20, 'bold'), textvariable=kd3, insertwidth=4, justify='right')
txtfiletofishmeal.grid(row=1, column=3)

lblChickenmeal = Label(f1, font=('aerial', 20, 'bold'), text='Chicken meal', anchor='w')
lblChickenmeal.grid(row=2, column=0)
txtChickenmeal = Entry(f1, font=('aerial', 20, 'bold'), textvariable=kd4, insertwidth=4, justify='right')
txtChickenmeal.grid(row=2, column=1)

lblZangomeal = Label(f1, font=('aerial', 20, 'bold'), text='Zango meal', anchor='w')
lblZangomeal.grid(row=2, column=2)
txtZangomeal = Entry(f1, font=('aerial', 20, 'bold'), textvariable=kd5, insertwidth=4, justify='right')
txtZangomeal.grid(row=2, column=3)

lbldrinks = Label(f1, font=('aerial', 20, 'bold'), text='Drinks', anchor='w')
lbldrinks.grid(row=3, column=0)
txtdrinks = Entry(f1, font=('aerial', 20, 'bold'), textvariable=kd6, insertwidth=4, justify='right')
txtdrinks.grid(row=3, column=1)

lblServicetax = Label(f1, font=('aerial', 20, 'bold'), text='Service tax', anchor='w')
lblServicetax.grid(row=4, column=0)
txtServicetax = Entry(f1, font=('aerial', 20, 'bold'), textvariable=kd7, insertwidth=4, justify='right')
txtServicetax.grid(row=4, column=1)

lbltotal = Label(f1, font=('aerial', 20, 'bold'), text='Total Amount', anchor='w')
lbltotal.grid(row=6, column=0)
txttotal = Entry(f1, font=('aerial', 20, 'bold'), textvariable=kd8, insertwidth=4, justify='right')
txttotal.grid(row=6, column=1)

lblDiscount = Label(f1, font=('aerial', 20, 'bold'), text='Discount', anchor='w')
lblDiscount.grid(row=5, column=2)
txtDiscount = Entry(f1, font=('aerial', 20, 'bold'), textvariable=kd9, insertwidth=4, justify='right')
txtDiscount.grid(row=5, column=3)

lblsubtotalamount = Label(f1, font=('aerial', 20, 'bold'), text='Sub Total', anchor='w')
lblsubtotalamount.grid(row=5, column=0)
txtsubtotalamount = Entry(f1, font=('aerial', 20, 'bold'), textvariable=kd10, insertwidth=4, justify='right')
txtsubtotalamount.grid(row=5, column=1)

btnTotal = Button(f1, padx=4, pady=4, fg='black', font=('aerial', 20, 'bold'), width=10, bd=16, command=Ref,
                  text='Total')
btnTotal.grid(row=13, column=0)

btnexit = Button(f1, padx=4, pady=4, fg='black', font=('aerial', 20, 'bold'), width=10, bd=16, command=exitt,
                 text='Exit')
btnexit.grid(row=13, column=1)

btnfirstbill = Button(f1, padx=4, pady=4, fg='black', font=('aerial', 20, 'bold'), width=10, bd=16,
                      command=display_first, text='firstbill')
btnfirstbill.grid(row=14, column=0)

btnlastbill = Button(f1, padx=4, pady=4, fg='black', font=('aerial', 20, 'bold'), width=10, bd=16, command=display_last,
                     text='lastbill')
btnlastbill.grid(row=14, column=1)

btnupdate = Button(f1, padx=4, pady=4, fg='black', font=('aerial', 20, 'bold'), width=10, bd=16, command=update,
                   text='Updatebill')
btnupdate.grid(row=15, column=0)

btnDelete = Button(f1, padx=4, pady=4, fg='black', font=('aerial', 20, 'bold'), width=10, bd=16, command=delete,
                   text='Delete')
btnDelete.grid(row=15, column=1)

btnAdd = Button(f1, padx=4, pady=4, fg='black', font=('aerial', 20, 'bold'), width=10, bd=16, command=add,
                text='AddBill')
btnAdd.grid(row=15, column=2)

btnReset = Button(f1, padx=4, pady=4, fg='black', font=('aerial', 20, 'bold'), width=10, bd=16, command=Reset,
                  text='Reset')
btnReset.grid(row=15, column=3)

root.mainloop()
