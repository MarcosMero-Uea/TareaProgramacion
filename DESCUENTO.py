
'calcula el descuento'
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

'Calcula el IVA sobre el monto dado.'
def calcular_iva(monto, porcentaje_iva=15):
    iva = (porcentaje_iva / 100) * monto
    return iva


# Programa principal para simular la factura
def generar_factura(monto_compra):
    # Cálculo del subtotal, IVA y total sin descuento
    subtotal = monto_compra
    iva = calcular_iva(subtotal)
    total_sin_descuento = subtotal + iva

    # Cálculo del descuento (10% predeterminado)
    descuento = calcular_descuento(total_sin_descuento, 10)

    # Cálculo del monto final a pagar (después del descuento)
    valor_a_cancelar = total_sin_descuento - descuento

    # Mostrar la factura
    print("\n===== Factura =====")
    print(f"Subtotal:             ${subtotal:.2f}")
    print(f"IVA (15%):            ${iva:.2f}")
    print(f"Total sin descuento:  ${total_sin_descuento:.2f}")
    print(f"Descuento (10%):      -${descuento:.2f}")
    print(f"Valor a cancelar:     ${valor_a_cancelar:.2f}")
    print("====================\n")


# Solicitar el monto de la compra al usuario
try:
    monto_compra = float(input("Ingrese el sub-total de la compra: "))
    generar_factura(monto_compra)
except ValueError:
    print("Por favor, ingrese un valor numérico válido.")

