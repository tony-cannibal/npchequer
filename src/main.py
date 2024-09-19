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

        self.captura = ttk.Entry(self, justify='center')
        self.captura.grid(row=0, column=0, columnspan=6, sticky="EW")

        self.np_number = ttk.Label(self, text="0")
        self.np_number.grid(row=2, column=3, columnspan=3)

        self.num_parte = ttk.Label(self, text="Numero de Parte")
        self.num_parte.grid(row=2, column=0, columnspan=3)

        self.status = ttk.Label(
            self, text="Escane la caja para empesar.", borderwidth=1)
        self.status.grid(row=4, column=0, columnspan=6)

        self.spacer = ttk.Label(self, text="")
        self.spacer.grid(row=1, column=0, columnspan=6)
        self.spacer2 = ttk.Label(self, text="")
        self.spacer2.grid(row=3, column=0, columnspan=6)

        # Keys
        self.captura.bind('<Return>', self.captureItem)

    def captureItem(self, event):
        codigo = self.captura.get()
        self.captura.delete(0, 'end')
        if codigo == "":
            return

        if self.scan_type == "box":
            np = codigo[-10:]
            print(np)
            if np in cn.np_codes:
                self.num_parte.config(text=cn.codes[np])
                self.current_np = np
                self.scan_type = "piece"
                self.status.config(text="Escanee la Pieza",)
        else:
            pz = codigo[1:13]
            pz = pz.replace("-", "")
            print(pz)
            if pz == self.current_np:
                self.pz_number += 1
                if self.pz_number == 10:
                    self.pz_number = 0
                    self.scan_type = "box"
                    self.np_number.config(text=str(self.pz_number))
                    self.num_parte.config(text="Numero de Parte.")
                    self.status.config(
                        text="Escane la caja para empesar.", bootstyle="default")
                else:
                    self.np_number.config(text=str(self.pz_number))
                    self.status.config(
                        text="Pieza OK.", bootstyle="inverse success")
            else:
                self.status.config(
                    text="Numero de Parte Equivocado.", bootstyle="inverse danger")


if __name__ == "__main__":

    app = ttk.Window(
        title="Verificador De Codigo",
        themename="litera",
        size=(400, 200),
        resizable=(False, False),
    )
    Application(app)
    app.mainloop()
