import tkinter as tk
import tkinter.messagebox as msg
top = tk.Tk()   
top.title= ("My tkinter window")
top.geometry= ("400x300")
top.configure(bg="blue") #this line will not have any effect since
def pesanHello():
    msg.showinfo("Pesan","bilang yg bagus itu doa loo, hrs sukses kakak bisa kok, kakak tu pinter, tinggal harus bisa lebih lagi upgrade diri kakak hrs keluar dri zona nyaman, emg susah kak adek sndiri aja nguras energi bgt tp harus bisa, klu gk gtu gk ke upgrade diri adek ini, stuck disitu situ aja, branding diri sndiri tu jauh lebih oke dripada gak sama sekali, bodmat org bilang apa ntr nya caper lah apa lah, tu branding kakak nantinya keren, value nya hrs kuat kak!")
tombol = tk.Button(top, text= "Klik saya", command=pesanHello)
tombol = tk.Button(top, text="klik Saya", command=pesanHello)
ChekVar1=tk.IntVar()
ChekVar2=tk.IntVar()
Check1=tk.Checkbutton(top, text="Pilihan 1", variable=ChekVar1)
Check2=tk.Checkbutton(top, text="Pilihan 2", variable=ChekVar2)
Check1.pack()
Check2.pack()
tombol.pack ()#pady=20
L1=tk.Label(top, text ="Masukan nama:")
L1.pack(side=tk.LEFT)
E1=tk.Entry(top, bd=5)
E1.pack(side=tk.RIGHT)
def tampilkanNama():
    nama =E1.get()
    msg.showinfo("Nama Anda",f"Nama Anda Adalah:{nama}")
tombolnama = tk.Button(top, text="Tampilkan Nama",command=tampilkanNama)
tombolnama.pack(side=tk.BOTTOM)
top.mainloop()  