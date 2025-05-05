# Valores iniciales
estado_est = 0       # Estimación inicial del estado
error_est = 1        # Incertidumbre inicial

movimiento = 1       # Movimiento por paso
ruido_mov = 0.2      # Ruido en movimiento
ruido_med = 0.5      # Ruido en medición

mediciones = [1.2, 2.3, 2.9, 4.2, 5.1]  # Datos "reales" con ruido

print("📈 Filtro de Kalman en 1D:\n")

for i, medicion in enumerate(mediciones):
    # PREDICCIÓN
    estado_pred = estado_est + movimiento
    error_pred = error_est + ruido_mov

    # ACTUALIZACIÓN
    ganancia_kalman = error_pred / (error_pred + ruido_med)
    estado_est = estado_pred + ganancia_kalman * (medicion - estado_pred)
    error_est = (1 - ganancia_kalman) * error_pred

    print(f" Paso {i+1}")
    print(f"  Medición: {medicion:.2f}")
    print(f"  Estimación: {estado_est:.2f}")
    print(f"  Incertidumbre: {error_est:.2f}\n")
