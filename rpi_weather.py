# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import get_weather_lib
import datetime


from form_ui import Ui_Form


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #set timer for time
        self.timer_time = QtCore.QTimer(self)
        self.timer_time.setInterval(1000)
        self.timer_time.timeout.connect(self.update_time)
        self.timer_time.start()

        #set timer for weather
        self.timer_weather = QtCore.QTimer(self)
        self.timer_weather.setInterval(1000)
        self.timer_weather.timeout.connect(self.update_weather)
        self.timer_weather.start()

    def update_time(self):
        cur_time = QtCore.QDateTime.currentDateTime()
        self.ui.dateTimeEdit_time.setDateTime(cur_time)

    def update_weather(self):
        cur_weather = get_weather_lib.cur_weather()
        cur_weather.get_weather()
        self.ui.lcdNumber_temp.display(float(cur_weather.get_temp()))
        self.ui.lcdNumber_hum.display(float(cur_weather.get_hum()))
        self.ui.lcdNumber_pres.display(float(cur_weather.get_pres()))

        title, descr = cur_weather.get_weather_text()
        self.ui.label_weather_text.setText(title)
        self.ui.label_weather_descr_text.setText(descr)

        self.ui.label_cloud_text.setText(str(cur_weather.get_clouds()))

        speed, dest = cur_weather.get_wind_text()
        self.ui.label_wind_speed_text.setText(str(speed))
        self.ui.label_wind_dest_text.setText(str(dest))

        date_of_data = datetime.datetime.fromtimestamp(cur_weather.get_timestamp())
        self.ui.label_time_date.setText(str(date_of_data) + ' UTC')

    # http://stackoverflow.com/questions/5506781/pyqt4-application-on-windows-is-crashing-on-exit
    def closeEvent(self, event):
        sys.exit(0)


app = QtGui.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())