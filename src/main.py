import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import constants as cn


class Application(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, padding=10, **kwargs)

        self.scan_type = "box"
        self.current_np = ""
        self.pz_number = 0

        ttk.Style().configure("TButton", font="TkFixedFont 12")
        self.pack(fill=BOTH, expand=YES)
        self.grid_columnconfigure(
            (0, 1, 2, 3, 4, 5), weight=1, uniform="column")

        self.captura = ttk.Entry(self)
        self.captura.grid(row=0, column=0, columnspan=3)

        self.np_number = ttk.Label(self, text="0")
        self.np_number.grid(row=1, column=3, columnspan=3)

        self.num_parte = ttk.Label(self, text="Numero de Parte")
        self.num_parte.grid(row=1, column=0, columnspan=3)

        # Keys
        self.captura.bind('<Return>', self.captureItem)

    def captureItem(self, event):
        codigo = self.captura.get()
        self.captura.delete(0, 'end')
        if codigo == "":
            return

        if self.scan_type == "box":
            np = codigo[-10:]
            if np in cn.np_codes:
                self.num_parte.config(text=np)
                self.current_np = np
        else:
            pz = codigo[2:13]
            pz.replace("-", "")
            if pz == self.current_np:
                self.pz_number += 1

                self.np_number.config(text=str(self.pz_number))


if __name__ == "__main__":

    app = ttk.Window(
        title="Calculator",
        themename="litera",
        size=(350, 600),
        resizable=(False, False),
    )
    Application(app)
    app.mainloop()
