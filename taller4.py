import tkinter as tk
from tkinter import messagebox, ttk
import logging
import re
from abc import ABC, abstractmethod

logging.basicConfig(
    filename='software_fj_sistema.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class EntidadSistema(ABC):
    @abstractmethod
    def obtener_id_unico(self): pass

class Cliente(EntidadSistema):
    def __init__(self, email):
        self.__email = None 
        self.email = email
    @property
    def email(self): return self.__email
    @email.setter
    def email(self, valor):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, valor.strip()): raise ValueError("Email inválido.")
        self.__email = valor.strip()
    def obtener_id_unico(self): return self.__email

class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre, self.precio_base = nombre, precio_base
    @abstractmethod
    def calcular_costo(self, horas, dias=0): pass

class Sala(Servicio):
    def calcular_costo(self, horas, dias=0): return (int(dias) * 8 * self.precio_base) + (int(horas) * self.precio_base)
class Equipo(Servicio):
    def calcular_costo(self, horas, dias=0): return int(((int(dias) * 8 * self.precio_base) + (int(horas) * self.precio_base)) * 0.90)
class Asesoria(Servicio):
    def calcular_costo(self, horas, dias=0): return int(((int(dias) * 8 * self.precio_base) + (int(horas) * self.precio_base)) * 1.19)

class Reserva:
    def __init__(self, cliente, servicio, dias, horas):
        if int(dias) == 0 and int(horas) == 0:
            raise ValueError("El tiempo no puede ser 0 días y 0 horas.")
        self.cliente, self.servicio, self.dias, self.horas = cliente, servicio, dias, horas
    def procesar(self):
        return self.servicio.calcular_costo(self.horas, self.dias)

class AppSoftwareFJ:
    def __init__(self, root):
        self.root = root
        self.root.title("Software FJ")
        self.root.geometry("520x750")
        self.root.configure(bg="#2c3e50")
        self.registros_memoria = []
        self.catalogo = {
            "Reservas de Salas": ["Microelectrónica", "Networking", "Estudio Grupal"],
            "Alquiler de Equipos": ["Estación Calor", "Osciloscopio", "Multímetro"],
            "Asesorías Especializadas": ["Lógica Programación", "PCB Design", "Sistemas Op."]
        }
        self.crear_widgets()

    def crear_widgets(self):
        estilo = {"bg": "#2c3e50", "fg": "#ecf0f1", "font": ("Arial", 10, "bold")}
        tk.Label(self.root, text="SOFTWARE FJ - GESTIÓN", font=("Arial", 14, "bold"), bg="#2c3e50", fg="#f1c40f").pack(pady=20)
        
        tk.Label(self.root, text="Correo Electrónico:", **estilo).pack()
        self.ent_email = tk.Entry(self.root, width=40, font=("Arial", 11)); self.ent_email.pack(pady=5)
        
        f_dom = tk.Frame(self.root, bg="#2c3e50"); f_dom.pack()
        for d in ["@gmail.com", "@hotmail.com", "@outlook.com"]:
            tk.Button(f_dom, text=d, font=("Arial", 8), bg="#34495e", fg="#bdc3c7", relief="flat", command=lambda dom=d: self.completar_email(dom)).pack(side="left", padx=3)

        tk.Label(self.root, text="Categoría:", **estilo).pack(pady=(10,0))
        self.cb_cat = ttk.Combobox(self.root, values=list(self.catalogo.keys()), state="readonly", width=37); self.cb_cat.pack(pady=5)
        self.cb_cat.bind("<<ComboboxSelected>>", lambda e: self.actualizar_items(self.cb_cat, self.cb_item))
        
        tk.Label(self.root, text="Item:", **estilo).pack()
        self.cb_item = ttk.Combobox(self.root, state="readonly", width=37); self.cb_item.pack(pady=5)

        f_t = tk.Frame(self.root, bg="#2c3e50"); f_t.pack(pady=15)
        tk.Label(f_t, text="Días:", **estilo).grid(row=0, column=0, padx=5)
        self.cb_dias = ttk.Combobox(f_t, values=[str(i) for i in range(32)], state="readonly", width=5); self.cb_dias.set("0"); self.cb_dias.grid(row=0, column=1, padx=5)
        tk.Label(f_t, text="Horas:", **estilo).grid(row=0, column=2, padx=5)
        self.cb_horas = ttk.Combobox(f_t, values=[str(i) for i in range(25)], state="readonly", width=5); self.cb_horas.set("1"); self.cb_horas.grid(row=0, column=3, padx=5)

        tk.Button(self.root, text="GUARDAR REGISTRO", command=self.guardar, bg="#27ae60", fg="white", font=("Arial", 10, "bold"), width=35).pack(pady=10)
        tk.Button(self.root, text="VER LISTADO / REPORTES", command=self.abrir_reporte, bg="#2980b9", fg="white", font=("Arial", 10, "bold"), width=35).pack(pady=5)
        tk.Button(self.root, text="REINICIAR TODO", command=self.reset_total, bg="#c0392b", fg="white", font=("Arial", 10, "bold"), width=35).pack(pady=20)

    def completar_email(self, dominio):
        actual = self.ent_email.get().split('@')[0]
        if actual: self.ent_email.delete(0, tk.END); self.ent_email.insert(0, actual + dominio)

    def actualizar_items(self, c_cat, c_item):
        c_item['values'] = self.catalogo[c_cat.get()]; c_item.set('')

    def guardar(self):
        try:
            cl = Cliente(self.ent_email.get())
            cat, item = self.cb_cat.get(), self.cb_item.get()
            if not item: raise ValueError("Seleccione un Item.")
            res = Reserva(cl, self.obtener_serv(cat, item), self.cb_dias.get(), self.cb_horas.get())
            total = res.procesar()
            self.registros_memoria.append({"email": cl.email, "cat": cat, "item": item, "dias": self.cb_dias.get(), "horas": self.cb_horas.get(), "total": total})
            messagebox.showinfo("Éxito", f"Guardado.\nTotal: ${total}"); self.limpiar()
        except Exception as e: messagebox.showwarning("Error", str(e))

    def obtener_serv(self, cat, item):
        precios = {"Reservas de Salas": 5000, "Alquiler de Equipos": 4500, "Asesorías Especializadas": 8000}
        clases = {"Reservas de Salas": Sala, "Alquiler de Equipos": Equipo, "Asesorías Especializadas": Asesoria}
        return clases[cat](item, precios[cat])

    def limpiar(self):
        self.ent_email.delete(0, tk.END); self.cb_cat.set(''); self.cb_item.set(''); self.cb_dias.set("0"); self.cb_horas.set("1")

    def reset_total(self):
        if messagebox.askyesno("Confirmar", "¿Desea eliminar TODA la base de datos?"): 
            self.registros_memoria = []
            logging.info("Base de datos reiniciada.")
            self.limpiar()

    def abrir_reporte(self):
        v = tk.Toplevel(self.root); v.title("Reportes"); v.geometry("900x500")
        cols = ("Email", "Categoría", "Item", "Días", "Horas", "Total")
        self.tabla = ttk.Treeview(v, columns=cols, show='headings')
        for c in cols: self.tabla.heading(c, text=c); self.tabla.column(c, width=140)
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
        f = tk.Frame(v); f.pack(fill="x", padx=10, pady=10)
        tk.Button(f, text="✎ MODIFICAR", bg="#16a085", fg="white", font=("Arial", 9, "bold"), command=self.abrir_modificador).pack(side="left", padx=5)
        tk.Button(f, text="🗑 BORRAR", bg="#e67e22", fg="white", command=self.borrar_fila).pack(side="left", padx=5)
        tk.Button(f, text="📊 VENTAS", bg="#27ae60", fg="white", command=lambda: messagebox.showinfo("Ventas", f"Total: ${sum(r['total'] for r in self.registros_memoria)}")).pack(side="right", padx=5)
        self.refrescar_tabla()

    def refrescar_tabla(self):
        for i in self.tabla.get_children(): self.tabla.delete(i)
        for r in self.registros_memoria: self.tabla.insert("", tk.END, values=(r['email'], r['cat'], r['item'], r['dias'], r['horas'], f"${r['total']}"))

    def borrar_fila(self):
        sel = self.tabla.selection()
        if not sel:
            messagebox.showwarning("Atención", "Seleccione un registro.")
            return
        if messagebox.askyesno("Confirmar", "¿Eliminar registro?"):
            idx = self.tabla.index(sel)
            logging.info(f"Eliminado: {self.registros_memoria[idx]['email']}")
            del self.registros_memoria[idx]
            self.refrescar_tabla()

    def abrir_modificador(self):
        sel = self.tabla.selection()
        if not sel: return
        idx = self.tabla.index(sel); datos = self.registros_memoria[idx]
        vm = tk.Toplevel(); vm.title("Editor"); vm.geometry("400x550")
        
        tk.Label(vm, text=f"Editando: {datos['email']}", font=("Arial", 11, "bold")).pack(pady=15)
        tk.Label(vm, text="Categoría:").pack(); cb_c = ttk.Combobox(vm, values=list(self.catalogo.keys()), state="readonly", width=30); cb_c.set(datos['cat']); cb_c.pack(pady=5)
        tk.Label(vm, text="Nuevo Item:").pack(); cb_i = ttk.Combobox(vm, values=self.catalogo[datos['cat']], state="readonly", width=30); cb_i.set(datos['item']); cb_i.pack(pady=5)
        cb_c.bind("<<ComboboxSelected>>", lambda e: self.actualizar_items(cb_c, cb_i))
        
        tk.Label(vm, text="Días:").pack(); md = ttk.Combobox(vm, values=[str(i) for i in range(32)], state="readonly", width=15); md.set(datos['dias']); md.pack(pady=5)
        tk.Label(vm, text="Horas:").pack(); mh = ttk.Combobox(vm, values=[str(i) for i in range(25)], state="readonly", width=15); mh.set(datos['horas']); mh.pack(pady=5)

        def confirmar():
            try:
                cl_fake = Cliente(datos['email'])
                res_check = Reserva(cl_fake, self.obtener_serv(cb_c.get(), cb_i.get()), md.get(), mh.get())
                self.registros_memoria[idx].update({'cat':cb_c.get(), 'item':cb_i.get(), 'dias':md.get(), 'horas':mh.get(), 'total':res_check.procesar()})
                self.refrescar_tabla(); vm.destroy()
            except Exception as e: messagebox.showerror("Error", str(e))
            
        tk.Button(vm, text="APLICAR", bg="#27ae60", fg="white", font=("Arial", 10, "bold"), command=confirmar, width=15, relief="raised").pack(pady=30)

if __name__ == "__main__":
    root = tk.Tk(); AppSoftwareFJ(root); root.mainloop()