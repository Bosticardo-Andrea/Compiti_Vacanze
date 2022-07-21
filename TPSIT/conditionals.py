
def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500:return (temperature * neutrons_emitted) < 5e5
    else:return False
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    if efficiency >= 80:return 'green'
    if efficiency >= 60:return 'orange'
    if efficiency >= 30:return 'red'
    else:return 'black'
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    criticality = temperature * neutrons_produced_per_second
    low = 0.9 * threshold
    high = 1.1 * threshold
    if temperature * neutrons_produced_per_second < low:return 'LOW'
    if low <= criticality <= high:return 'NORMAL'
    else:return 'DANGER'
