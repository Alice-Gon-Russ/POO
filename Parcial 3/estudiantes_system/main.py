from estudiantes_paquete import estudiantesBD
from tkinter import Label,Entry,Button,Tk,messagebox


class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestión de Estudiantes")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0,0)
        self.main()
   
    ##.  ... Vistas de Estudiantes ....
    def borrarPantalla(self):
      for widget in self.ventana.winfo_children():
          widget.destroy()
    
    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Estudiantes"
        Label(self.ventana,text=f"\n...::: Menu de {tipo} :::... \n").pack(pady=10)
        Button(self.ventana,text="1.- Agregar",command=self.insertar_view).pack(pady=5)
        Button(self.ventana,text="2.- Borrar",command=self.eliminar_view).pack(pady=5)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_view).pack(pady=5)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_view).pack(pady=5)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=5)
        
    def main(self):
            self.borrarPantalla() 
            Label(self.ventana,text="\n...::: M E N U   P R I N C I P A L :::...").pack(pady=10)    
            Button(self.ventana,text="1.- Estudiantes",command=self.menu_acciones).pack(pady=5) 
            Button(self.ventana,text="2.- Salir",command=self.ventana.quit).pack(pady=5)  
    
    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar los datos del Estudiante...").pack(pady=10)
        
        Label(self.ventana,text="Nombre: ").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)
        
        Label(self.ventana,text="Nota: ").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)
        
        Button(self.ventana,text="Guardar",command=lambda:{self.insertar_controller(),self.insertar_view()}).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)
        
    def eliminar_view(self):
            self.borrarPantalla()
            Label(self.ventana,text="...Ingresar el ID del Estudiante a Eliminar...").pack(pady=10)
            
            Label(self.ventana,text="ID: ").pack(pady=5)
            self.id=Entry(self.ventana)
            self.id.focus()
            self.id.pack(pady=5)
            
            self.btn_buscar=Button(self.ventana,text="Buscar",command=lambda:self.buscar_controller("eliminar"))
            self.btn_buscar.pack(pady=5)
    
            self.btn_eliminar=Button(self.ventana,text="Eliminar",state="disabled",command=lambda:{self.eliminar_controller(),self.eliminar_view()})
            self.btn_eliminar.pack(pady=5)
            
            Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)
        
    def modificar_view(self):
       self.borrarPantalla()
       Label(self.ventana,text="...Ingresar el ID del Estudiante a modificar...").pack(pady=10)
                   
       Label(self.ventana,text="ID: ").pack(pady=5)
       self.id=Entry(self.ventana)
       self.id.focus()
       self.id.pack(pady=5)

       Label(self.ventana,text="Nuevo Nombre: ").pack(pady=5)
       self.nombre=Entry(self.ventana)
       self.nombre.pack(pady=5)
        
       Label(self.ventana,text="Nueva Nota: ").pack(pady=5)
       self.nota=Entry(self.ventana)
       self.nota.pack(pady=5)
        
       Button(self.ventana,text="Guardar",command=lambda:{self.modificar_controller(),self.modificar_view()}).pack(pady=10)
       Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)
       
    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text=" ::: Consultar los Estudiantes :::").pack(pady=10)
        filas=""  
        filas=self.consultar_controller(filas)
        Label(self.ventana,text=f"{'No.':<15}{'ID':<15}{'Nombre':<15}{'Nota':<15}").pack(pady=5)
        Label(self.ventana,text=f"-"*100).pack(pady=5)
        Label(self.ventana,text=f"{filas}").pack(pady=5)
        Label(self.ventana,text=f"-"*100).pack(pady=5)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    def cambiar_estado_btn(self,estado,tipo_accion):
        if estado:
            if tipo_accion=="eliminar":
               self.btn_eliminar.config(state="normal")
            elif tipo_accion=="modificar": 
               self.btn_modificar.config(state="normal") 
        else:
            if tipo_accion=="eliminar":
               self.btn_eliminar.config(state="disabled")
            elif tipo_accion=="modificar":
               self.btn_modificar.config(state="disabled")   
    
    def confirmacion_eliminar(self,tipo):
        resp=messagebox.askquestion(title="...¡Atencion!...",message=f"...¿Desea {tipo} este registro?...")
        if resp=="yes":
           return True
        else:
            return False
    # ... Controlador de Estudiantes ...
    def respuesta_sql(self,respuesta):
            if respuesta:
                messagebox.showinfo(title="... Exitoso ...",message="...¡Accion Realizada con Exito!...")
            else:
                messagebox.showerror(title="...¡ Verifica por favor !...",message="...¡Esta Accion no pudo realizarse en este momento!...")
       
    def insertar_controller(self):
        estudiante1=estudiantesBD.EstudiantesBD(self.nombre.get().upper().strip(),self.nota.get().upper().strip())
        respuesta=estudiante1.insertar()
        self.respuesta_sql(respuesta)
        del estudiante1                 
    
    def eliminar_controller(self):
        id=self.id.get().strip()
        resp=self.confirmacion_eliminar("eliminar")
        if resp:
           respuesta=estudiantesBD.EstudiantesBD.eliminar(id)
        else:
            respuesta=False   
        self.respuesta_sql(respuesta)
  
    def consultar_controller(self,filas):
       registros=estudiantesBD.EstudiantesBD.consultar()
       if len(registros)>0:
            num_estudiantes=1
            for fila in registros:
                filas=filas+f"\n{num_estudiantes:<15}{fila[0]:<15}{fila[1]:<15}{fila[2]:<15}"
                num_estudiantes+=1
       else:
           filas="... ¡No existen datos que mostrar por el momento ...!"
       return filas   
           
    def modificar_controller(self):
        id=self.id.get().strip()
        estudiante1=estudiantesBD.EstudiantesBD(self.nombre.get().upper().strip(),self.nota.get().upper().strip())
        respuesta=estudiante1.actualizar(id)
        self.respuesta_sql(respuesta)
        del estudiante1        

    def buscar_controller(self,tipo_accion):
        id=self.id.get().strip()
        estudiante1=estudiantesBD.EstudiantesBD.buscar(id)
        if len(estudiante1)>0: 
            messagebox.showinfo(title="...¡ Registro Encontrado !...",message=f"...¡El registro fue encontrado con exito, puedes {tipo_accion}!...")
            self.cambiar_estado_btn(True,tipo_accion) 
        else:
            messagebox.showerror(title="...¡ Verifica por favor !...",message=f"...¡El registro no fue encontrado, no es posible {tipo_accion}!...")
            self.cambiar_estado_btn(False,tipo_accion)  
            
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()