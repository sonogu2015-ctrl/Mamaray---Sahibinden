import math

# Marmaray istasyonları (örnek başlangıç listesi)
stations = [
    ("Halkalı", 41.0008, 28.7931),
    ("Bakırköy", 40.9807, 28.8721),
    ("Yenikapı", 41.0054, 28.9496),
    ("Üsküdar", 41.0256, 29.0152),
    ("Bostancı", 40.9633, 29.0951),
    ("Kartal", 40.9030, 29.1822),
    ("Pendik", 40.8783, 29.2331),
    ("Gebze", 40.8000, 29.4300)
]

def distance(lat1, lon1, lat2, lon2):
    R = 6371000

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c


def near_station(lat, lon):

    for name, s_lat, s_lon in stations:

        d = distance(lat, lon, s_lat, s_lon)

        if d <= 500:
            return name, d

    return None


def test():

    lat = 40.9807
    lon = 28.8721

    result = near_station(lat, lon)

    if result:
        print("Yakın istasyon:", result)
    else:
        print("Uygun değil")


if __name__ == "__main__":
    test()
