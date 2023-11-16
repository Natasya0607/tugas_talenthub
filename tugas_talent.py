class Suhu:
    def kelvin_ke_celsius(self, kelvin):
        self.celsius = kelvin - 273.15
        return self.celsius

    def celsius_ke_kelvin(self, celsius):
        self.kelvin = celsius + 273.15
        return self.kelvin

    def suhu_ke_fahrenheit(self, suhu, jenis):
        if jenis == 'C':
            suhu_kelvin = self.celsius_ke_kelvin(suhu)
        elif jenis == 'K':
            suhu_kelvin = suhu
        else:
            raise ValueError("Jenis suhu tidak valid.")
        
        fahrenheit = (suhu_kelvin - 273.15) * 9/5 + 32
        return fahrenheit

    def fahrenheit_ke_suhu(self, fahrenheit, jenis):
        suhu_celsius = (fahrenheit - 32) * 5/9

        if jenis == 'C':
            return suhu_celsius
        elif jenis == 'K':
            return self.celsius_ke_kelvin(suhu_celsius)
        else:
            raise ValueError("Jenis suhu tidak valid.")
