import tkinter as tk

def wyswietl_komunikat():
    okno = tk.Tk()
    okno.title("Komunikat")
    
    # Ustawienie koloru tła
    okno.configure(bg='#F0F0F0')  # Domyślnie szary, możesz dostosować kolor według własnych preferencji
    
    # Utworzenie etykiety z pogrubionym tekstem
    etykieta = tk.Label(okno, text="Błędne dane logowania", font=('Helvetica', 12, 'bold'), bg='#F0F0F0')
    etykieta.pack(padx=20, pady=20)
    
    # Utworzenie przycisku
    przycisk = tk.Button(okno, text="Zamknij", command=okno.destroy)
    przycisk.pack(pady=10)
    
    okno.mainloop()

# Wywołanie funkcji
wyswietl_komunikat()

