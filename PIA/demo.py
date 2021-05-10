
''''
diccionario = {"Presupuesto de venta":
              {"CE":
                    {"semestre":1,
                    "unidades a vender":12000,
                    "Precio de venta":300,
                    "Importe de venta":36000
                    },
                    "Total de ventas por semestestre":
                    {"1er semestre":80000,
                        "2do semestre":2000000,
                        "Total en el año":800010.}}}'''



import json

lista_po = list()
totales_semestre = list()
PresupuestoVentas = {}
basejson = list()

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
                    producto_gral = {}
                    totales_sem = {}
                    print("1ER SEMESTRE")
                    print("\n")
                    nombre_product = input("Ingrese el nombre del producto: ")

                    semestre = {}
                    productosem1 = {}

                    psemestre = 1

                    und_vender = int(input("Unidades a Vender: "))
                    semestre["Unidades a Vender"] = und_vender

                    precio_ventas = int(input("Precio de Venta: "))
                    semestre["Precio de Venta"] = precio_ventas

                    importe_De_venta1 = und_vender * precio_ventas
                    semestre["Importe de Venta"] = importe_De_venta1

                    totales_semestre.append(importe_De_venta1)

                    productosem1[psemestre] = semestre

                    print("\n")
                    print("2DO SEMESTRE")
                    print("\n")

                    semestre2 = {}
                    productosem2 = {}

                    ssemestre = 2

                    _und_vender = int(input("Unidades a Vender: "))
                    semestre2["Unidades a Vender"] = _und_vender

                    _precio_ventas = int(input("Precio de Venta: "))
                    semestre2["Precio de Venta"] = _precio_ventas

                    _importe_De_venta1 = _und_vender * _precio_ventas
                    semestre2["Importe de Venta"] = _importe_De_venta1

                    totales_semestre.append(_importe_De_venta1)

                    productosem2[ssemestre] = semestre2

                    tota_proSem = sum(totales_semestre)
                    totales_sem["Totales del Año"] = tota_proSem

                    producto_gral[nombre_product] = productosem1,productosem2,totales_sem

                    lista_po.append(producto_gral)

                    # vaciado de las liststa y diccionario utilizados
                    semestre = {}
                    productosem1 = {}
                    semestre2 = {}
                    productosem2 = {}
                    producto_gral = {}
                    totales_sem = {}
                    totales_semestre = []

                    print("\n")

                PresupuestoVentas["Presupuesto de Ventas"] = lista_po
                basejson.append(PresupuestoVentas)

                with open("Presupuesto de ventas.json",'w') as archivo:
                    json.dump(basejson,archivo)
                    print("La cedula de Presupuesto de Ventas se genero exitosamente")
                    print("\n")

                #for termino in lista_po:
                    #print(termino)