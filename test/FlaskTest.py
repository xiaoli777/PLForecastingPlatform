import sys

from flask import Flask
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.createPreviewGroupBox()
        self.createGeneralOptionGroupBox()
        self.createDatesGroupBox()
        self.createTextFormatsGroupBox()

        self.layout = QGridLayout()
        self.layout.addWidget(self.previewGroupBox, 0, 0)
        self.layout.addWidget(self.generalOptionGroupBox, 0, 1)
        self.layout.addWidget(self.datesGroupBox, 1, 0)
        self.layout.addWidget(self.textFormatsGroupBox, 1, 1)
        self.layout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(self.layout)

        self.previewLayout.setRowMinimumHeight(0, self.calendar.sizeHint().height())
        self.previewLayout.setColumnMinimumWidth(0, self.calendar.sizeHint().width())

        self.setWindowTitle('Calendar Widget')

    def createPreviewGroupBox(self):
        self.previewGroupBox = QGroupBox('PreView')

        self.calendar = QCalendarWidget()
        self.calendar.setMinimumDate(QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QDate(3000, 1, 1))
        self.calendar.setGridVisible(True)

        self.calendar.currentPageChanged.connect(self.reformatCalendarPage)

        self.previewLayout = QGridLayout()
        self.previewLayout.addWidget(self.calendar, 0, 0, Qt.AlignCenter)
        self.previewGroupBox.setLayout(self.previewLayout)

    def createGeneralOptionGroupBox(self):
        self.generalOptionGroupBox = QGroupBox('General Options')

        self.localeCombo = QComboBox()
        curLocaleIndex = -1
        index = 0
        countries = []
        for i in range(QLocale.C, QLocale.LastLanguage+1):
            lang = QLocale(i)
            countries.append(lang.country())
            for j in range(len(countries)):
                country = countries[j]
                label = QLocale.languageToString(lang.language())
                label += '/'
                label += QLocale.countryToString(country)
                locale = QLocale(i, country)
                if self.locale().language() == lang and self.locale().country() == country:
                    curLocaleIndex = index
                self.localeCombo.addItem(label, locale)
                index += 1
        if curLocaleIndex != -1:
            self.localeCombo.setCurrentIndex(curLocaleIndex)
        localeLabel = QLabel('&Locale')
        localeLabel.setBuddy(self.localeCombo)

        self.firstDayCombo = QComboBox()
        self.firstDayCombo.addItem('Sunday', Qt.Sunday)
        self.firstDayCombo.addItem('Monday', Qt.Monday)
        self.firstDayCombo.addItem('Tuesday', Qt.Tuesday)
        self.firstDayCombo.addItem('Wendnesday', Qt.Wednesday)
        self.firstDayCombo.addItem('Thursday', Qt.Thursday)
        self.firstDayCombo.addItem('Friday', Qt.Friday)
        self.firstDayCombo.addItem('Saturday', Qt.Saturday)

        firstDayLabel = QLabel('Wee&k starts on:')
        firstDayLabel.setBuddy(self.firstDayCombo)

        self.selectionModeCombo = QComboBox()
        self.selectionModeCombo.addItem('Single selection', QCalendarWidget.SingleSelection)
        self.selectionModeCombo.addItem('None', QCalendarWidget.NoSelection)

        selectionModeLabel = QLabel('&Selection mode:')
        selectionModeLabel.setBuddy(self.selectionModeCombo)

        gridCheckBox = QCheckBox('&Grid')
        gridCheckBox.setChecked(self.calendar.isGridVisible())

        navigationCheckBox = QCheckBox('&Navigation bar')
        navigationCheckBox.setChecked(True)

        self.horizontalHeaderCombo = QComboBox()
        self.horizontalHeaderCombo.addItem('Single letter day names', QCalendarWidget.SingleLetterDayNames)
        self.horizontalHeaderCombo.addItem('Short day names', QCalendarWidget.ShortDayNames)
        self.horizontalHeaderCombo.addItem('None', QCalendarWidget.NoHorizontalHeader)
        self.horizontalHeaderCombo.setCurrentIndex(1)

        horizontalHeaderLabel = QLabel('&Horizontal header:')
        horizontalHeaderLabel.setBuddy(self.horizontalHeaderCombo)

        self.verticalHeaderCombo = QComboBox()
        self.verticalHeaderCombo.addItem('ISO week numbers', QCalendarWidget.ISOWeekNumbers)
        self.verticalHeaderCombo.addItem('None', QCalendarWidget.NoVerticalHeader)

        verticalHeaderLabel = QLabel('&Vertical header:')
        verticalHeaderLabel.setBuddy(self.verticalHeaderCombo)

        self.localeCombo.currentIndexChanged.connect(self.localeChanged)
        self.firstDayCombo.currentIndexChanged.connect(self.firstDayChanged)
        self.selectionModeCombo.currentIndexChanged.connect(self.selectionModeChanged)
        gridCheckBox.toggled.connect(self.calendar.setGridVisible)
        navigationCheckBox.toggled.connect(self.calendar.setNavigationBarVisible)
        self.horizontalHeaderCombo.currentIndexChanged.connect(self.horizontalHeaderChanged)
        self.verticalHeaderCombo.currentIndexChanged.connect(self.veritcalHeaderChanged)

        checkBoxLayout = QHBoxLayout()
        checkBoxLayout.addWidget(gridCheckBox)
        checkBoxLayout.addStretch()
        checkBoxLayout.addWidget(navigationCheckBox)

        outerLayout = QGridLayout()
        outerLayout.addWidget(localeLabel, 0, 0)
        outerLayout.addWidget(self.localeCombo, 0, 1)
        outerLayout.addWidget(firstDayLabel, 1, 0)
        outerLayout.addWidget(self.firstDayCombo, 1, 1)
        outerLayout.addWidget(selectionModeLabel, 2, 0)
        outerLayout.addWidget(self.selectionModeCombo, 2, 1)
        outerLayout.addLayout(checkBoxLayout, 3, 0, 1, 2)
        outerLayout.addWidget(horizontalHeaderLabel, 4, 0)
        outerLayout.addWidget(self.horizontalHeaderCombo, 4, 1)
        outerLayout.addWidget(verticalHeaderLabel, 5, 0)
        outerLayout.addWidget(self.verticalHeaderCombo, 5, 1)
        self.generalOptionGroupBox.setLayout(outerLayout)

        self.firstDayChanged(self.firstDayCombo.currentIndex())
        self.selectionModeChanged(self.selectionModeCombo.currentIndex())
        self.horizontalHeaderChanged(self.horizontalHeaderCombo.currentIndex())
        self.veritcalHeaderChanged(self.verticalHeaderCombo.currentIndex())

    def createDatesGroupBox(self):
        self.datesGroupBox = QGroupBox('Dates')

        self.minimumDateEdit = QDateEdit()
        self.minimumDateEdit.setDisplayFormat('MMM d yyyy')
        self.minimumDateEdit.setDateRange(self.calendar.minimumDate(), self.calendar.maximumDate())
        self.minimumDateEdit.setDate(self.calendar.minimumDate())

        minimumDateLabel = QLabel('&Minimum Date:')
        minimumDateLabel.setBuddy(self.minimumDateEdit)

        self.currentDateEdit = QDateEdit()
        self.currentDateEdit.setDisplayFormat('MMM d yyyy')
        self.currentDateEdit.setDate(self.calendar.selectedDate())
        self.currentDateEdit.setDateRange(self.calendar.minimumDate(), self.calendar.maximumDate())

        currentDateLabel = QLabel('Current Date:')
        currentDateLabel.setBuddy(self.currentDateEdit)

        self.maximumDateEdit = QDateEdit()
        self.maximumDateEdit.setDisplayFormat('MMM d yyyy')
        self.maximumDateEdit.setDateRange(self.calendar.minimumDate(), self.calendar.maximumDate())
        self.maximumDateEdit.setDate(self.calendar.maximumDate())

        maximumDateLabel = QLabel('Ma&ximum Date:')
        maximumDateLabel.setBuddy(self.maximumDateEdit)

        self.currentDateEdit.dateChanged.connect(self.calendar.setSelectedDate)
        self.calendar.selectionChanged.connect(self.selectDateChanged)
        self.minimumDateEdit.dateChanged.connect(self.minimumDateChanged)
        self.maximumDateEdit.dateChanged.connect(self.maximumDateChanged)

        dateBoxLayout = QGridLayout()
        dateBoxLayout.addWidget(currentDateLabel, 1, 0)
        dateBoxLayout.addWidget(self.currentDateEdit, 1, 1)
        dateBoxLayout.addWidget(minimumDateLabel, 0, 0)
        dateBoxLayout.addWidget(self.minimumDateEdit, 0, 1)
        dateBoxLayout.addWidget(maximumDateLabel, 2, 0)
        dateBoxLayout.addWidget(self.maximumDateEdit, 2, 1)
        dateBoxLayout.setRowStretch(3, 1)

        self.datesGroupBox.setLayout(dateBoxLayout)

    def createTextFormatsGroupBox(self):
        self.textFormatsGroupBox = QGroupBox('Text Formats')

        self.weekdayColorCombo = self.createColorComboBox()
        self.weekdayColorCombo.setCurrentIndex(self.weekdayColorCombo.findText('Black'))

        weekdayColorLabel = QLabel('&Weekday color:')
        weekdayColorLabel.setBuddy(self.weekdayColorCombo)

        self.weekendColorCombo = self.createColorComboBox()
        self.weekendColorCombo.setCurrentIndex(self.weekdayColorCombo.findText('Red'))

        weekendColorLabel = QLabel('Week&end color:')
        weekendColorLabel.setBuddy(self.weekendColorCombo)

        self.headerTextFormatCombo = QComboBox()
        self.headerTextFormatCombo.addItem('Bold')
        self.headerTextFormatCombo.addItem('Italic')
        self.headerTextFormatCombo.addItem('Plain')

        headerTextFormatLabel = QLabel('&Header text:')
        headerTextFormatLabel.setBuddy(self.headerTextFormatCombo)

        self.firstFridayCheckBox = QCheckBox('&First Friday in blue')

        self.mayFirstCheckBox = QCheckBox('May &1 in red')

        self.weekendColorCombo.currentIndexChanged.connect(self.weekdayFormatChanged)
        self.weekendColorCombo.currentIndexChanged.connect(self.reformatCalendarPage)
        self.weekendColorCombo.currentIndexChanged.connect(self.weekendFormatChanged)
        self.weekendColorCombo.currentIndexChanged.connect(self.reformatCalendarPage)
        self.headerTextFormatCombo.currentIndexChanged.connect(self.reformatHeaders)
        self.firstFridayCheckBox.toggled.connect(self.reformatCalendarPage)
        self.mayFirstCheckBox.toggled.connect(self.reformatCalendarPage)

        checkBoxLayout = QHBoxLayout()
        checkBoxLayout.addWidget(self.firstFridayCheckBox)
        checkBoxLayout.addStretch()
        checkBoxLayout.addWidget(self.mayFirstCheckBox)

        outerLayout = QGridLayout()
        outerLayout.addWidget(weekdayColorLabel, 0, 0)
        outerLayout.addWidget(self.weekdayColorCombo, 0, 1)
        outerLayout.addWidget(weekendColorLabel, 1, 0)
        outerLayout.addWidget(self.weekendColorCombo, 1, 1)
        outerLayout.addWidget(headerTextFormatLabel, 2, 0)
        outerLayout.addWidget(self.headerTextFormatCombo, 2, 1)
        outerLayout.addLayout(checkBoxLayout, 3, 0, 1, 2)
        self.textFormatsGroupBox.setLayout(outerLayout)

        self.weekdayFormatChanged()
        self.weekendFormatChanged()
        self.reformatHeaders()
        self.reformatCalendarPage()

    def createColorComboBox(self):
        comboBox = QComboBox()
        comboBox.addItem('Red', QColor(Qt.red))
        comboBox.addItem('Blue', QColor(Qt.blue))
        comboBox.addItem('Black', QColor(Qt.black))
        comboBox.addItem('Magenta', QColor(Qt.magenta))
        return comboBox

    def localeChanged(self, index):
        newLocale = QLocale(self.localeCombo.itemData(index))
        self.calendar.setLocale(newLocale)
        newLocaleFirstDayIndex = self.firstDayCombo.findData(newLocale.firstDayOfWeek())
        self.firstDayCombo.setCurrentIndex(newLocaleFirstDayIndex)

    def firstDayChanged(self, index):
        self.calendar.setFirstDayOfWeek(self.firstDayCombo.itemData(index))

    def selectionModeChanged(self, index):
        self.calendar.setSelectionMode(self.selectionModeCombo.itemData(index))

    def horizontalHeaderChanged(self, index):
        self.calendar.setHorizontalHeaderFormat(self.horizontalHeaderCombo.itemData(index))

    def veritcalHeaderChanged(self, index):
        self.calendar.setVerticalHeaderFormat(self.verticalHeaderCombo.itemData(index))

    def selectDateChanged(self):
        self.currentDateEdit.setDate(self.calendar.selectedDate())

    def minimumDateChanged(self, date):
        self.calendar.setMinimumDate(date)
        self.maximumDateEdit.setDate(self.calendar.maximumDate())

    def maximumDateChanged(self, date):
        self.calendar.setMaximumDate(date)
        self.minimumDateEdit.setDate(self.calendar.minimumDate())

    def weekdayFormatChanged(self):
        txFormat = QTextCharFormat()

        txFormat.setForeground(self.weekdayColorCombo.itemData(self.weekdayColorCombo.currentIndex()))
        self.calendar.setWeekdayTextFormat(Qt.Monday, txFormat)
        self.calendar.setWeekdayTextFormat(Qt.Tuesday, txFormat)
        self.calendar.setWeekdayTextFormat(Qt.Wednesday, txFormat)
        self.calendar.setWeekdayTextFormat(Qt.Thursday, txFormat)
        self.calendar.setWeekdayTextFormat(Qt.Friday, txFormat)

    def weekendFormatChanged(self):
        txFormat = QTextCharFormat()

        txFormat.setForeground(self.weekendColorCombo.itemData(self.weekendColorCombo.currentIndex()))
        self.calendar.setWeekdayTextFormat(Qt.Saturday, txFormat)
        self.calendar.setWeekdayTextFormat(Qt.Sunday, txFormat)

    def reformatHeaders(self):
        text = self.headerTextFormatCombo.currentText()
        txFormat = QTextCharFormat()

        if text == 'Bold':
            txFormat.setFontWeight(QFont.Bold)
        elif text == 'Italic':
            txFormat.setFontItalic(True)
        elif text == 'Green':
            txFormat.setForeground(Qt.green)
        self.calendar.setHeaderTextFormat(txFormat)

    def reformatCalendarPage(self):
        mayFirstFormat = QTextCharFormat()
        mayFirst = QDate(self.calendar.yearShown(), 5, 1)

        firstFridayFormat = QTextCharFormat()
        firstFriday = QDate(self.calendar.yearShown(), self.calendar.monthShown(), 1)
        while firstFriday.dayOfWeek() != Qt.Friday:
            firstFriday = firstFriday.addDays(1)

        if self.firstFridayCheckBox.isChecked():
            firstFridayFormat.setForeground(Qt.blue)
        else:
            dayOfWeek = firstFriday.dayOfWeek()
            firstFridayFormat.setForeground(self.calendar.weekdayTextFormat(dayOfWeek).foreground())

        self.calendar.setDateTextFormat(firstFriday, firstFridayFormat)

        if self.mayFirstCheckBox.isChecked():
            mayFirstFormat.setForeground(Qt.red)
        elif not self.firstFridayCheckBox.isChecked():
            dayOfWeek = mayFirst.dayOfWeek()
            self.calendar.setDateTextFormat(mayFirst, self.calendar.weekdayTextFormat(dayOfWeek))

        self.calendar.setDateTextFormat(mayFirst, mayFirstFormat)

app=Flask(__name__)
@app.route('/')
def hello_world():
    apple = QApplication(sys.argv)
    win = Window()
    win.show()
    apple.exec_()

if __name__ == '__main__':
    app.run()