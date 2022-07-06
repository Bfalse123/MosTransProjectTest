from geopy.distance import geodesic
import data

with open('results.txt', 'w', encoding="utf-8") as file:
    file.write(f"Название ЖК\tНазвание остановки\tРасстояние\n")
    for complex in data.residential_complexes:
        ansforcomplex = []
        for stop in data.complex_stops[complex['name']]:
            distance = geodesic((stop[data.LONGITUDE_KEY], stop[data.latitudekey]), (complex[data.LONGITUDE_KEY], complex[data.latitudekey])).meters
            if distance <= 1000:
                #убираем личшние данные которые выходят за предел радиуса в 1км
                #т.е. по углам квадрата допустимых значений
                ansforcomplex.append([complex['name'], stop['name'], distance])
        
        ansforcomplex.sort(key= lambda x: x[2])
        for ans in ansforcomplex:
            file.write('\t'.join(map(str, ans)))
            file.write("\n")    
