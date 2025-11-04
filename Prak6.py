import tkinter as tk
top = tk.Tk()
top.title("Aplikasi Prediksi Pilihan Prodi ")
top.geometry("400x300")
lbl_judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan", font=("times new roman", 12))
lbl_judul.pack(pady=10)
entries=[]
for i in range(1, 11):
    label = tk.Label(top, text=f"Masukkan Nilai {i}:", bg="white")
    label.pack(side=tk.TOP, pady=3)

    entry = tk.Entry(top, bd=5)
    entry.pack(side=tk.TOP, pady=3)
    
    entries.append(entry)  
def tampilkan_hasil():
    nilai = [e.get() for e in entries]  
    hasil_text = f"Nilai yang dimasukkan: {', '.join(nilai)}"
    
    hasil_label.config(text=hasil_text)
tombol = tk.Button(top, text="Tampilkan Hasil", command=tampilkan_hasil)
tombol.pack(pady=10)

hasil_label = tk.Label(top, text="", font=("Arial", 12), bg="white")
hasil_label.pack(pady=10)


top.mainloop()