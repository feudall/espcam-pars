import requests
import time

class Camera():

    def __init__(self, ip):
        self.ip = ip

    def __repr__(self):
        return self.ip

    def __str__(self):
        return self.ip

    def get_images(self, nameFile):
        '''
        получение картинки с камеры по ip и сохранение в файл
        :param nameFile: имя файла
        :return: статус ответа
        '''

        res = requests.get(f'http://{self.ip}/capture?_cb=')
        if res.status_code == 200:
            with open(nameFile, 'wb') as file:
                file.write(res.content)
            return res.status_code
        else:
            return res.status_code

    def resolution(self , resol):
        '''
        настройка разрешения камеры
        таблица соответствия
        пиклели = значение
        96х96 = 0
        160х120 = 1
        176х144 = 2
        240х176 = 3
        240х240 = 4
        320х240 = 5
        400х296 = 6
        480х320 = 7
        640х480 = 8
        800х600 = 9
        1024х768 = 10
        1280х720 = 11
        1280х1024 = 12
        1600х1200 = 13
        :param resol: int
        :return: статус
        '''
        res = requests.get(f'http://{self.ip}/control?var=framesize&val={resol}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code


    def quality(self, val):
        '''
        настройка качества
        принимает значения от 4 до 63 включительно
        :param val: int
        :return: статус
        '''

        if val > 63 or val < 4:
            raise MyException('значение вне диапазона. Используйте значение от 4 до 63 включительно')
        res = requests.get(f'http://{self.ip}/control?var=quality&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code


    def brightness(self, val):
        working_range = (2,1,0,-1,-2)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от -2 до 2 включительно')
        res = requests.get(f'http://{self.ip}/control?var=brightness&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code


    def contrast(self, val):
        working_range = (2,1,0,-1,-2)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от -2 до 2 включительно')
        res = requests.get(f'http://{self.ip}/control?var=contrast&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code


    def saturation(self, val):
        working_range = (2,1,0,-1,-2)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от -2 до 2 включительно')
        res = requests.get(f'http://{self.ip}/control?var=saturation&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code



cam1 = Camera('192.168.171.193')

print(cam1.quality(5))
