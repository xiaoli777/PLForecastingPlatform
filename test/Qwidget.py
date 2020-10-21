import sys
#import Algorithm.SVM

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class PredictList:
    def __init__(self, date=[], real=[], predict=[], MAPE=0):
        self.date = date
        self.real = real
        self.predict = predict
        self.MAPE = MAPE


class AppForm(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(1000, 900)
        self.setWindowTitle('预测信息')
        self.setWindowIcon(QIcon('Icon\\DataMining.jpg'))

        self.create_menu()
        self.create_main_frame()
        self.create_status_bar()
        self.on_start()

    def save_plot(self):
        file_choices = "PNG (*.png)|*.png"
        path = QFileDialog.getSaveFileName(self,
                                           'Save file', '',
                                           file_choices)
        # if path:
        #    self.canvas.print_figure(path, dpi=self.dpi)
        #    self.statusBar().showMessage('Saved to %s' % path, 2000)

        print(path)

    def on_about(self):
        msg = """ A demo of using PyQt with matplotlib:
         * Use the matplotlib navigation bar
         * Add values to the text box and press Enter (or click "Draw")
         * Show or hide the grid
         * Drag the slider to modify the width of the bars
         * Save the plot to a file using the File menu
         * Click on a bar to receive an informative message
        """
        QMessageBox.about(self, "About the demo", msg.strip())

    def on_start(self):
        start = self.dateTimeEdit_start.dateTime()
        end = self.dateTimeEdit_end.dateTime()
        project_name = self.textbox_project_name.text()
        predict_algorithm = self.comboBox_predict_algorithm.currentText()
        predict_type = self.comboBox_predict_type.currentText()
        startDay = start.toString("yyyy") + "-" + start.toString("MM") + "-" + start.toString("dd")
        endDay = end.toString("yyyy") + "-" + end.toString("MM") + "-" + end.toString("dd")
        i = 1
        if not self.checkBox_History.isChecked():
            i = 0
        if self.checkBox_Holiday.isChecked():
            i = i + 2
        if self.checkBox_Season.isChecked():
            i = i + 4
        print(startDay, endDay, project_name, predict_algorithm, predict_type, i)

        #self.result = Algorithm.SVM.Predict_Main(startDay, endDay, 1, i)

        self.result = PredictList()

        self.axes.clear()
        self.axes.grid(self.grid_cb.isChecked())

        line1, = self.axes.plot(self.result.real, "k", markeredgecolor='k', marker=u'$\circ$',
                                markersize=self.slider.value() / 10.0)
        line2, = self.axes.plot(self.result.predict, "r", markeredgecolor='r', marker=u'$\star$',
                                markersize=self.slider.value() / 10.0)  # diamond

        self.axes.legend((line1, line2), ('real output', 'predict output', 'svm output'), loc='upper left')

        yticks = range(0, 10000, 1000)
        ytickslabel = range(0, 10000, 1000)
        self.axes.set_yticks(yticks)
        self.axes.set_yticklabels(ytickslabel)
        self.axes.set_ylabel(u'Power Load')

        xticks = range(0, len(self.result.date), 1)
        xtickslabel = self.result.date
        self.axes.set_xticks(xticks)
        self.axes.set_xticklabels(xtickslabel)
        self.axes.set_xlabel(u'Date')

        self.axes.set_title('SVM Power Load Real & Predict')

        self.canvas.draw()

    def restart(self):
        self.axes.clear()
        self.axes.grid(self.grid_cb.isChecked())

        line1, = self.axes.plot(self.result.real, "k", markeredgecolor='k', marker=u'$\circ$',
                                markersize=self.slider.value() / 10.0)
        line2, = self.axes.plot(self.result.predict, "r", markeredgecolor='r', marker=u'$\star$',
                                markersize=self.slider.value() / 10.0)  # diamond

        self.axes.legend((line1, line2), ('real output', 'predict output', 'svm output'), loc='upper left')

        yticks = range(0, 10000, 1000)
        ytickslabel = range(0, 10000, 1000)
        self.axes.set_yticks(yticks)
        self.axes.set_yticklabels(ytickslabel)
        self.axes.set_ylabel(u'Power Load')

        xticks = range(0, len(self.result.date), 1)
        xtickslabel = self.result.date
        self.axes.set_xticks(xticks)
        self.axes.set_xticklabels(xtickslabel)
        self.axes.set_xlabel(u'Date')
        self.axes.set_title('SVM Power Load Real & Predict')

        self.canvas.draw()

    def create_main_frame(self):
        self.main_frame = QWidget()

        self.dpi = 100
        self.fig = Figure((10.0, 10.0), dpi=self.dpi)

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)

        self.axes = self.fig.add_subplot(111)

        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

        self.label_project_name = QLabel("项 目 名:")
        self.textbox_project_name = QLineEdit()

        self.label_predict_algorithm = QLabel("预测算法:")
        self.comboBox_predict_algorithm = QComboBox()
        self.comboBox_predict_algorithm.addItem("SVM回归分析")
        self.comboBox_predict_algorithm.addItem("均值修正预测")
        self.comboBox_predict_algorithm.addItem("多元线性回归预测")

        self.label_predict_type = QLabel("预测类型:")
        self.comboBox_predict_type = QComboBox()
        self.comboBox_predict_type.addItem("电力负荷最大值")
        self.comboBox_predict_type.addItem("电力负荷平均值")
        self.comboBox_predict_type.addItem("电力负荷最小值")

        self.label_time_range = QLabel("时间范围:")
        self.dateTimeEdit_start = QDateTimeEdit()
        self.dateTimeEdit_start.setDisplayFormat("yyyy/M/d")
        self.dateTimeEdit_start.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit_start.setMinimumDateTime(QDateTime(QDate(2007, 1, 1), QTime(0, 0, 0)))

        self.dateTimeEdit_end = QDateTimeEdit()
        self.dateTimeEdit_end.setDisplayFormat("yyyy/M/d")
        self.dateTimeEdit_end.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit_end.setMinimumDateTime(QDateTime(QDate(2007, 1, 1), QTime(0, 0, 0)))

        self.label_parameter = QLabel("参数因子:")
        self.checkBox_Season = QCheckBox("季节")
        self.checkBox_Holiday = QCheckBox("节假日")
        self.checkBox_History = QCheckBox("历史因素")
        self.checkBox_History.toggle()

        self.start_button = QPushButton("&开始")
        self.start_button.clicked.connect(self.on_start)

        self.grid_cb = QCheckBox("Show &Grid")
        self.grid_cb.setChecked(False)
        self.grid_cb.stateChanged.connect(self.restart)

        slider_label = QLabel('Bar width (%):')
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(1, 100)
        self.slider.setValue(20)
        self.slider.setTracking(True)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.valueChanged.connect(self.restart)

        hbox_name = QHBoxLayout()
        hbox_name.addWidget(self.label_project_name)
        hbox_name.addWidget(self.textbox_project_name)

        hbox_predict_algorithm = QHBoxLayout()
        hbox_predict_algorithm.addWidget(self.label_predict_algorithm)
        hbox_predict_algorithm.addWidget(self.comboBox_predict_algorithm)

        hbox_predict_type = QHBoxLayout()
        hbox_predict_type.addWidget(self.label_predict_type)
        hbox_predict_type.addWidget(self.comboBox_predict_type)

        hbox_time = QHBoxLayout()
        hbox_time.addWidget(self.label_time_range)
        hbox_time.addWidget(self.dateTimeEdit_start)
        hbox_time.addWidget(self.dateTimeEdit_end)

        hbox_parameter = QHBoxLayout()
        hbox_parameter.addWidget(self.label_parameter)
        hbox_parameter.addWidget(self.checkBox_Season)
        hbox_parameter.addWidget(self.checkBox_Holiday)
        hbox_parameter.addWidget(self.checkBox_History)

        hbox = QHBoxLayout()
        for w in [self.grid_cb, slider_label, self.slider]:
            hbox.addWidget(w)
            hbox.setAlignment(w, Qt.AlignVCenter)

        hbox_start_button = QHBoxLayout()
        hbox_start_button.addWidget(self.start_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.mpl_toolbar)
        vbox.addWidget(self.canvas)
        vbox.addLayout(hbox_name)
        vbox.addLayout(hbox_predict_algorithm)
        vbox.addLayout(hbox_predict_type)
        vbox.addLayout(hbox_time)
        vbox.addLayout(hbox_parameter)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox_start_button)

        self.main_frame.setLayout(vbox)
        #self.setCentralWidget(self.main_frame)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.main_frame)

        self.setLayout(self.mainLayout)

    def create_status_bar(self):
        self.status_text = QLabel("StatusBar")
        self.statusBar().addWidget(self.status_text, 1)

    def create_menu(self):
        self.file_menu = self.menuBar().addMenu("&File")

        load_file_action = self.create_action("&Save plot",
                                              shortcut="Ctrl+S", slot=self.save_plot, icon="save.jpg",
                                              tip="Save the plot")
        quit_action = self.create_action("&Quit", slot=self.close,
                                         shortcut="Ctrl+Q", icon="close.jpg",
                                         tip="Close the application")

        self.add_actions(self.file_menu,
                         (load_file_action, None, quit_action))

        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About",
                                          shortcut='F1', slot=self.on_about, icon="about.jpg",
                                          tip='About the demo')

        self.add_actions(self.help_menu, (about_action,))

    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def create_action(self, text, slot=None, shortcut=None,
                      icon=None, tip=None, checkable=False,
                      signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon("Icon/%s" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action


class PredictWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        stack = QStackedLayout()
        stack.addWidget(AppForm())


def main():
    app = QApplication(sys.argv)
    form = PredictWidget()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
