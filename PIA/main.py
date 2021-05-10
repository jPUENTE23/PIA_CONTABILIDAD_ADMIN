import json

lista_po = list()
totales_semestre = list()

'''print("PRESUPUESTO MAESTRO")
nombre_empresa = input("Nombre de la empresa: ")'''
while True:
    print("[1]. Presupuesto de Operacion")
    print("[2]. Presupuesto Financiero")
    opcion = int(input("Opcion :"))
    if opcion == 1:
        print("\n")
        estado_po = False
        while True:
            print("[1]. Presupuesto de Ventas")
            print("[2]. Determinación del saldo de Clientes y Flujo de Entradas")
            print("[3]. Presupuesto de Producción")
            print("[4]. Presupuesto de Requerimiento de Materiales")
            print("[5]. Presupuesto de Compra de Materiales")
            print("[6]. Determinación del saldo de Proveedores y Flujo de Salidas")
            print("[7]. Presupuesto de Mano de Obra Directa")
            print("[8]. Presupuesto de Gastos Indirectos de Fabricación")
            print("[9]. Presupuesto de Gastos de Operación")
            print("[10]. Determinación del Costo Unitario de Productos Terminados")
            print("[11]. Valuación de Inventarios Finales")
            print("[12]. Concluir con el Presupuesto Financiero")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                print("\n")
                for pro in range(2):
                    producto = {}
                    nombre_product = input("Ingrese el nombre del producto: ")
                    for semestre in range(2):

                        semestre = {}

                        _semestre = int(input("Semestre: "))
                        semestre["Semestre"] = _semestre

                        und_vender = int(input("Unidades a Vender: "))
                        semestre["Unidades a Vender"] = und_vender

                        precio_ventas = int(input("Precio de Venta: "))
                        semestre["Precio de Venta"] = precio_ventas

                        importe_De_venta1 = und_vender * precio_ventas
                        semestre["Importe de Venta"] = importe_De_venta1

                        totales_semestre.append(importe_De_venta1)
                        total_sem = sum(totales_semestre)

                        producto[nombre_product] = semestre
                        lista_po.append(producto)

                        semestre = {}
                        producto = {}

                        print("\n")

                _total_smestre = {}



                for termino in lista_po:
                    print(termino)