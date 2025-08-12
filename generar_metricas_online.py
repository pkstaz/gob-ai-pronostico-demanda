import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Rango de fechas cada 30 minutos desde 1 junio 2025 hasta 11 agosto 2025
fecha_inicio = datetime(2025, 6, 1, 0, 0)
fecha_fin = datetime(2025, 8, 11, 23, 30)
fechas = pd.date_range(fecha_inicio, fecha_fin, freq='30T')

rows = []
for fecha_hora in fechas:
    # Tramites online: simula variabilidad y picos
    base_tramites = random.randint(5, 50)
    if fecha_hora.hour in [9, 10, 11, 14, 15, 16]:
        tramites_online = base_tramites + random.randint(20, 80)
    else:
        tramites_online = base_tramites + random.randint(-5, 10)
    # CPU usage: 10-95% con picos y valles
    cpu_usage = round(np.clip(np.random.normal(50, 20), 10, 95), 2)
    # RAM usage: 1-32 GB
    ram_usage = round(np.clip(np.random.normal(8, 6), 1, 32), 2)
    # Storage usage: 100-1000 GB
    storage_usage = round(np.clip(np.random.normal(500, 200), 100, 1000), 2)
    # Input bytes: 1MB-100MB
    input_bytes = round(np.clip(np.random.normal(20, 15), 1, 100), 2) * 1024 * 1024
    # Output bytes: 1MB-100MB
    output_bytes = round(np.clip(np.random.normal(20, 15), 1, 100), 2) * 1024 * 1024
    rows.append({
        'fecha_hora': fecha_hora.strftime('%Y-%m-%d %H:%M'),
        'tramites_online': tramites_online,
        'cpu_usage': cpu_usage,
        'ram_usage': ram_usage,
        'storage_usage': storage_usage,
        'input_bytes': int(input_bytes),
        'output_bytes': int(output_bytes)
    })

pd.DataFrame(rows).to_csv('metricas_tramites_online.csv', index=False)
print('Archivo metricas_tramites_online.csv generado correctamente.')
