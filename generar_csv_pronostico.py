import pandas as pd
from datetime import datetime, timedelta

# Parámetros
fecha_inicio = datetime(2024, 8, 12)
fecha_fin = datetime(2025, 8, 11)

# Días festivos (ejemplo, puedes ajustar)

# Días festivos nacionales de Argentina para 2024 y 2025
dias_festivos = [
    # 2024
    '2024-01-01', '2024-02-12', '2024-02-13', '2024-03-24', '2024-03-29', '2024-03-30',
    '2024-04-02', '2024-05-01', '2024-05-25', '2024-06-17', '2024-06-20', '2024-07-09',
    '2024-08-19', '2024-10-14', '2024-11-18', '2024-12-08', '2024-12-25',
    # 2025
    '2025-01-01', '2025-03-03', '2025-03-04', '2025-03-24', '2025-04-18', '2025-04-19',
    '2025-04-02', '2025-05-01', '2025-05-25', '2025-06-16', '2025-06-20', '2025-07-09',
    '2025-08-18', '2025-10-13', '2025-11-17', '2025-12-08', '2025-12-25'
]

# Generar datos
fechas = pd.date_range(fecha_inicio, fecha_fin)
rows = []
for fecha in fechas:
    dia_semana = fecha.strftime('%A')
    dia_semana_es = {
        'Monday': 'Lunes', 'Tuesday': 'Martes', 'Wednesday': 'Miércoles',
        'Thursday': 'Jueves', 'Friday': 'Viernes', 'Saturday': 'Sábado', 'Sunday': 'Domingo'
    }[dia_semana]
    es_festivo = fecha.strftime('%Y-%m-%d') in dias_festivos or dia_semana_es == 'Domingo'
    # Simulación de trámites atendidos
    import random
    if es_festivo:
        tramites = 0
    else:
        base = 200 + (fecha.month - 8) * 10
        # Variación semanal y aleatoria
        if dia_semana_es == 'Martes':
            tramites = base + 50 + random.randint(-20, 40)
        elif dia_semana_es == 'Lunes':
            tramites = base + 20 + random.randint(-15, 30)
        elif dia_semana_es == 'Viernes':
            tramites = base - 10 + random.randint(-30, 20)
        elif dia_semana_es == 'Sábado':
            tramites = base - 100 + random.randint(-20, 20)
        elif dia_semana_es == 'Miércoles':
            tramites = base + random.randint(-10, 25)
        elif dia_semana_es == 'Jueves':
            tramites = base + random.randint(-15, 20)
        else:
            tramites = base + random.randint(-10, 10)
    rows.append({
        'fecha': fecha.strftime('%Y-%m-%d'),
        'tramites_atendidos': tramites,
        'dia_semana': dia_semana_es,
        'dia_festivo': es_festivo
    })

# Guardar CSV
pd.DataFrame(rows).to_csv('datos_sucursal.csv', index=False)
print('Archivo datos_sucursal.csv generado correctamente.')
