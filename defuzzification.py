from membership import member

def defuzzifikasi(output):
    total_bobot_nilai = 0.0
    total_bobot = 0.0

    for z in range(0, 101):
        low = min(output['low'], member(z, 0, 0, 50))
        medium = min(output['medium'], member(z, 30, 50, 70))
        high = min(output['high'], member(z, 50, 100, 100))

        derajat_member = max(low, medium, high)
        total_bobot_nilai += derajat_member * z
        total_bobot += derajat_member

    return total_bobot_nilai / total_bobot if total_bobot != 0 else 0.0
