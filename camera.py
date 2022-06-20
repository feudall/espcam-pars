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

    def resolution(self, resol):
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
        working_range = (2, 1, 0, -1, -2)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от -2 до 2 включительно')
        res = requests.get(f'http://{self.ip}/control?var=brightness&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def contrast(self, val):
        working_range = (2, 1, 0, -1, -2)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от -2 до 2 включительно')
        res = requests.get(f'http://{self.ip}/control?var=contrast&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def saturation(self, val):
        working_range = (2, 1, 0, -1, -2)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от -2 до 2 включительно')
        res = requests.get(f'http://{self.ip}/control?var=saturation&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def special_effect(self, val):
        working_range = (0, 1, 2, 3, 4, 5, 6)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 6 включительно')
        res = requests.get(f'http://{self.ip}/control?var=special_effect&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def avb(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=awb&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def avb_gain(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=awb_gain&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def wb_mode(self, val):
        working_range = (0, 1, 2, 3, 4)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 4 включительно')
        res = requests.get(f'http://{self.ip}/control?var=wb_mode&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def aec_sensor(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=aec&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def aec_dsp(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=aec2&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def ae_level(self, val):
        working_range = (2, 1, 0, -1, -2)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=ae_level&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def exposure(self, val):

        if val > 1200 or val < 0:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1200 включительно')
        res = requests.get(f'http://{self.ip}/control?var=aec_value&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def agc(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=agc&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def gain(self, val):

        if val > 30 or val < 0:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=agc_gain&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def bpc(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=bpc&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def wpc(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=wpc&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def raw_gma(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=raw_gma&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def lens_correction(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=lenc&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def h_mirror(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=hmirror&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def v_flip(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=vflip&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def dcw(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=dcw&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def color_bar(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=colorbar&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def face_detection(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=face_detect&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code

    def face_recognition(self, val):
        working_range = (0, 1)
        if val not in working_range:
            raise MyException('значение вне диапазона. Используйте значение от 0 до 1 включительно')
        res = requests.get(f'http://{self.ip}/control?var=face_recognize&val={val}')
        if res.status_code == 200:
            time.sleep(1)
            return res.status_code
        else:
            return res.status_code


if __name__ == '__main__':
    cam = Camera('192.168.171.193')
    cam.resolution(13)
    # cam.resolution(5)
    # cam.quality(5)
    # cam.quality(60)
    # cam.brightness(-1)
    # cam.brightness(2)
    # cam.contrast(-2)
    # cam.contrast(2)
    # cam.saturation(-2)
    # cam.saturation(2)
    # cam.special_effect(4)
    # cam.special_effect(0)
    # cam.avb(1)
    # cam.avb(0)
    # cam.avb_gain(0)
    # cam.avb_gain(1)
    # cam.aec_sensor(1)
    # cam.exposure(1100)
    cam.get_images('qqwe.jpg')
